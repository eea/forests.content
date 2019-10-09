# import logging
# from plone.indexer.decorator import indexer
# from plone.rfc822.interfaces import IPrimaryFieldInfo
# from forests.content.contenttypes import IRichImage
#
#
# logger = logging.getLogger('forests.content')
#
#
# @indexer(IRichImage)
# def getObjSize_image(obj):
#     try:
#         primary_field_info = IPrimaryFieldInfo(obj)
#     except TypeError:
#         logger.warn(
#             u'Lookup of PrimaryField failed for {0} If renaming or importing '
#             u'please reindex!'.format(obj.absolute_url())
#         )
#         return
#     return obj.getObjSize(None, primary_field_info.value.size)
