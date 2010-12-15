from Products.CMFPlone.factory import addPloneSite
from sys import argv
from transaction import commit


def _setup_app(app, admin):
    from AccessControl.SecurityManagement import newSecurityManager
    from Testing.makerequest import makerequest
    admin = app.acl_users.getUser(admin)
    admin = admin.__of__(app.acl_users)  # Add admin to acl_users' aq_chain
    newSecurityManager(None, admin)
    app = makerequest(app)
    return app


def addsite(app, admin, site):
    app = _setup_app(app, admin)
    extension_ids = ('plonetheme.classic:default',
        'plonetheme.sunburst:default')
    addPloneSite(app, site, extension_ids=extension_ids)


def adduser(app, site, user, pw):
    app[site].portal_membership.addMember(user, pw, [], [])

if __name__ == '__main__':
    app = locals()['app']  # make pyflakes happy
    if len(argv) != 5:
        print ("Usage: bin/plone run addsite.py <zope_admin> <plone_site>"
            " <user> <password>")
    else:
        admin, site, user, pw = argv[1:5]
        addsite(app, admin, site)
        adduser(app, site, user, pw)
        commit()
