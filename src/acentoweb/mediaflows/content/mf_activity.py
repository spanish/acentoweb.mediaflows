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

    relatedSpeakers = RelationList(
        title=_(u'label_related_speakers', default=u'MF Speakers'),
        default=[],
        value_type=RelationChoice(
            title=u'MF Speakers',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    relatedCommunicators = RelationList(
        title=_(u'label_related_communicators', default=u'MF Communicators'),
        default=[],
        value_type=RelationChoice(
            title=u'MF Communicators',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedAssistants = RelationList(
        title=_(u'label_related_assistants', default=u'MF Assistants'),
        default=[],
        value_type=RelationChoice(
            title=u'MF Assistants',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedModerators = RelationList(
        title=_(u'label_related_moderators', default=u'MF Moderators'),
        default=[],
        value_type=RelationChoice(
            title=u'MF Moderators',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )


    relatedOrganizers = RelationList(
        title=_(u'label_related_organizers', default=u'MF Organizers'),
        default=[],
        value_type=RelationChoice(
            title=u'MF Organizers',
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
