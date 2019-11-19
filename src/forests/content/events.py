# -*- coding: utf-8 -*-
from zope.event import notify

from forests.content.contenttypes import IRichImage
from plone.app.iterate.dexterity.utils import get_baseline
from plone.app.iterate.event import WorkingCopyDeletedEvent


def handle_iterate_wc_deletion(object, event):
    """ When a WorkingCopy is deleted, the problem was that the locking was not
    removed. We're manually triggering the IWorkingCopyDeletedEvent because
    the plone.app.iterate handler is registered for IWorkingCopyRelation, a
    derivate of Archetype's relations, which is not used in the dexterity
    implementation.
    """
    try:
        baseline = get_baseline(object)
    except:
        return
    notify(WorkingCopyDeletedEvent(object, baseline, relation=None))


def set_title_description(obj, event):
    ''' Sets title to filename if no title
        was provided.
        Also sets an empty unicode as description if
        no description was provided.
    '''
    title = obj.title

    if not title:
        if IRichImage.providedBy(obj):
            datafield = obj.image
        else:
            datafield = obj.file

        if datafield:
            filename = datafield.filename
            obj.title = filename

    description = obj.description

    if not description:
        obj.description = u''
