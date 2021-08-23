# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model

from zope.interface import implementer
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource


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


    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('activity.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )



@implementer(IActivity)
class Activity(Item):
    """
    """
