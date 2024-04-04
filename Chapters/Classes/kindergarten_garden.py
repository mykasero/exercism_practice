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


garden = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
garden.plants("Patricia")