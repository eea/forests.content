# from zope.component import adapter
# from zope.interface import Interface, implementer
#
# from plone.app.contenttypes.behaviors.richtext import IRichText
# from plone.supermodel import interfaces
#
# KEY = 'forests.tweaks.richtext'
#
#
# @implementer(interfaces.ISchemaPlugin)
# @adapter(IRichText)
# class TweakRichTextSchema(object):
#     """
#     """
#
#     order = 1000
#
#     def __init__(self, schema):
#         self.schema = schema
#
#     def __call__(self):
#         pass
#
#
# IRichText.setTaggedValue(KEY,
#                          [
#                              (Interface, 'blocks', 'true'),
#                          ]
#                          )
