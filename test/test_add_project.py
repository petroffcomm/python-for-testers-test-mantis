import pytest

from datagen.project import testdata
from utils.data_transformations import produce_instance_for_groups_page_view


@pytest.mark.parametrize("new_project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, new_project):
    old_projects = app.projects.get_projects_list()
    app.projects.create(new_project)
    new_projects = app.projects.get_projects_list()

    old_projects.append(produce_instance_for_groups_page_view(new_project))

    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
