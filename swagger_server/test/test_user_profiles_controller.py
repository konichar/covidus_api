# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assessment import Assessment  # noqa: E501
from swagger_server.models.profile_item import ProfileItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserProfilesController(BaseTestCase):
    """UserProfilesController integration test stubs"""

    def test_create_user_profile(self):
        """Test case for create_user_profile

        Create a new user profile
        """
        body = ProfileItem()
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profile',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_profile(self):
        """Test case for delete_user_profile

        Delete User by id
        """
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profile/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_profile_id_get(self):
        """Test case for profile_id_get

        Returns a User by it's id
        """
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profile/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_assessment_by_id(self):
        """Test case for read_assessment_by_id

        Return list of assessment of a particular user
        """
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profile/{id}/assessment'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_user_profile(self):
        """Test case for search_user_profile

        Returns a list of all user profiles
        """
        query_string = [('search_term', 'search_term_example')]
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profiles',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update User by id
        """
        body = ProfileItem()
        response = self.client.open(
            '/konichar/covidus_api_v1/1.0.0/profile/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
