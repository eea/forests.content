from zope.component import adapter
from zope.interface import Interface, implementer

from forests.content.interfaces import IDataConnector, IDataProvider
from plone.restapi.interfaces import IExpandableElement


@implementer(IExpandableElement)
@adapter(IDataProvider, Interface)
class ConnectorData(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def change_orientation(self, data):
        res = {}

        if not data:
            return res

        keys = data[0].keys()

        # in-memory built, should optimize

        for k in keys:
            res[k] = [row[k] for row in data]

        return res

    def __call__(self, expand=False):
        result = {
            "connector-data": {
                "@id": "{}/@connector-data".format(self.context.absolute_url())
            }
        }

        if not expand:
            return result

        connector = IDataConnector(self.context)
        result['connector-data']["data"] = connector.data['results']

        return result
