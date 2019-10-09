from plone.app.dexterity.behaviors.metadata import (DCFieldProperty,
                                                    MetadataBase)

from .interfaces import IMetadata, IOptionalMetadata


class Metadata(MetadataBase):
    """ Standard Fise Metadata adaptor
    """
    resource_type = DCFieldProperty(IMetadata['resource_type'])
    data_source = DCFieldProperty(IMetadata['data_source'])
    dataset = DCFieldProperty(IMetadata['dataset'])
    publisher = DCFieldProperty(IMetadata['publisher'])
    external_url = DCFieldProperty(IMetadata['external_url'])
    geo_coverage = DCFieldProperty(IMetadata['geo_coverage'])
    publishing_year = DCFieldProperty(IMetadata['publishing_year'])
    collection_year_start = DCFieldProperty(IMetadata['collection_year_start'])
    collection_year_end = DCFieldProperty(IMetadata['collection_year_end'])
    topics = DCFieldProperty(IMetadata['topics'])
    keywords = DCFieldProperty(IMetadata['keywords'])
    info_level = DCFieldProperty(IMetadata['info_level'])
    accessibility_level = DCFieldProperty(IMetadata['accessibility_level'])


class OptionalMetadata(MetadataBase):
    """ Optional Fise metadata adaptor
    """

    nuts_level = DCFieldProperty(IOptionalMetadata['nuts_level'])


class DataConnector(MetadataBase):
    """ Allow data connectivity to discodata
    """
