import unittest
import mock
from apigee_python.v1.organizations import Roles


class TestApis(unittest.TestCase):

    @mock.patch('apigee_python.v1.organizations.roles.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Roles(org_name='name', username='xx', password='xx')
        t.get()

        mock_instance.get.assert_called_with(
            'https://api.enterprise.apigee.com/v1/organizations/name/userroles'
        )

