from zope.component import adapter, queryMultiAdapter
from zope.interface import Interface, implementer
from zope.schema import getFields

from plone.namedfile.interfaces import INamedFileField
from plone.restapi.interfaces import IFieldSerializer, ISerializeToJson
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import (DefaultFieldSerializer,
                                               FileFieldSerializer,
                                               ImageFieldSerializer)

from .interfaces import IAttachment


@implementer(ISerializeToJson)
@adapter(IAttachment, Interface)
class SerializeToJson(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, version=None, include_items=True):
        obj = self.context
        result = {
            # '@context': 'http://www.w3.org/ns/hydra/context.jsonld',
            "@id": obj.absolute_url(),
            "id": obj.id,
        }

        for name, field in getFields(IAttachment).items():

            serializer = queryMultiAdapter(
                (field, obj, self.request), IFieldSerializer
            )

            assert serializer
            value = serializer()
            result[json_compatible(name)] = value

        return result


@adapter(INamedFileField, IAttachment, Interface)
@implementer(IFieldSerializer)
class AttachmentFileSerializer(DefaultFieldSerializer):

    def __call__(self):
        namedfile = self.field.get(self.context)

        if namedfile is None:
            return None

        ctype = namedfile.contentType

        if 'image' in ctype:
            return ImageFieldSerializer(self.field, self.context,
                                        self.request)()
        else:
            return FileFieldSerializer(self.field, self.context,
                                       self.request)()
