from forests.content.interfaces import IDataConnector
from Products.Five.browser import BrowserView


class DataConnectorView(BrowserView):
    """ Basic view for the DataConnector
    """

    def data(self):
        if self.context.query:
            connector = IDataConnector(self.context)

            return connector.data['results']

        return []
