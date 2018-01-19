import pytest

from datagen.project import testdata


@pytest.mark.parametrize("new_project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, new_project):
    old_projects = app.mantis_soap_api.get_projects_list()
    app.projects.create(new_project)
    new_projects = app.mantis_soap_api.get_projects_list()

    old_projects.append(new_project)

    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
