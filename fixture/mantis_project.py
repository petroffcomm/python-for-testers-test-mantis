from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def set_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_field_value(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

    def produce_project_instance_from_maintable_row(self, project_row):
        cells = project_row.find_elements_by_tag_name("td")
        name = cells[0].find_element_by_tag_name("a").text
        description = cells[4].text
        return Project(name, description)

    def get_projects_list(self):
        wd = self.app.wd
        self.app.navigation.open_projects_page()

        projects = []
        for project_row in wd.find_elements_by_xpath("//table[@class='width100'][2]//tr[position()>2]"):
            project = self.produce_project_instance_from_maintable_row(project_row)

            projects.append(project)

        return list(projects)

    def create(self, project):
        create_project_btn_xpath = ".//input[@type='submit'][@value='Create New Project']"
        wd = self.app.wd

        self.app.navigation.open_projects_page()

        wd.find_element_by_xpath(create_project_btn_xpath).click()
        self.set_field_value("name", project.name)
        self.set_field_value("description", project.description)
        wd.find_element_by_xpath(".//input[@type='submit'][@value='Add Project']").click()

        # wait for proceeding after project created
        WebDriverWait(wd, 10).until(
            presence_of_element_located((By.XPATH, create_project_btn_xpath))
        )

    def delete(self, project):
        wd = self.app.wd

        self.app.navigation.open_projects_page()
        wd.find_element_by_link_text(project.name).click()

        # wait until project edit page gets opened
        WebDriverWait(wd, 10).until(
            presence_of_element_located((By.XPATH, ".//input[@type='submit'][@value='Delete Project']"))
        )

        # init deletion on the project's edit page
        wd.find_element_by_xpath(".//input[@type='submit'][@value='Delete Project']").click()

        # and submit project deletion on the confirmation page
        # (locators are the same in both cases)
        wd.find_element_by_xpath(".//input[@type='submit'][@value='Delete Project']").click()
