import re


def parse(markdown):
    final = ""
    strips = []
    case_ctr = 0
    _strip = ""

    if re.search("\n",markdown):
        splitted = markdown.split("\n")
    else:
        splitted = markdown.split(" ")

    for item in splitted:
        if re.match(".*\*.*",item) or re.match("_",item) or re.match("#",item):
            case_ctr += 1


    if case_ctr == 1:

        if re.match(".*\*.*",splitted[0]):
            final = "<ul>"
            for item in splitted:
                final += "<li>" + item.replace("*","").strip() + "</li>"

            final += "</ul>"


        elif re.match("#######", splitted[0]):
            final = "<p>" + markdown + "</p>"

        elif re.match("######", splitted[0]):
            final = "<h6>" + markdown.replace("######", "").strip() + "</h6>"

        elif re.match("#####", splitted[0]):
            final = "<h5>" + markdown.replace("#####", "").strip() + "</h5>"

        elif re.match("####", splitted[0]):
            final = "<h4>" + markdown.replace("####", "").strip() + "</h4>"

        elif re.match("###",splitted[0]):
            final = "<h3>" + markdown.replace("###", "").strip() + "</h3>"

        elif re.match("##",splitted[0]):
            final = "<h2>" + markdown.replace("##", "").strip() + "</h2>"

        elif re.match("#",splitted[0]):
            final = "<h1>" + markdown.replace("#","").strip() + "</h1>"

        elif re.match("__",splitted[0]):
            final = "<p><strong>" + markdown.replace("__", "").strip() + "</strong></p>"

        elif re.match("_",splitted[0]):
            final = "<p><em>" + markdown.replace("_","").strip() +"</em></p>"

        else:
            final = "<p>" + markdown + "</p>"

    else:
        for item in splitted:
            if re.match(".*\*.*", item):
                _strip += "<ul>"
                _strip += "<li>" + item.replace("*", "").strip() + "</li>"

                final += "</ul>"

    stop = "STOP"

    return final
