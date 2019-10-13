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
from plone.supermodel import directives, model
from z3c.formwidget.optgroup.widget import OptgroupFieldWidget


class IForestsContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


@provider(IFormFieldProvider)
class IMetadata(model.Schema):
    """ Generic metadata for forests data types
    """

    directives.fieldset('fise-metadata', label="Forests Metadata", fields=[
        'resource_type',
        'data_source',
        'dataset',
        'publisher',
        'external_url',
        'geo_coverage',
        'publishing_year',
        'collection_year_start',
        'collection_year_end',
        'topics',
        'keywords',
        'info_level',
        'accessibility_level',
    ])

    resource_type = schema.Choice(title=u'Resource type',
                                  vocabulary="fise.resource_types",
                                  required=False,
                                  )

    data_source = schema.Choice(
        title=u"Data Source",
        vocabulary="fise.data_sources",
        required=False,

    )
    form.widget(
        'data_source',
        OptgroupFieldWidget,
        vocabulary='fise.data_sources'
    )

    dataset = schema.Choice(title=u"Dataset", vocabulary="fise.datasets",
                            required=False)

    publisher = schema.TextLine(
        title=u"Publisher",
        required=False,
    )
    form.widget(        # text with autocomplete
        'publisher',
        AjaxSelectFieldWidget,
        vocabulary='fise.publishers'
    )

    external_url = schema.TextLine(title=u"Link to resource", required=False)

    geo_coverage = schema.Tuple(
        title=u"Geographical coverage",
        value_type=schema.Choice(vocabulary="fise.geocoverage"),
        required=False,
        missing_value=(),
        default=(),
    )

    publishing_year = schema.Int(title=u"Publishing year", required=False,)

    # interval between 2 years
    collection_year_start = schema.TextLine(title=u"Collection start year",
                                            required=False,)
    collection_year_end = schema.TextLine(title=u"Collection end year",
                                          required=False,)

    topics = schema.Tuple(
        title=u"Topics",
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    form.widget(
        'topics',
        AjaxSelectFieldWidget,
        vocabulary='fise.topics'
    )

    keywords = schema.Tuple(
        title=u"Keywords",
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=()
    )
    form.widget(
        'keywords',
        AjaxSelectFieldWidget,
        vocabulary='fise.keywords'
    )

    info_level = schema.Choice(title=u"Info level",
                               vocabulary='fise.info_levels',
                               required=False,)

    accessibility_level = schema.Choice(title=u'Accesibility levels',
                                        vocabulary='fise.accessibility_levels',
                                        required=False,)


@provider(IFormFieldProvider)
class IOptionalMetadata(model.Schema):
    """ Generic optional metadata for forests data types
    """

    nuts_level = schema.Tuple(
        title=u"NUTS Levels",
        value_type=schema.Choice(vocabulary="fise.nuts_levels"),
        required=False,
        missing_value=(),
        default=(),
    )
    directives.fieldset('fise-metadata', label="Forests Metadata", fields=[
        'nuts_level',
    ])


class IComputedMetadata(Interface):
    """ Forests Metadata fields that are automatically computed
    """

    resource_format = Attribute(u'Extracted from file extension')


@provider(IFormFieldProvider)
class IDataConnector(model.Schema):
    """ A generic discodata connector
    """

    endpoint_url = schema.TextLine(
        title=u"Discodata endpoint URL", required=True,
        default=u"http://discomap.eea.europa.eu/App/SqlEndpoint/query"
    )
    query = schema.Text(
        title=u"SQL Query",
        required=True,
    )

    # directives.fieldset('dataconnector', label="Data connector", fields=[
    #     'endpoint_url', 'query',
    # ])


class IBasicDataProvider(Interface):
    """ A data provider concept
    """


class IDataProvider(IBasicDataProvider):
    """ An export of data for remote purposes
    """

    provided_data = Attribute(u'Data made available by this data provider')


class IFileDataProvider(IBasicDataProvider):
    """ Marker interface for objects that provide data to visualizations
    """


class IConnectorDataProvider(IBasicDataProvider):
    """ Marker interface for objects that provide data to visualizations
    """


VIZ_SCHEMA = json.dumps({"type": "object", "properties": {}})


@provider(IFormFieldProvider)
class IDataVisualization(model.Schema):
    """ A data visualization (chart)
    """

    visualization = JSONField(title=u"Visualization", required=False,
                              default={},
                              schema=VIZ_SCHEMA)
