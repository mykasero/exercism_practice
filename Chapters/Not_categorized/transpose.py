def transpose(lines):
    new_lines = []
    transposed_word = ""
    transposed_list = []

    if len(lines) < 1:
        return ""
    else:
        lines = lines.splitlines()
        longest_str = len(max(lines, key=len))

        for line in lines:
            if len(line) < longest_str:
                line += (longest_str - len(line)) * "_"

            new_lines.append(line)

        for i in range(longest_str):
            for item in new_lines:
                transposed_word += item[i]

            if i == len(lines[len(lines) - 1]) - 1:
                lines.pop(len(lines) - 1)
                new_lines.pop(len(lines))

            if len(transposed_word) == 2 and transposed_word[1] == "_":

                transposed_list.append(transposed_word.replace("_", ""))

            else:

                transposed_list.append(transposed_word.replace("_", " "))

            transposed_word = ""

        final2 = "\n".join(transposed_list).rstrip()

        return final2