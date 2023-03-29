import unittest

from unittest.mock import patch, MagicMock

import api

# print(get_len())
class TestApi(unittest.TestCase):
    # mock function
    @patch("api.user_list")
    def test_api_response(self, mock_user_list):
        mock_user_list.return_value = {"m":"moun"}
        # print(user_list().json())
        print(api.get_len())
        assert api.get_len() == {"m":"moun"}

    # mock get request
    @patch("api.requests")
    def test_user_directly(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"m":"moun"}
        mock_request.get.return_value = mock_response

        response = api.user_list()
        assert response.json() == {"m":"moun"}
        assert response.status_code == 200

    # mock get request
    @patch("api.requests")
    def test_user_unavailability(self, mock_request):
        mock_response = MagicMock(status_code=404)
        mock_response.json.return_value = {"m":"moun"}
        mock_request.get.return_value = mock_response

        response = api.user_list()
        assert response == {"data":"failed to get user details."}