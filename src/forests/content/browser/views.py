''' views '''
import json
from Products.Five.browser import BrowserView


class DebugView(BrowserView):
    """DebugView."""

    def __call__(self):

        import pdb
        pdb.set_trace()

        return 'ok'


class DocumentViewWide(BrowserView):
    """ A fallback view for Document View Wide default layout pages
    """

    def blocks(self):
        ''' load blocks from json '''
        blocks = getattr(self.context.aq_inner.aq_self, 'blocks', '{}')

        return json.loads(blocks)
