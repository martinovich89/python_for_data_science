def all_thing_is_obj(object: any) -> int:
    known_types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    type_name = known_types.get(type(object), "Type not found")
    output = ""

    if (type_name == "String"):
        output += ("%s is in the kitchen" % object)
    else:
        output += (type_name)

    if (type_name != "Type not found"):
        output += " : %s" % type(object)

    print(output)

    return (42)
