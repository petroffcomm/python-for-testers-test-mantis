
from suds.client import Client
from suds import WebFault


class MantisSoapApiHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        soap_client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")

        try:
            soap_client.service.mc_login(username, password)
            return True
        except WebFault:
            return False
