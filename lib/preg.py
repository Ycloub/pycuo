import re
def preg_match_One(match,content):
    reGroup = re.search(match,content)
    if hasattr(reGroup,'groups'):
        return reGroup.groups()[0]
    else:
        return None