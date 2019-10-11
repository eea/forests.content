from forests.content.interfaces import IDataProvider
from Products.Five.browser import BrowserView


class DataConnectorView(BrowserView):
    """ Basic view for the DataConnector
    """

    def data(self):
        self.context = IDataProvider(self.context)

        return self.context.provided_data


class DebugView(BrowserView):
    def __call__(self):

        import pdb
        pdb.set_trace()

        return 'ok'
