from zope.component import adapter
from zope.interface import implementer

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import interfaces


@implementer(interfaces.ISchemaPlugin)
@adapter(IFormFieldProvider)
class TweakRichTextSchema(object):
    """
    """

    order = 10001

    def __init__(self, schema):
        self.schema = schema

    def __call__(self):
        if self.schema.getName() == 'IRichTextBehavior':
            field = self.schema['text']
            field.description = u'Rich text, double click for toolbar'
