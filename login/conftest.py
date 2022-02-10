from pytest import fixture
from playwright.sync_api import sync_playwright
from login.login_page import LoginPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def login_page(get_playwright):
    page = LoginPage(get_playwright)
    yield page
    page.close()
