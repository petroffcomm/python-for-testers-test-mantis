
from suds.client import Client

soap_client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
projects = soap_client.service.mc_projects_get_user_accessible("administrator", "root")

print("\n".join(list(map(lambda p: p['name'], projects))))
