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


#Leave this commented, in case you need
#Namedfile, if you want to add a pdf field
#from plone.namedfile import field as namedfile

#from zope.schema.vocabulary import SimpleTerm
#from zope.schema.vocabulary import SimpleVocabulary
#from plone.schema import Email


from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')


class IActivity(model.Schema):
    """ Marker interface for Activity
    """

    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Persons'),
        default=[],
        value_type=RelationChoice(
            title=u'Persons',
            source=CatalogSource(portal_type=['Person', 'person']),
        ),
        required=False,
    )

    relatedLanguageItems = schema.List(
        title=_(u'label_related_items', default=u'Persons'),
        default=[],
        value_type=schema.Choice(
            title=u'Persons',
            vocabulary='acentoweb.mediaflows.PersonVocabulary',
        ),
        required=False,
    )

    relatedItemsTwo = RelationList(
        title=_(u'label_related_items', default=u'Persons'),
        default=[],
        value_type=RelationChoice(
            title=u'Persons',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    ## zope.schema.Choice">


    #change base path to '/persons' if you decide to put them all there

    directives.widget(
        'relatedItems',
        RelatedItemsFieldWidget,
        pattern_options={
            'basePath': '/',
            "mode": "auto",
            "favorites": []
            }
        )

    directives.widget(
        "relatedItemsTwo",
        RelatedItemsFieldWidget,
        pattern_options={
             "selectableTypes": ["Person", "person"],
        },
    )

     


@implementer(IActivity)
class Activity(Item):
    """
    """
