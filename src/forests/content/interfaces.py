# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

import json

from zope import schema
from zope.interface import Attribute, Interface, provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema import JSONField
from plone.supermodel import model
from plone.app.textfield import RichText


class IForestsContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


COLLECTION_YEARS_SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "start_year": {
            "type": "string"
        },
        "end_year": {
            "type": "string"
        }
    }
})


@provider(IFormFieldProvider)
class ILeadImageControls(model.Schema):
    """ FISE lead image controls
    """

    model.fieldset('lead_image_controls',
                   label="Lead Image Controls",
                   fields=[
                       'big_leading_image', 'inherit_leading_data',
                       'lead_navigation', 'lead_image_caption'
                   ])

    big_leading_image = schema.Bool(
        title='Big Leading Image',
        description='Set Leading image bigger',
        required=False,
    )
    inherit_leading_data = schema.Bool(
        title='Inherit Leading Data',
        description='Inherit Leading image and text from parent',
        required=False,
    )
    lead_navigation = schema.Bool(
        title='Lead Navigation',
        description='Insert Navigation from parent',
        required=False,
    )
    lead_image_caption = RichText(
        title="FISE Lead Image Caption",
        description="Metadata caption visible in lead image",
        required=False,
    )


@provider(IFormFieldProvider)
class IBasicMetadata(model.Schema):
    """ FISE generic required metadata
    """

    topics = schema.Tuple(
        title=u"Topics",
        description=u"Relevant FISE topic",
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    form.widget('topics',
                AjaxSelectFieldWidget,
                vocabulary='collective.taxonomy.topics')

    keywords = schema.Tuple(title=u"Keywords",
                            description=u"Relevant FISE keywords",
                            value_type=schema.TextLine(),
                            required=False,
                            missing_value=(),
                            default=())
    form.widget('keywords',
                AjaxSelectFieldWidget,
                vocabulary='collective.taxonomy.keywords')


@provider(IFormFieldProvider)
class IContentMetadata(model.Schema):
    """ FISE specific content metadata
    """
    # directives.fieldset('fise-metadata', label="Forests Metadata", fields=[
    #     'nuts_level',
    # ])

    resource_type = schema.Choice(
        title=u'Resource type',
        # description=u"Type of result; for NFI the values are taken from the"
        #             u"'Result format' field",
        vocabulary="collective.taxonomy.resource_type",
        required=False,
    )

    nuts_level = schema.Tuple(
        title=u"NUTS Levels",
        description=u"Nomenclature of territorial units for statistics level",
        value_type=schema.Choice(vocabulary="collective.taxonomy.nuts_levels"),
        required=False,
        missing_value=(),
        default=(),
    )

    dataset = schema.Choice(title=u"Dataset",
                            description=u"The provenance dataset",
                            vocabulary="collective.taxonomy.datasets",
                            required=False)

    data_source = schema.Choice(
        title=u"Data Source",
        description=u"The source for the data (not its publisher!)",
        vocabulary="collective.taxonomy.data_sources",
        required=False,
    )
    # form.widget(
    #     'data_source',
    #     OptgroupFieldWidget,
    #     vocabulary='collective.taxonomy.data_sources'
    # )

    collection_years = JSONField(
        title=u"Collection years",
        description=u"Start year - end year",  # noqa
        schema=COLLECTION_YEARS_SCHEMA,
        default={},
        required=False,
    )

    publisher = schema.Tuple(
        title=u"Publisher",
        description=u"Owner/Responsible Organisation",
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    form.widget(  # text with autocomplete
        'publisher',
        AjaxSelectFieldWidget,
        vocabulary='collective.taxonomy.publishers')

    publishing_year = schema.Int(
        title=u"Publishing year",
        required=False,
    )

    external_url = schema.TextLine(title=u"Link to resource", required=False)

    info_level = schema.Choice(
        title=u"Info level",
        vocabulary='collective.taxonomy.info_levels',
        required=False,
    )

    accessibility_level = schema.Choice(
        title=u'Accesibility levels',
        description=u"Level of access, from 'public' to restricted'",
        vocabulary='collective.taxonomy.accessibility_levels',
        required=False,
    )

    geo_coverage = schema.Tuple(
        title=u"Geographical coverage",
        description=u"Geographic areas covered by this resource",
        value_type=schema.Choice(
            vocabulary="collective.taxonomy.geographical_coverage"),
        required=False,
        missing_value=(),
        default=(),
    )


@provider(IFormFieldProvider)
class IGeospatialMetadata(model.Schema):
    """ FISE geospatial metadata
    """

    spatial_resolution = schema.TextLine(
        title=u"Spatial resolution",
        required=False,
    )
    coordinate_system = schema.TextLine(
        title=u"Coordinate system",
        required=False,
    )


class IComputedMetadata(Interface):
    """ Forests Metadata fields that are automatically computed
    """

    resource_format = Attribute(u'Extracted from file extension')


# directives.fieldset('fise-metadata', label="Forests Metadata", fields=[
#     'resource_type',
#     'data_source',
#     'dataset',
#     'publisher',
#     'external_url',
#     'geo_coverage',
#     'publishing_year',
#     'collection_year_start',
#     'collection_year_end',
#     'topics',
#     'keywords',
#     'info_level',
#     'accessibility_level',
# ])

# publisher = schema.TextLine(
#     title=u"Publisher",
#     required=False,
# )

# # interval between 2 years
# collection_year_start = schema.TextLine(title=u"Collection start year",
#                                         required=False,)
# collection_year_end = schema.TextLine(title=u"Collection end year",
#                                       required=False,)
