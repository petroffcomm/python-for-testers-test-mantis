
from suds.client import Client
from suds import WebFault

from model.project import Project


class MantisSoapApiHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")

        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        mantis_creds = self.app.config['webadmin']
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")

        try:
            projects = client.service.mc_projects_get_user_accessible(mantis_creds['user'], mantis_creds['password'])
        except WebFault:
            return ["An error occurred", WebFault.__repr__()]

        return list(map(lambda prj: Project(name=prj['name'], description=prj['description']), projects))
