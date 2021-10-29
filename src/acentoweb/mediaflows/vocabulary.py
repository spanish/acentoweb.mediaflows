from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.dutchestheme')

def format_title(folder):
    return "{}  ...   [ {} ]".format( folder.Title, folder.getURL())

def PersonsVocabulary(context):

    mf_persons = api.content.find(portal_type=['MF Person', 'mf_person'], sort_on='sortable_title')

    if mf_persons:
        terms = [ SimpleTerm(value=mf_person.UID, token=mf_person.UID, title=mf_person.Title) for mf_person in mf_persons ]
    return SimpleVocabulary(terms)

directlyProvides(PersonsVocabulary, IVocabularyFactory)
