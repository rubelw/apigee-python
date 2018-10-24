import unittest
import mock
from apigee_python.v1.organizations import Proxies


class TestApis(unittest.TestCase):

    @mock.patch('apigee_python.v1.organizations.proxies.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Proxies(org_name='name', username='xx', password='xx')
        t.get()

        mock_instance.get.assert_called_with(
            'https://api.enterprise.apigee.com/v1/organizations/name/apis'
        )

