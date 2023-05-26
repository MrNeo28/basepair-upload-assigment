from pytest_bdd import given, parsers
from page_object.upload import Upload

import os


@given("User is on url")
def user_is_on_url(selenium):
    Upload(selenium).go_to_url(os.getenv("URL"))


@given("I enter username and password")
def i_enter_username(selenium):
    Upload(selenium).login(os.getenv("USERNAME"), os.getenv("PASSWORD"))


@given("I click on login button")
def login_btn(selenium):
    Upload(selenium).click_login_button()


@given("I should see Dashboard page")
def dashboard_page(selenium):
    Upload(selenium).is_dashboard_title_displayed()


@given("I click on 'Upload Data' button")
def click_upload_data_btn(selenium):
    Upload(selenium).upload_sample()
