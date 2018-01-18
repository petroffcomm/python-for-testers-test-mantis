# -*- coding: utf-8 -*-
import json
import os.path

import pytest

from fixture.application import Application

fixture = None
target = None


# test.fixture(scope="session")
@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")

    web_config = load_config(request.config.getoption("--target"))['web']
    webadmin = load_config(request.config.getoption("--target"))['webadmin']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=webadmin['user'], password=webadmin['password'])

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config:
            target = json.load(config)
    return target


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
