from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from OFS.OrderedFolder import OrderedFolder
from OFS.SimpleItem import SimpleItem

from .interfaces import IAttachment


class Attachment(SimpleItem):
    """ Attachment implementation
    """
    implements(IAttachment)

    file = FieldProperty(IAttachment['file'])
    text = FieldProperty(IAttachment['text'])


class AttachmentFolder(OrderedFolder):
    """
    """

    def getPhysicalPath(self):
        # override, to be able to provide a fake name for the physical path
        path = super(AttachmentFolder, self).getPhysicalPath()
        path = () + path[:-1] + ('++attachment++' + path[-1], )

        return path
