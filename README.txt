Introduction
============

Another "mock up" (experimental) PAS plugin

Goal
----

To enforce only one simultaneous login per user in Plone, the Right Way(tm).
This is just an experiment. The results will likely go into
Products.NoDuplicateLogin (which is the closest pre-existing add-on I could
find, but does not yet work in Plone 4).

Notes
~~~~~

Via Laurence Rowe on plone-developers.

http://sourceforge.net/mailarchive/message.php?msg_id=26576028::

    You'll need a PAS plugin either way. Whether that uses the Zope2
    session machinery or something else is then up to you. Zope's sessions
    are notoriously  prone to conflict errors though.

    PAS is supplied with a SessionAuthHelper plugin, but this would quite
    happily give a separate session to each browser the user is logged in
    on. Perhaps that could be solved with a custom browser_id_manager or
    using something else to store per user sessions.

http://sourceforge.net/mailarchive/message.php?msg_id=26577841::

    It would be better to store this in the normal Zope session storage in
    the temp_folder though rather than in the main ZODB, otherwise sites
    with lots of logged in users would see a great deal of database bloat.

    I think the easiest way to do this would be to modify the
    browser_id_manager to return the userid for logged in users - it would
    be possible to get this from the plone.session cookie. Sessions would
    then be per user rather than per browser.

    You would still need a per browser random id cookie. A PAS plugin
    could then check this cookieagainst the user's browser id stored at
    login time.

http://sourceforge.net/mailarchive/message.php?msg_id=26697074::

    plone.session is confusingly named. It has no relation to zope 2 sessions,
    which offer per session storage, it only identifies a user. While zope 2
    sessions have problems with conflict errors, this is only because they use
    the zodb with full transactional integrity (which comes at a cost). The
    various single login plugins you've shown me all reimplement in zodb
    sessions naively and will show more problems than zope 2 sessions. You
    should be able to use the current browser id manager to give you a per
    browser id. (you just want to have zope 2 session storage per user not per
    browser.)
