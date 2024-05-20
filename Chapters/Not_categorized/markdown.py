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
        for i in range(len(splitted)):
            if len(splitted[i]) > 1:
                if re.match(".*\*.*", splitted[i]):
                    if not re.search("<ul>",final):
                        _strip += "<ul>"

                    if re.search("__",splitted[i]):
                        _strip += "<li><strong>" + splitted[i].replace("__", "").replace("*","").strip() + "</strong></li>"

                    elif re.search("_",splitted[i]):
                        if splitted[i].index("*") == 0 and splitted[i].count("*") == 1:
                            _strip += "<li><em>" + splitted[i].replace("_", "").replace("*","").strip() + "</em></li>"
                        else:
                            _strip += "<li><em>" + splitted[i][1:].replace("_", "").replace("*","").strip() + "</em></li>"

                    else:
                        if splitted[i].index("*") == 0 and splitted[i].count("*") == 1:
                            _strip += "<li>" + splitted[i].replace("*", "").strip() + "</li>"
                        else:
                            _strip += "<li>" + splitted[i][1:].strip() + "</li>"

                elif re.match("#",splitted[i]):
                    _strip += "<h1>" + splitted[i].replace("#","").strip() + "</h1>"

                elif re.match("__",splitted[i]):
                    _strip += "<strong>" + splitted[i].replace("__", "").strip() + "</strong>"

                elif re.match("_",splitted[i]):
                    _strip += "<em>" + splitted[i].replace("_","").strip() + "</em> "

                else:
                    if i == 0 and not re.match(".*\*.*",splitted[i]) and not re.match("#",splitted[i]):
                        _strip += "<p>" + splitted[i] + " "

                    elif re.search("<ul>",final) and not re.match(".*\*.*",splitted[i]) and not re.match("#",splitted[i]):
                        _strip += "</ul><p>" + splitted[i].strip() + "</p>"

                    else:
                        _strip += splitted[i] + " "
            else:
                if i > 0:
                    _strip += splitted[i] + " "

                if i == 0 and len(splitted[i]) == 1:
                    _strip += "<h1>"

            final += _strip
            _strip = ""

        if re.search("<ul>",final) and not re.search("</ul>",final):
            final += "</ul>"
        if re.search("<h1>",final) and not re.search("</h1>",final):
            final = final.rstrip()
            final += "</h1>"
        if re.search("<p>",final) and not re.search("</p>",final):
            final = final.rstrip()
            final += "</p>"
        if not re.search("<h1>",final) and not re.search("<ul>",final) and not re.search("<p>",final):
            final = "<p>" + final.rstrip() + "</p>"

    return final
