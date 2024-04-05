class Allergies:
    def __init__(self, score):
        self.items = {
                "eggs": 1,
                "peanuts": 2,
                "shellfish": 4,
                "strawberries": 8,
                "tomatoes": 16,
                "chocolate": 32,
                "pollen": 64,
                "cats": 128
                }
        self.allergies = []

        for key,value in self.items.items():
            if score & value == value:
                self.allergies.append(key)


    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):

        return self.allergies
