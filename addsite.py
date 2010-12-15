
import sys

def addsite(app, admin, site):
    print app, admin, site

def adduser(site, user, pw):
    print site, user, pw

if __name__ == '__main__':
    argv = sys.argv
    admin , site , user , pw = argv[1:5]
    addsite(app, admin, site)
    adduser(site, user, pw)
