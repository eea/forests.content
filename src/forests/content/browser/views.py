from forests.content.interfaces import IDataProvider
from Products.Five.browser import BrowserView


class DataConnectorView(BrowserView):
    """ Basic view for the DataConnector
    """

    def data(self):
        if self.context.query:
            self.context = IDataProvider(self.context)

            return self.context.data['results']

        return []


class DebugView(BrowserView):
    def __call__(self):

        import pdb
        pdb.set_trace()

        return 'ok'
