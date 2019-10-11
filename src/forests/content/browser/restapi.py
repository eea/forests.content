from zope.component import adapter
from zope.interface import Interface, implementer

from forests.content.interfaces import IDataProvider
from plone.restapi.interfaces import IExpandableElement


@implementer(IExpandableElement)
@adapter(IDataProvider, Interface)
class ConnectorData(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            "connector-data": {
                "@id": "{}/@connector-data".format(self.context.absolute_url())
            }
        }

        if not expand:
            return result

        connector = IDataProvider(self.context)
        result['connector-data']["data"] = connector.provided_data

        return result