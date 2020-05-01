''' views '''
from Products.Five.browser import BrowserView


class DebugView(BrowserView):
    """DebugView."""

    def __call__(self):

        import pdb
        pdb.set_trace()

        return 'ok'
