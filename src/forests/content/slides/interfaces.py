from zope.interface import Interface

# class ISliderImagesBehavior(Interface):
#     """ Behavior for slider images
#     """


class IHasSliderImages(Interface):
    """ Marker interface for objects that provide slider images
    """


class ISliderImagesStorage(Interface):
    """ Annotation based storage for slider images
    """
