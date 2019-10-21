from persistent.mapping import PersistentMapping
from zope.annotation.factory import factory
from zope.component import adapter
from zope.interface import implements

from .interfaces import IHasSliderImages, ISliderImagesStorage


@adapter(IHasSliderImages)
class SliderImages(PersistentMapping):
    """ Slider images stored in a persistent mapping
    """
    implements(ISliderImagesStorage)


slides_annotation_storage = factory(SliderImages, key='slider.images.storage')
