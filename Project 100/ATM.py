class ATM(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo

    def cashWithDrawal(self):
        self.cardNo=input("Enter your card number : ")
        self.pinNo=input("Enter you pin number : ")
        amount1=input("Enter the amount you want to withdraw : ")
        if (int(amount1)>=500):
            print("You have withdrawn Rs : " + amount1)
        else:
            print("Please enter an amount of value 500 or greater")

    def cashDeposit(self):
        self.cardNo=input("Enter your card number : ")
        self.pinNo=input("Enter you pin number : ")
        amount2=input("Enter the amount you want to deposit : ")
        if (int(amount2)>=500):
            print("You have deposited Rs : " + amount2)
        else:
            print("Please enter an amount of value 500 or greater")
    
    def ATMode(self):
        select=int(input("Hello! Welcome to your ATM. Please enter 1 if you want to WITHDRAW money. Please enter 2 if you want to DEPOSIT money : "))
        if(select==1):
            self.cashWithDrawal()
        else:
            self.cashDeposit()

object=ATM(0000, 000000)
object.ATMode() 