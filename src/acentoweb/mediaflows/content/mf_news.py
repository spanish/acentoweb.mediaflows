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

class IMFNews(model.Schema):
    """ Marker interface for MF News
    """

    news_categories = schema.Set (
        title=_(u'label_news_categories', default=u'Categories'),
        description=_(u'label_news_categories_description', default=u'News categories'),
        value_type=schema.Choice(
            title = _("label_news_categories", default=u"Categories"),
            vocabulary = 'collective.taxonomy.mf_news_categories',
            required = True
        )
    )

    relatedPersons = RelationList(
        title=_(u'label_news_related_persons', default=u'Persons'),
        default=[],
        value_type=RelationChoice(
            title=u'Persons',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    directives.widget(
        'relatedPersons',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

@implementer(IMFNews)
class MFNews(Item):
    """
    """
