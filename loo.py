from AccessControl.Permissions import manage_users
from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PluggableAuthService import registerMultiPlugin
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin


# This is probably insane, but it fools five:registerPackage into thinking that this single module is a package.
__path__ = '.'


class LoginOnlyOncePlugin(BasePlugin):
    meta_type = 'Login Only Once Plugin'
    security = ClassSecurityInfo()

    def __init__(self, id, title=None):
        self._setId(id)
        self.title = title



def manage_addpackage(dispatcher, id, title=None, REQUEST=None):
    """
    Boo yah! You need this doc string or Zope 2's publisher will drop this method 
    faster than you can say: "Page not found". During this time you will also be wondering what is going on
    until you finally get around to deleting the ignored exceptions in /Plone/error_log.
    """
    plugin = LoginOnlyOncePlugin(id, title)
    dispatcher._setObject(plugin.getId(), plugin)
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect('%s/manage_workspace'
                                     '?manage_tabs_message='
                                     'packageHelper+added.'
                                      % dispatcher.absolute_url())


registerMultiPlugin(LoginOnlyOncePlugin.meta_type)


def initialize(context):
    manage_addform = PageTemplateFile('add_plugin', globals(), __name__='manage_addform')
    context.registerClass(LoginOnlyOncePlugin, permission=manage_users, constructors=(manage_addform,manage_addpackage), visibility=None)
