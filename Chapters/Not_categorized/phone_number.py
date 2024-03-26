letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","u","p","r","s","t","q","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
punctuation = ["?",",",":",";","-","!","@"]


class PhoneNumber:
    def __init__(self, number):
        self.number = number
        has_letters = False
        has_punctuation = False

        for item in number:
            if item in letters:
                has_letters = True

        for item in range(len(number)-2):
            if number[item] in punctuation and number[item+1] in punctuation:
                has_punctuation = True

        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(number) == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")
        elif has_letters:
            raise ValueError("letters not permitted")
        elif has_punctuation:
            raise ValueError("punctuations not permitted")
        else:
            for item in number:
                if item not in numbers:
                    self.number = self.number.replace(item,"")

            if len(self.number) == 11:
                if self.number[1] == "0":
                    raise ValueError("area code cannot start with zero")
                elif self.number[1] == "1":
                    raise ValueError("area code cannot start with one")
                elif self.number[4] == "0":
                    raise ValueError("exchange code cannot start with zero")
                elif self.number[4] == "1":
                    raise ValueError("exchange code cannot start with one")
                else:
                    self.number = self.number[1:]
                    self.area_code = self.number[:3]
            elif len(self.number) > 11:
                raise ValueError("must not be greater than 11 digits")
            elif len(self.number) == 10:
                if self.number[0] == "0":
                    raise ValueError("area code cannot start with zero")
                elif self.number[0] == "1":
                    raise ValueError("area code cannot start with one")
                elif self.number[3] == "0":
                    raise ValueError("exchange code cannot start with zero")
                elif self.number[3] == "1":
                    raise ValueError("exchange code cannot start with one")
                else:
                    self.area_code = self.number[:3]

    def pretty(self):
        if len(self.number) == 10:
            return "(" + self.number[:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
        else:
            return "(" + self.number[1:4] + ")-" + self.number[4:7] + "-" + self.number[7:]