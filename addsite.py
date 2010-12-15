
from sys import argv
from Products.CMFPlone.factory import addPloneSite

def _setup_app(app, admin):
    from AccessControl.SecurityManagement import newSecurityManager
    from Testing.makerequest import makerequest
    admin = app.acl_users.getUser(admin)
    admin = admin.__of__(app.acl_users)
    newSecurityManager(None, admin)
    app = makerequest(app)
    return app

def addsite(app, admin, site):
    app = _setup_app(app, admin)
    addPloneSite(app, site)

def adduser(site, user, pw):
    print site, user, pw

if __name__ == '__main__':
    admin, site, user, pw = argv[1:5]
    addsite(app, admin, site)
    adduser(site, user, pw)
