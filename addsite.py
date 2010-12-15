
import sys

def addsite(app, admin, site):
    print app, admin, site

def adduser(site, user, pw):
    print site, user, pw

if __name__ == '__main__':
    argv = sys.argv
    admin = argv[1]
    site = argv[2]
    user = argv[3]
    pw = argv[4]
    addsite(app, admin, site)
    adduser(site, user, pw)
