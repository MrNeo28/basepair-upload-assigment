from pytest_bdd import then, parsers
from page_object.upload import Upload

import os


@then("I should see file uploaded successfully")
def upload_message(selenium):
    Upload(selenium).get_upload_message()
