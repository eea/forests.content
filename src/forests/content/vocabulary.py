from zope.interface import alsoProvides, implementer, provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from plone.app.vocabularies.catalog import KeywordsVocabulary as KV
from z3c.formwidget.optgroup.widget import OptgroupTerm

from .constants import (ACCESSIBILITY_LEVELS, DATA_SOURCES, DATASETS,
                        GEOCOVERAGE_REGIONS, NUTS_LEVELS, RESOURCE_TYPES)


@implementer(IVocabularyFactory)
class KeywordsVocabulary(KV):
    def __init__(self, index):
        self.keyword_index = index


def generic_vocabulary(_terms, sort=True):
    """ Returns a zope vocabulary from a dict or a list
    """

    if _terms and isinstance(_terms, dict):
        _terms = _terms.items()
    elif _terms and isinstance(_terms[0], basestring):
        _terms = [(x, x) for x in _terms]

    if sort:
        _terms = sorted(_terms, key=lambda x: x[0])

    def factory(context):
        return SimpleVocabulary([
            SimpleTerm(n, n.encode('utf-8'), l) for n, l in _terms
        ])

    return factory


@provider(IVocabularyFactory)
def data_sources_vocabulary(context):
    terms = []

    for (source, items) in DATA_SOURCES:
        for item in items:
            terms.append(OptgroupTerm(value=item, token=item,
                                      title=item, optgroup=source))

    return SimpleVocabulary(terms)


resource_types_vocabulary = generic_vocabulary(RESOURCE_TYPES)
alsoProvides(resource_types_vocabulary, IVocabularyFactory)


nuts_levels_vocabulary = generic_vocabulary(NUTS_LEVELS)
alsoProvides(nuts_levels_vocabulary, IVocabularyFactory)

datasets_vocabulary = generic_vocabulary(DATASETS)
alsoProvides(datasets_vocabulary, IVocabularyFactory)

geocoverage_vocabulary = generic_vocabulary(GEOCOVERAGE_REGIONS)
alsoProvides(geocoverage_vocabulary, IVocabularyFactory)

accessibility_vocabulary = generic_vocabulary(ACCESSIBILITY_LEVELS)
alsoProvides(accessibility_vocabulary, IVocabularyFactory)

PublishersVocabularyFactory = KeywordsVocabulary('publisher')
TopicsVocabularyFactory = KeywordsVocabulary('topics')
KeywordsVocabularyFactory = KeywordsVocabulary('keywords')
