

class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My View").click()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get(self.app.base_url + "/manage_proj_page.php")
