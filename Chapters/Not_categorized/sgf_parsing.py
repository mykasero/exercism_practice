# STATUS = 16/23 passed

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if input_string == "":
        raise ValueError("tree missing")
    elif input_string == "()":
        raise ValueError("tree with no nodes")
    elif "(" not in input_string:
        raise ValueError("tree missing")
    elif len(input_string) == 3 and input_string[1] == ";":
        return SgfTree()

    else:
        #first step splitting properties and children

        properties = []
        children = []
        tmp_prop = ""
        tmp_child = ""

        is_property_key = True
        child_flag = False
        for i in range(2,len(input_string)):
            if input_string[i] == ";":
                child_flag = True
            elif input_string[i] == ")" and child_flag == True:
                children.append(tmp_child)
                child_flag = False
                tmp_child = ""
            elif input_string[i] == "[":
                is_property_key = False
            elif input_string[i].islower() and is_property_key == True:
                raise ValueError("property must be in uppercase")
            elif is_property_key == True and i == len(input_string)-1:
                raise ValueError("properties without delimiter")


            if child_flag == True and input_string[i] != ";":
                tmp_child += input_string[i]
            else:
                if input_string[i] not in [";",")"]:
                    tmp_prop += input_string[i]

            if child_flag == False and input_string[i] == ")":
                properties.append(tmp_prop)
                tmp_prop = ""
            elif child_flag == True and input_string[i] == ")":
                children.append(tmp_child)
                tmp_child = ""

        properties = properties[0]
        prop_dict = dict()
        keys = []
        vals = []
        tmp_val = ""
        is_property_key = True
        for i in range(len(properties)):
            if properties[i] == "[":
                is_property_key = False
                continue
            elif properties[i] == "]" and is_property_key == False:
                is_property_key = True
                continue

            if is_property_key == True and properties[i] != "]":
                if tmp_val != "":
                    vals.append(tmp_val)
                tmp_val = ""
                keys.append(properties[i])
            else:
                tmp_val += properties[i]
        if tmp_val != "":
            vals.append(tmp_val)

        for key,value in zip(keys,vals):
            prop_dict[key] = [value]

        props = str_to_dict(properties)

        sgf_childs = []
        for item in children:
            sgf_childs.append(SgfTree(str_to_dict(item)))

        stop = "stop"


        #returning properties and children returning works correctly, now special items

        return SgfTree(props, sgf_childs)

def str_to_dict(item):
    #find a better way to deal with backslash pairs and other special items like ( ] etc
    prop_dict = dict()
    keys = []
    vals = []
    tmp_val = ""
    is_property_key = True
    for i in range(len(item)):
        if item[i] == "[":
            is_property_key = False

        elif item[i] == "]" and is_property_key == False:
            is_property_key = True


        if is_property_key == True and item[i] != "]":
            keys.append(item[i])

        else:
            tmp_val += item[i]
            if item[i] == "]":
                if "\t" in tmp_val:
                    tmp_val = tmp_val.replace("\t", " ")
                if "\\" in tmp_val:
                    tmp_val = tmp_val.replace("\\","")

                vals.append(tmp_val)
                tmp_val = ""
    if tmp_val != "":
        vals.append(tmp_val)

    for key, value in zip(keys, vals):
        if len(vals) > 1 and len(keys) != len(vals):
            prop_dict[key] = [item[1:-1] for item in vals]
        else:
            prop_dict[key] = [value[1:-1]]



    return prop_dict
