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
from acentoweb.mediaflows.vocabulary import PersonVocabulary

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')


class IActivity(model.Schema):
    """ Marker interface for Activity
    """

    relatedItems =  RelationList(
        title=_(u'label_related_items', default=u'Persons'),
        default=[],
        value_type=RelationChoice(
            title=u'Persons',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )





@implementer(IActivity)
class Activity(Item):
    """
    """
