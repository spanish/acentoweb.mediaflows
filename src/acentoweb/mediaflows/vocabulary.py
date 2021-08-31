from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.dutchestheme')

def format_title(folder):
    return "{}  ...   [ {} ]".format( folder.Title, folder.getURL())



def PersonVocabulary(context):

    persons = api.content.find(portal_type=['Person', 'person'], sort_on='sortable_title')

    if persons:
        terms = [ SimpleTerm(value=person.UID, token=person.UID, title=person.Title) for person in persons ]
    return SimpleVocabulary(terms)

directlyProvides(PersonVocabulary, IVocabularyFactory)
