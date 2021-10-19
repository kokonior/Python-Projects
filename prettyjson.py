# https://github.com/andy-gh/prettyjson/blob/master/prettyjson.py

def prettyjson(obj, indent=2, maxlinelength=80):
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(obj, itemkey="", islast=True,maxlinelength=maxlinelength - indent, indent=indent)
    return indentitems(items, indent, level=0)

def basictype2str(obj):
    if isinstance(obj, str):
        return "\"" + str(obj) + "\""
    elif isinstance(obj, bool):
        return {True: "true", False: "false"}[obj]
    else:
        return str(obj)
