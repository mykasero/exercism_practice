class Garden:
    def __init__(self, diagram, **args):
        self.plants1 = {"V" : "Violets", "R" : "Radishes", "G" : "Grass", "C" : "Clover"}
        self.students = []
        self.diagram = diagram
        self.plants_string = ""
        self.plant_list = []

        if args:
            self.students = sorted(args['students'])
        else:
            self.students = ["Alice", "Bob", "Charlie", "David",
                            "Eve", "Fred", "Ginny", "Harriet",
                            "Ileana", "Joseph", "Kincaid", "Larry"]

        self.diagram = self.diagram.split("\n")
        print(self.diagram)

    def plants(self, name):
        person_index = self.students.index(name)
        self.plants_string = self.diagram[0][person_index*2:(person_index*2)+2] + self.diagram[1][person_index*2:(person_index*2)+2]

        for plant in self.plants_string:
            self.plant_list.append(self.plants1[plant])

        return self.plant_list

'''
Instructions
Given a diagram, determine which plants each child in the kindergarten class is responsible for.

The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.

They've chosen to grow grass, clover, radishes, and violets.

To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.

[window][window][window]
........................ # each dot represents a cup
........................
There are 12 children in the class:

Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.

The following diagram represents Alice's plants:

[window][window][window]
VR......................
RG......................
In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.

Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, it should be able to determine which plants belong to each student.

For example, if it's told that the garden looks like so:

[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
Then if asked for Alice's plants, it should provide:

Violets, radishes, violets, radishes

While asking for Bob's plants would yield:

Clover, grass, clover, clover


Python Implementation
The tests for this exercise expect your program to be implemented as a Garden class in Python.
Your class should implement a method called plants, which takes a student's name as an argument and returns the list of plant names belonging to that student.

Constructors
Creating the example garden

[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV

would, in the tests, be represented as Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV").

Default Parameters
In some tests, a list of students is passed as an argument to __init__(). This should override the twelve student roster provided in the problem statement. Both of these statements need to work with your __init__() method:

# Make a garden based on the default 12-student roster.
Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV") 

# Make a garden based on a 2-student roster.
Garden("VRCC\nVCGG", students=["Valorie", "Raven"]) 
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/kindergarten-garden/canonical-data.json
