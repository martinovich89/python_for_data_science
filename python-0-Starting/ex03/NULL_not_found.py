import math


def NULL_not_found(object: any) -> int:
    known_types = {
        None: "Nothing",
        math.nan: "Cheese",
        '0': "Zero",
        '': "Empty",
        False: "Fake"
    }

    type_name = known_types.get(object, "Type not Found")
    output = ""
    ret = 0

    if (object == 0 and type(object) is int):
        type_name = "Zero"
    elif (type(object) is float):
        type_name = "Cheese"
    output += type_name

    if (type_name != "Type not Found"):
        output += ": %s %s" % (object, type(object))
    else:
        ret = 1

    if (type_name == "Empty"):
        output = output.replace(" ", "", 1)
    print(output)

    return (ret)
