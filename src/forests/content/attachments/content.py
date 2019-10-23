from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from Acquisition import Implicit
from OFS.OrderedFolder import OrderedFolder
from OFS.SimpleItem import SimpleItem

from .interfaces import (IAttachedFile, IAttachedImage, IAttachment,
                         IAttachmentFolder)


class Attachment(SimpleItem):
    """ Attachment implementation
    """
    implements(IAttachment)

    file = FieldProperty(IAttachment['file'])
    text = FieldProperty(IAttachment['text'])


class AttachedFile(Attachment):
    """ Attachment implementation
    """
    implements(IAttachedFile)

    file = FieldProperty(IAttachedFile['file'])


class AttachedImage(Attachment):
    """ Attachment implementation
    """
    implements(IAttachedImage)

    file = FieldProperty(IAttachedImage['file'])


class AttachmentFolder(OrderedFolder, Implicit):
    """
    """
    implements(IAttachmentFolder)

    def getPhysicalPath(self):
        # override, to be able to provide a fake name for the physical path
        # should probably set this as folder id
        path = super(AttachmentFolder, self).getPhysicalPath()
        path = () + path[:-1] + ('++attachment++' + path[-1], )

        return path


# class Fake(Implicit):
#     def __init__(self, name, parent):
#         super(Fake, self).__init__()
#         self.id = self.__name__ = self
#         self.__parent__ = parent
