import random

from model.project import Project


def test_del_project(app):
    old_projects = app.projects.get_projects_list()

    if len(old_projects) == 0:
        app.projects.create(Project(name="test project"))
        old_projects = app.projects.get_projects_list()

    project = random.choice(old_projects)
    app.projects.delete(project)

    new_projects = app.projects.get_projects_list()
    old_projects.remove(project)

    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
