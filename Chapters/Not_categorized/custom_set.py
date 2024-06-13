class CustomSet:
    def __init__(self, elements=[]):
        self.elements = elements

    def isempty(self):
        return True if len(self.elements) < 1 else False

    def __contains__(self, element):
        return True if element in self.elements else False

    def issubset(self, other):
        compare_list = []
        if len(other.elements) > len(self.elements):
            return True
        elif len(other.elements) < len(self.elements):
            return False
        else:
            x = sorted(self.elements)
            y = sorted(other.elements)
            for item, o_item in zip(x, y):
                if item != o_item:
                    compare_list.append(False)

            if len(compare_list) > 0:
                return False
            else:
                return True

    def isdisjoint(self, other):
        for item in self.elements:
            if item in other.elements:
                return False

        return True

    def __eq__(self, other):
        duplicates = dict()
        if not isinstance(other, CustomSet):
            return CustomSet()

        elif len(self.elements) == len(other.elements) == 0:
            return True

        else:
            for o_item in other.elements:
                duplicates.setdefault(o_item, 0)
                if o_item in self.elements:
                    duplicates[o_item] += 1

            for k, v in duplicates.items():
                if v > 1:
                    other.elements.pop(other.elements.index(1))
                    duplicates[k] -= 1

            if len(self.elements) != len(other.elements):
                return False
            else:
                x = sorted(self.elements)
                y = sorted(other.elements)

                for item, o_item in zip(x, y):
                    if item != o_item:
                        return False

                return True

    def add(self, element):
        if self.elements != []:
            if element not in self.elements:
                for i in range(len(self.elements)):
                    if element < self.elements[i]:
                        self.elements = self.elements[:i] + [element] + self.elements[i:]
        else:
            self.elements.append(element)

    def intersection(self, other):
        common = []

        if len(self.elements) > 0 and len(other.elements) > 0:
            for item in self.elements:
                if item in other.elements:
                    common.append(item)

    def __sub__(self, other):
        if len(self.elements) == len(other.elements) == 0:
            return CustomSet()

        elif len(self.elements) == 0:
            return CustomSet()

        else:
            if len(other.elements) == 0:
                return self.elements
            else:
                ind_to_pop = []

                for i in range(len(self.elements)):
                    if self.elements[i] in other.elements:
                        ind_to_pop.append(i)

                for item in ind_to_pop:
                    self.elements.pop(item)

    def __add__(self, other):
        if len(self.elements) == len(other.elements) == 0:
            return CustomSet()

        elif len(self.elements) == 0:
            return other.elements

        elif len(other.elements) == 0:
            return self.elements
        else:
            x = sorted(self.elements)
            y = sorted(other.elements)
            total = []

            for item in other.elements:
                if item not in self.elements:
                    total.append(item)

            for item in total:
                for i in range(len(self.elements)):
                    if item < self.elements[i]:
                        self.elements = self.elements[:i] + [item] + self.elements[i:]
