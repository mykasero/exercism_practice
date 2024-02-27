### needs rework
class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")[::-1]
        self.new_card = ""
        self.second_list = []
        self.doubled_list = []

    def valid(self):
        if len(self.card) < 17 or len(self.card) > 18:
            for check_symbols in self.card:
                if check_symbols not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    return False
                    break
            return False
        else:
            for items in range(0, len(self.card), 2):
                self.second_list.append(self.card[items])
            for numb in self.second_list:
                numb = int(numb) * 2
                if numb > 9:
                    numb -= 9
                self.doubled_list.append(numb)

            nc_ctr = 0

            for element in range(len(self.card)):
                if element % 2 == 1:
                    self.new_card += self.card[element]
                else:
                    self.new_card += str(self.doubled_list[nc_ctr])
                    nc_ctr += 1

            return self.new_card[::-1]
