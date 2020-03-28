class Lotto:

    def __init__(self, user_numbers, winning_numbers):
        self.user_numbers = user_numbers
        self.winning_numbers = winning_numbers
        self.CORRECT_ANS = 0
    
    def compare_lists(self):
        try:
            self.user_numbers = list(map(int, self.user_numbers))
            CORRECT_ANS = 0

            for i in range(6):
                for j in range(6):
                    if self.user_numbers[i] == self.winning_numbers[j]:
                        CORRECT_ANS += 1

                self.CORRECT_ANS = CORRECT_ANS 
            
            if CORRECT_ANS == 5:
                for i in range(6):
                    if self.user_numbers[i] == self.winning_numbers[-1]:
                        CORRECT_ANS = 7          # second prize is '7'

                    self.CORRECT_ANS = CORRECT_ANS

        except ValueError:
            print("ERROR : Please write in integer")


    def __str__(self):
        if self.CORRECT_ANS < 3:
            return "SORRY, It's a bad one"
        
        if self.CORRECT_ANS == 3:
            return "You won fifth prize"
        
        if self.CORRECT_ANS == 4:
            return "You won fourth prize"
        
        if self.CORRECT_ANS == 5:
            return "You won third prize"
        
        if self.CORRECT_ANS == 7:
            return "CONGRATULATION! You won second prize"
        
        if self.CORRECT_ANS == 6:
            return "CONGRATULATION!!! You won the first prize"