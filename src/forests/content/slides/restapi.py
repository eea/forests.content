from random import randint

from DateTime import DateTime
from plone.namedfile.file import NamedBlobImage
from plone.restapi.deserializer import json_body
from plone.restapi.services import Service


class ContentPost(Service):
    """Creates a new content object.
    """

    def reply(self):
        data = json_body(self.request)

        text = data.get("text", None)
        # content-type, data, filename, encoding
        image = data.get("image", None)

        if not image:
            return {}

        blob = NamedBlobImage(
            data=data,
            filename=data['filename'],
            contentType=data['content-type'],
        )

        now = DateTime()
        new_id = "slide.{}.{}{:04d}".format(
            now.strftime("%Y-%m-%d"),
            str(now.millis())[7:],
            randint(0, 9999),
        )
