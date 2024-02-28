class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")[::-1]
        self.new_card = ""
        self.second_list = []
        self.doubled_list = []

    def valid(self):
        total_sum = 0
        not_num = 0
        for item1 in self.card:
            if item1 not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                not_num += 1
        if not_num > 0:
            return False
        elif len(self.card) == 1 and self.card[0] == "0":
            return False
        else:
            for items in range(0, len(self.card)):
                if items % 2 == 0:
                    self.new_card += self.card[items]
                else:
                    if int(self.card[items]) * 2 > 9:
                        self.new_card += str((int(self.card[items]) * 2) - 9)
                    else:
                        self.new_card += str(int(self.card[items]) * 2)

            for element in self.new_card:
                total_sum += int(element)
            if total_sum % 10 == 0:
                print(total_sum)
                return True
            else:
                return False
