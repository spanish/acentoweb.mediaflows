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

class IMFPublication(model.Schema):
    """ Marker interface for MF Publication
    """

    publication_categories = schema.Set (
        title=_(u'label_publication_categories', default=u'Categories'),
        description=_(u'label_publication_categories_description', default=u'Publication categories'),
        value_type=schema.Choice(
            title = _("label_publication_categories", default=u"Categories"),
            vocabulary = 'collective.taxonomy.mf_publication_categories',
            required = True
        )
    )

    relatedAuthors = RelationList(
        title=_(u'label_publication_related_authors', default=u'Authors'),
        default=[],
        value_type=RelationChoice(
            title=u'Authors',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    directives.widget(
        'relatedAuthors',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['mf_person', 'MF Person']
            }
        )

@implementer(IMFPublication)
class MFPublication(Item):
    """
    """
