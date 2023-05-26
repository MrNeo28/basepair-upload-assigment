import time

from pytest_bdd import when, parsers
from page_object.upload import Upload


@when(parsers.re('I pause for "(?P<seconds>.*)" seconds'), converters=dict(seconds=int))
def pause(selenium, seconds):
    time.sleep(seconds)


@when("I click on 'Upload Data' button")
def click_upload_data_btn(selenium):
    Upload(selenium).upload_sample()


@when("I click on 'Choose File' button")
def click_upload_sample_btn(selenium):
    Upload(selenium).upload_sample_file(
        "/Users/ashishvishwakarma/Desktop/python-ppt/basepair/test_data/sample_text.txt"
    )


@when("I click on 'Upload' button")
def click_upload_btn(selenium):
    Upload(selenium).click_upload_data_button()
