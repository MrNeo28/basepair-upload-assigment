from assertpy import assert_that
from page_object.base_page import BasePage
from page_object.locators import LoginPageLocators, DashboardPageLocators


class Upload(BasePage):
    def login(self, username: str, password: str):
        self.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def create_project(self, project_name: str):
        self.find_element(*DashboardPageLocators.CREATE_NEW_PROJECT).click()
        self.find_element(*DashboardPageLocators.INPUT_PROJECT_NAME).send_keys(
            project_name
        )
        self.find_element(*DashboardPageLocators.CREATE_BUTTON).click()

    def upload_sample(self):
        self.find_element(*DashboardPageLocators.UPLOAD_BUTTON).click()

    def upload_sample_file(self, sample_path: str):
        # use javascript to make the input element visible
        script = """
        var element = document.querySelector('span.ant-upload > input:nth-child(1)');
        if (element) {
            element.style.display = 'block';
        }
        """
        self.driver.execute_script(script)
        self.find_element(*DashboardPageLocators.UPLOAD_INPUT).send_keys(sample_path)

    def click_upload_data_button(self):
        self.find_element(*DashboardPageLocators.UPLOAD_SAMPLE_BUTTON).click()

    def get_upload_message(self):
        assert_that(
            self.find_element(*DashboardPageLocators.SUCCESSFUL_UPLOAD).is_displayed()
        ).is_true()

    def is_dashboard_title_displayed(self):
        assert_that(
            self.find_element(*DashboardPageLocators.DASHBOARD_TITLE).is_displayed()
        ).is_true()

    def is_upload_button_displayed(self):
        assert_that(
            self.is_element_displayed(*DashboardPageLocators.UPLOAD_BUTTON)
        ).is_true()
