import unittest
import mock
from apigee_python.v1.organizations import ResourceFiles


class TestResourceFiles(unittest.TestCase):

    @mock.patch('apigee_python.v1.organizations.resourcefiles.RestClient')
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = ResourceFiles(org_name='name', username='xx', password='xx', environment='prod')
        t.get()

        mock_instance.get.assert_called_with(
            'https://api.enterprise.apigee.com/v1/organizations/name/prod/resourcefiles'
        )

