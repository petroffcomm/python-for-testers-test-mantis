
from model.project import Project

from datagen.utils import random_string, rnd_name_string

# default values
projects_qty = 10

# this part of code is not executed while importing this module -
# only while running itself
if __name__ == "__main__":
    pass


testdata = [
    Project(name=rnd_name_string("project name:", 10), description=random_string("", 200))
    for i in range(projects_qty)
]
