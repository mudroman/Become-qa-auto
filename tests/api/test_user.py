import requests
import pytest

def test_user_exists(github_api_client):
    user = github_api_client.get_user('defunkt')
    assert user['login'] == 'defunkt'
    assert user['id'] == 2


# def test_user_non_exists(github_api_client):
#     with pytest.raises(requests.exceptions.HTTPError):
#         # assert user.status_code == 400
#         github_api_client.get_user('asdasdsadsad')
#     # assert user.