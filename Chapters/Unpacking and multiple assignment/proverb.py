def proverb(*input_data,qualifier):
    final = []
    line = ""

    if len(input_data) == 0:
        return final
    elif len(input_data) == 1:
        if qualifier:
            final.append("And all for the want of a " + qualifier + " " + input_data[0] + ".")
        else:
            final.append("And all for the want of a " + input_data[0] + ".")

    else:

        if qualifier:
            for item in range(len(input_data)-1):
                line = "For want of a " + input_data[item] + " the " + input_data[item+1] + " was lost."
                final.append(line)
            final.append("And all for the want of a " + qualifier + " " + input_data[0] + ".")
        else:
            for item in range(len(input_data)-1):
                line = "For want of a " + input_data[item] + " the " + input_data[item+1] + " was lost."
                final.append(line)
            final.append("And all for the want of a " + input_data[0] + ".")


    return final

'''
Instructions
For want of a horseshoe nail, a kingdom was lost, or so the saying goes.

Given a list of inputs, generate the relevant proverb. For example, given the list ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"], you will output the full text of this proverbial rhyme:

For want of a nail the shoe was lost.
For want of a shoe the horse was lost.
For want of a horse the rider was lost.
For want of a rider the message was lost.
For want of a message the battle was lost.
For want of a battle the kingdom was lost.
And all for the want of a nail.

How this exercise is implemented for Python
The test cases for this track add an additional keyword argument called qualifier. You should use this keyword arguments value to modify the final verse of your Proverb.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/proverb/canonical-data.json
