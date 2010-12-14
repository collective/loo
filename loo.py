from App.class_init import default__class_init__ as InitializeClass
from AccessControl.Permissions import manage_users
from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PluggableAuthService import registerMultiPlugin
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements
from Products.PluggableAuthService.interfaces.plugins import \
    IAnonymousUserFactoryPlugin, IAuthenticationPlugin, \
    IChallengePlugin, IChallengeProtocolChooser, ICredentialsResetPlugin, \
    ICredentialsUpdatePlugin, IExtractionPlugin, IGroupEnumerationPlugin, \
    IGroupsPlugin, ILoginPasswordExtractionPlugin, \
    ILoginPasswordHostExtractionPlugin, IPropertiesPlugin, \
    IRequestTypeSniffer, IRoleAssignerPlugin, \
    IRoleEnumerationPlugin, IRolesPlugin, \
    IUpdatePlugin, IUserAdderPlugin, \
    IUserEnumerationPlugin, IUserFactoryPlugin, IValidationPlugin


# This is probably insane, but it fools five:registerPackage into thinking
# that this single module is a package.
__path__ = '.'


class LoginOnlyOncePlugin(BasePlugin):
    meta_type = 'Login Only Once Plugin'
    security = ClassSecurityInfo()

    def __init__(self, id, title=None):
        self._setId(id)
        self.title = title


def create_plugin(dispatcher, id, title=None, REQUEST=None):
    """
    Boo yah! You need this doc string or Zope 2's publisher will drop this
    method faster than you can say: "This page does not seem to exist..."
    During this time you will also be wondering what is going on, until you
    finally get around to deleting the ignored exceptions in /Plone/error_log
    at which point you will realize that you need this doc string.
    """
    plugin = LoginOnlyOncePlugin(id, title)
    dispatcher._setObject(plugin.getId(), plugin)
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect('%s/manage_workspace?manage_tabs_message='
            'LoginOnlyOncePlugin+added.' % dispatcher.absolute_url())


registerMultiPlugin(LoginOnlyOncePlugin.meta_type)


def initialize(context):
    template = 'manage_addPlugin'
    pt = PageTemplateFile(template, globals(), __name__=template)
    context.registerClass(LoginOnlyOncePlugin, permission=manage_users,
        constructors=(pt, create_plugin), visibility=None, icon='loo.png')


classImplements(LoginOnlyOncePlugin, IAnonymousUserFactoryPlugin,
    IAuthenticationPlugin,
    IChallengePlugin, IChallengeProtocolChooser, ICredentialsResetPlugin,
    ICredentialsUpdatePlugin, IExtractionPlugin, IGroupEnumerationPlugin,
    IGroupsPlugin, ILoginPasswordExtractionPlugin,
    ILoginPasswordHostExtractionPlugin, IPropertiesPlugin,
    IRequestTypeSniffer, IRoleAssignerPlugin,
    IRoleEnumerationPlugin, IRolesPlugin,
    IUpdatePlugin, IUserAdderPlugin,
    IUserEnumerationPlugin, IUserFactoryPlugin, IValidationPlugin)

InitializeClass(LoginOnlyOncePlugin)
