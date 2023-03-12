import requests


# def test_lists():
#     # if [1, 2, 3] == [1, 2, 3]:
#     #   raise AssertionError("Not equeal")
#     # same as below code
#     print('Hi Roman Mud')
#     assert [1, 2, 3] == [1, 2, 3]


# def test_http_status_code200():
    # r = requests.get('https://api.github.com')
    # print(r.__dict__)
    # assert r.status_code == 200
    # assert r.text != 'Design for failure'
    # assert r.json()['login'] != 'romanmud'
    # assert r.json()['id'] == 443150

# def test_user_not_exists():
#         r = requests.get('https://api.github.com/users/romanmud')
#         # print(r.__dict__)
#         assert r.status_code != 200
#         # assert r.text == 200
#         assert r.json()['login'] != 'romanmud'
#         # assert r.json()['id'] == 443150

