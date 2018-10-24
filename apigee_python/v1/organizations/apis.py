import base64
from .rest import RestClient


class Apis(object):

    """Apigee api endpoints

    Args:
        username

        password

    """

    def __init__(self, org_name, username, password):
        self.org_name = org_name
        self.username = username
        self.password = password

        userPass = str(username) + ':' + str(password)
        userPass = userPass.encode("utf-8")
        base64string = base64.b64encode(userPass).decode("utf-8")
        self.authentication = base64string


        self.url = 'https://api.enterprise.apigee.com/v1/organizations/%s/apis' % org_name
        self.client = RestClient(token=self.authentication)

    def get(self):
        """Retrieves the jti and aud of all tokens in the blacklist.

        Args:
            aud (str, optional): The JWT's aud claim. The client_id of the
                application for which it was issued.
        """

        headers = {'Authorization': "Basic "+str(self.authentication)}

        return self.client.get(self.url)

