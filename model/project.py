
class Project:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def __repr__(self):
        return "Name:%s|Descr:%s" % (self.name, self.description)
