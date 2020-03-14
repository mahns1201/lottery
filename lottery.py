import random

class Lotto:
    def __init__(self, UserNumber, WinningNumber):
        self.UserNumber = UserNumber
        self.WinningNumber = WinningNumber
        self.CorrectAns = 0

    def compare(self):
        try:
            self.UserNumber = list(map(int, self.UserNumber))
            CorrectAns = 0
            for i in range(6):
                for j in range(6):
                    if self.UserNumber[i] == self.WinningNumber[j]:
                        CorrectAns += 1
                    self.CorrectAns = CorrectAns 
            
            if CorrectAns == 5:
                for i in range(6):
                    if self.UserNumber[6] == self.WinningNumber[i]:
                        CorrectAns = 7          # second class is '7'
                    self.CorrectAns = CorrectAns
        except ValueError:
            print("ERROR : Please write in integer")
    
    #def result(self): 최종 결과가 나오는 함수,,,,,,,,,,,,,,,,,,,?

                
    def __str__(self):
        if self.CorrectAns == 7:
            return "The number of correct Answer:5 + 1(second prize)"
        return "The number of correct Answer: " + str(self.CorrectAns)


class LottoPLAY:
    def __init__(self):
        self.userLottoNumbers = []
        self.TheWinningLotteryNumber = []
        self.NumberOfLotto = 0

    def init(self):
        try:
            self.TheWinningLotteryNumber = random.sample(range(1,45), 6)
            print(self.TheWinningLotteryNumber)
            self.NumberOfLottos = int(input("how much? (The price for 1 is 1000) : ")) // 1000
            while self.NumberOfLottos != 0:
                self.NumberOfLottos -= 1
                userLottos = input("type 6 the lottery nombers: .(the number is sparated in ',') : ").replace(" ", "").split(',')
                bonusNumber = input("type the bonus number : ")
                userLottos.append(bonusNumber)
                userLotto = Lotto(userLottos, self.TheWinningLotteryNumber)
                self.userLottoNumbers.append(userLotto)
        
        except ValueError:
            print("ERROR : Please write in integer")

    def play(self):
        for userLottoNumber in self.userLottoNumbers:
            userLottoNumber.compare()   
            
    def printState(self):
        for userLOTTO in self.userLottoNumbers:
            print(userLOTTO)


new = LottoPLAY()
new.init()
new.play()
new.printState()
