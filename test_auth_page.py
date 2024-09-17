from pages.auth_page import AuthPage
import time



def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email('email@gmail.com')
    page.enter_pass('555555pass')
    page.btn_click()

    assert page.get_relative_link() != '/all_pets', 'login error'

    time.sleep(4)
