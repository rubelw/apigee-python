from .apis import Apis
from .roles import Roles


class Apigee(object):
    """Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token
    """

    def __init__(self, org_name, username, password):
        self.apis = Apis(org_name, username, password)
        self.roles = Roles(org_name, username, password)
