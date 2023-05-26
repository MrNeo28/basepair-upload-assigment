from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#Login_username")
    PASSWORD = (By.CSS_SELECTOR, "#Login_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".ant-btn-primary")


class DashboardPageLocators:
    DASHBOARD_TITLE = (By.CSS_SELECTOR, ".dashboard-content-header")
    CREATE_NEW_PROJECT = (By.CSS_SELECTOR, ".dashboard-content .ant-btn-primary")
    INPUT_PROJECT_NAME = (By.CSS_SELECTOR, 'input[placeholder="Enter project name"]')
    CREATE_BUTTON = (By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(2)")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, ".sample-floating-upload")
    UPLOAD_INPUT = (By.CSS_SELECTOR, "span.ant-upload > input:nth-child(1)")
    UPLOAD_SAMPLE_BUTTON = (By.CSS_SELECTOR, ".action-buttons > button:nth-child(1)")
    SUCCESSFUL_UPLOAD = (By.CSS_SELECTOR, ".ant-alert-message")

