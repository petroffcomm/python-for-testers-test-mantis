
import re
from model.project import Project


def set_none_or_value_of(val):
    if val == "":
        return None
    else:
        return val

def produce_instance_for_groups_page_view(prj):
    # 1. We need to use 'set_none_or_value_of()' because some
    # objects in list we need to compare to current one
    # could be created with 'None'-value (but not empty string)
    # in the 'name'-field
    #
    # 2. We need to substitute multiple 'space'-chars to 1
    # because this is what application does for projects' name and description
    # 3. Web-browser trims edge 'space'-chars so we need to
    # take this into account.
    # 4. We use negative lookbehinds not to trim space-chars
    # at the beginning of strings
    # http://www.rexegg.com/regex-disambiguation.html#lookahead
    return Project(name=re.sub('(?!^)\s+', ' ', prj.name).rstrip(),
                   description=set_none_or_value_of(re.sub('(?!^)\s+', ' ', prj.description).rstrip()))


# print(produce_instance_for_groups_page_view(Project("  project name:  5H   ",
#                                                     "  Z*  Ag @s9JPG -n~WuLx p.rtCqu9&)#q~z*.Un zmR)h&t*[!R!Uu v;,@oc}x5wSIoZX' _ Oe18]vs*}me*e&%^|s! K1")))