import logging

from forests.content.interfaces import (IBasicMetadata, IContentMetadata,
                                        IGeospatialMetadata)
from plone.app.dexterity.behaviors.metadata import (DCFieldProperty,
                                                    MetadataBase)

logger = logging.getLogger(__name__)


class BasicMetadata(MetadataBase):
    """ Optional Fise metadata adaptor
    """

    topics = DCFieldProperty(IBasicMetadata['topics'])
    keywords = DCFieldProperty(IBasicMetadata['keywords'])


class ContentMetadata(MetadataBase):
    """ Standard Fise Metadata adaptor
    """

    resource_type = DCFieldProperty(IContentMetadata['resource_type'])
    data_source = DCFieldProperty(IContentMetadata['data_source'])
    dataset = DCFieldProperty(IContentMetadata['dataset'])
    publisher = DCFieldProperty(IContentMetadata['publisher'])
    external_url = DCFieldProperty(IContentMetadata['external_url'])
    geo_coverage = DCFieldProperty(IContentMetadata['geo_coverage'])
    publishing_year = DCFieldProperty(IContentMetadata['publishing_year'])
    collection_year_start = DCFieldProperty(
        IContentMetadata['collection_year_start'])
    collection_year_end = DCFieldProperty(
        IContentMetadata['collection_year_end'])
    info_level = DCFieldProperty(IContentMetadata['info_level'])
    accessibility_level = DCFieldProperty(
        IContentMetadata['accessibility_level'])
    nuts_level = DCFieldProperty(IContentMetadata['nuts_level'])


class GeospatialMetadata(MetadataBase):
    """ Fise Geospatial metadata adaptor
    """

    spatial_resolution = DCFieldProperty(
        IGeospatialMetadata['spatial_resolution'])
    coordinate_system = DCFieldProperty(
        IGeospatialMetadata['coordinate_system'])
