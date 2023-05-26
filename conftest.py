import pytest
from dotenv import load_dotenv

from step_definitions.steps_given import *
from step_definitions.steps_then import *
from step_definitions.steps_when import *
from step_definitions.steps_common import *


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = "bin/chromedriver"
    return chrome_options


#
#
# @pytest.fixture
# def firefox_options(firefox_options):
#     firefox_options.binary = '/path/to/firefox-bin'
#     return firefox_options
