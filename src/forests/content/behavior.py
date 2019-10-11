import csv
import logging
from collections import defaultdict
from io import StringIO

import requests
from zope.component import adapter
from zope.interface import implementer

from forests.content.interfaces import IDataProvider, IFileDataProvider
from plone.app.dexterity.behaviors.metadata import (DCFieldProperty,
                                                    MetadataBase)
from plone.rfc822.interfaces import IPrimaryFieldInfo

from .interfaces import IDataConnector, IMetadata, IOptionalMetadata

# from plone.dexterity.interfaces import IDexterityContent

logger = logging.getLogger(__name__)


class Metadata(MetadataBase):
    """ Standard Fise Metadata adaptor
    """
    resource_type = DCFieldProperty(IMetadata['resource_type'])
    data_source = DCFieldProperty(IMetadata['data_source'])
    dataset = DCFieldProperty(IMetadata['dataset'])
    publisher = DCFieldProperty(IMetadata['publisher'])
    external_url = DCFieldProperty(IMetadata['external_url'])
    geo_coverage = DCFieldProperty(IMetadata['geo_coverage'])
    publishing_year = DCFieldProperty(IMetadata['publishing_year'])
    collection_year_start = DCFieldProperty(IMetadata['collection_year_start'])
    collection_year_end = DCFieldProperty(IMetadata['collection_year_end'])
    topics = DCFieldProperty(IMetadata['topics'])
    keywords = DCFieldProperty(IMetadata['keywords'])
    info_level = DCFieldProperty(IMetadata['info_level'])
    accessibility_level = DCFieldProperty(IMetadata['accessibility_level'])


class OptionalMetadata(MetadataBase):
    """ Optional Fise metadata adaptor
    """

    nuts_level = DCFieldProperty(IOptionalMetadata['nuts_level'])


class DataConnector(MetadataBase):
    """ Allow data connectivity to discodata

    See http://discomap.eea.europa.eu/App/SqlEndpoint/Browser.aspx
    """

    endpoint_url = DCFieldProperty(IDataConnector['endpoint_url'])
    query = DCFieldProperty(IDataConnector['query'])

    def _get_data(self):
        # query = urllib.parse.quote_plus(self.query)

        try:
            req = requests.post(self.endpoint_url, data={'sql': self.query})
            res = req.json()
        except Exception:
            logger.exception("Error in requestion data")
            res = {'result': []}

        return res

    def change_orientation(self, data):
        res = {}

        if not data:
            return res

        keys = data[0].keys()

        # in-memory built, should optimize

        for k in keys:
            res[k] = [row[k] for row in data]

        return res

    @property
    def provided_data(self):
        if not self.query:
            return []

        data = self._get_data()

        return self.change_orientation(data['results'])


@implementer(IDataProvider)
@adapter(IFileDataProvider)
class DataProviderForFiles(object):
    """ Behavior implementation for content types with a File primary field
    """

    def __init__(self, context):
        self.context = context

    @property
    def provided_data(self):
        field = IPrimaryFieldInfo(self.context)

        if not field.value:
            return []

        text = field.value.data
        f = StringIO(text.decode('utf-8'))
        try:
            reader = csv.reader(f)
        except:
            return []

        rows = list(reader)

        if not rows:
            return []

        keys = rows[0]
        res = defaultdict(list)

        for (k, i) in enumerate(keys):
            for row in rows[1:]:
                res[k].append(row[i])

        return res
