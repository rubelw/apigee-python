from .proxies import Proxies
from .roles import Roles
from .products import Products
from .resourcefiles import ResourceFiles



class Apigee(object):
    """Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token
    """

    def __init__(self, org_name, username, password):
        self.proxies = Proxies(org_name, username, password)
        self.roles = Roles(org_name, username, password)
        self.products = Products(org_name, username, password)
        self.resourcefiles = ResourceFiles(org_name, username, password, environment)


