# def test_lists():
#     # if [1, 2, 3] == [1, 2, 3]:
#     #   raise AssertionError("Not equeal")
#     # same as below code
#     print('Hi Roman Mud')
#     assert [1, 2, 3] == [1, 2, 3]


import requests


def test_http_status_code200():
    r = requests.get('https://api.github.com')
    print(r)
    assert r.status_code == 200


test_http_status_code200()