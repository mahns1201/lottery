import random
from LottoObject import Lotto

class PlayTheLotto:

    def __init__(self):
        self.user_lotto_numbers = []
        self.winning_lotto_numbers = []
        self.NUMBER_OF_LOTTOS = 0

    def init(self):
        try:
            self.winning_lotto_numbers = random.sample(range(1,45), 7)  #7th number is bonus number
            print(self.winning_lotto_numbers)

            self.NUMBER_OF_LOTTOS = int(input("How much will you pay? : ")) // 1000

            if self.NUMBER_OF_LOTTOS < 1000:
                print("The price of one lottery is 1000")

            while self.NUMBER_OF_LOTTOS > 0:
                self.NUMBER_OF_LOTTOS -= 1

                user_numbers = input("Type 6 lottery nombers(numbers are sparated in ',') : ").replace(" ", "").split(',')
                
                if len(user_numbers) > 6:
                    print("The lottery number's length is should be 6.")
                    break
                
                user_lotto = Lotto(user_numbers, self.winning_lotto_numbers)
                self.user_lotto_numbers.append(user_lotto)
        
        except ValueError:
            print("ERROR : Please write in integer")

    def play(self):
        for user_lotto_number in self.user_lotto_numbers:
            user_lotto_number.compare_lists()   
            
    def print_state(self):
        for user_lotto_number in self.user_lotto_numbers:
            print(user_lotto_number)