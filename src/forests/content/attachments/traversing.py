from zope.traversing.namespace import SimpleHandler

from six.moves import urllib
from zExceptions import NotFound

from .interfaces import IAttachmentStorage


class AttachmentTraversing(SimpleHandler):
    name = None

    def __init__(self, context, request=None):
        self.context = context

    def traverse(self, name, remaining):

        # Note: also fixes possible unicode problems
        attach_name = urllib.parse.quote(name)
        container = self.name

        storage = IAttachmentStorage(self.context)

        if container not in storage:
            raise NotFound

        if attach_name not in storage[container]:
            raise NotFound

        return storage[container][attach_name]
