# Pytest test suite


## Project structure

```
├── README.md
├── bin # contains chromedriver and geckodriver
├── config # contains config.ini/.evn files for environment variables
├── conftest.py # contains pytest fixtures
├── features
│   └── sample_upload.feature
├── page_object
│   ├── __init__.py
│   ├── base_page.py # contains base page class
│   ├── locators.py # contains locators for the page
│   └── upload.py # contains page object class
├── pytest.ini
├── step_definitions
│   ├── __init__.py
│   ├── steps_common.py # contains common steps
│   ├── steps_given.py # contains given steps
│   ├── steps_then.py # contains then steps
│   ├── steps_when.py # contains when steps
│   └── test_upload.py # contains test cases
├── test_data
│   └── sample_text.txt # contains sample text file
└── utils
    ├── env_variables.py
    └── logger.py # contains logger class
```


## How to run the tests

Install the requirements
```bash
pip install -r requirements.txt
```

Run for chrome browser
```bash
pytest --driver Chrome
```

Run for firefox browser
```bash
pytest --driver Firefox
```

