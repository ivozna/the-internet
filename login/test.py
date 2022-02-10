""" Test scenario:
1. Enter username, password and click Login.
2. Assert you're logged in.
3. Log out.
4. Assert you logged out.
"""


def test_login(login_page):
    login_page.login()
    assert login_page.log_result('You logged into a secure area!')
    login_page.log_out()
    assert login_page.log_result('You logged out of the secure area!')


