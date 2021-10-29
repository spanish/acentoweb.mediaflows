# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from acentoweb.mediaflows.vocabulary import PersonsVocabulary

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')

class IMFActivity(model.Schema):
    """ Marker interface for MF Activity
    """

    activity_types = schema.Set (
        title=_(u'label_activity_types', default=u'Types'),
        description=_(u'label_activity_types_description', default=u'Activity types'),
        value_type=schema.Choice(
            title = _("label_activity_types", default=u"Types"),
            vocabulary = 'collective.taxonomy.mf_activity_types',
            required = True
        )
    )

    activity_categories = schema.Set (
        title=_(u'label_activity_categories', default=u'Categories'),
        description=_(u'label_activity_categories_description', default=u'Activity categories'),
        value_type=schema.Choice(
            title = _("label_activity_categories", default=u"Categories"),
            vocabulary = 'collective.taxonomy.mf_activity_categories',
            required = True
        )
    )

    start = schema.Datetime(
        title=_(u'label_activity_start', default=u'Start'),
        description=_(u'label_activity_start_description', default=u'Activity datetime start'),
        required=True
    )

    location = schema.TextLine(
        title=_(u'label_activity_location', default=u'Location'),
        description=_(u'label_activity_location_description', default=u'Activity location'),
        required=True,
    )

    video = schema.URI(
        title=_(u'label_activity_orcid', default=u'Video'),
        description=_(u'label_activity_orcid_description', default=u'Video URL'),
        required=False,
        missing_value=u'',
    )

    relatedSpeakers = RelationList(
        title=_(u'label_activity_related_speakers', default=u'Speakers'),
        default=[],
        value_type=RelationChoice(
            title=u'Speakers',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    relatedCommunicators = RelationList(
        title=_(u'label_activity_related_communicators', default=u'Communicators'),
        default=[],
        value_type=RelationChoice(
            title=u'Communicators',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedAssistants = RelationList(
        title=_(u'label_activity_related_assistants', default=u'Assistants'),
        default=[],
        value_type=RelationChoice(
            title=u'Assistants',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedModerators = RelationList(
        title=_(u'label_activity_related_moderators', default=u'Moderators'),
        default=[],
        value_type=RelationChoice(
            title=u'Moderators',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedOrganizers = RelationList(
        title=_(u'label_activity_related_organizers', default=u'Organizers'),
        default=[],
        value_type=RelationChoice(
            title=u'Organizers',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    directives.widget(
        'relatedSpeakers',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

    directives.widget(
        'relatedCommunicators',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

    directives.widget(
        'relatedAssistants',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

    directives.widget(
        'relatedModerators',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

    directives.widget(
        'relatedOrganizers',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )


@implementer(IMFActivity)
class MFActivity(Item):
    """
    """
