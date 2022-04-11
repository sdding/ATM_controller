class Bank:
    personal_data = {45161542: {"pin": 1234, "account": {569856: 54000,
                                                         965866: 126000}},
                    58965274: {"pin": 4567, "account": {1256985: 308000,
                                                        3524156: 7000}}}

class ATM:
    def __init__(self, card_num):
        self.card_num = card_num

    def Check_PIN_num(self):
        if self.card_num in Bank.personal_data:
            pswrd = int(input("Password : "))
            if pswrd != Bank.personal_data[self.card_num]["pin"]:
                while pswrd != Bank.personal_data[self.card_num]["pin"]:
                    print("Wrong password, try again")
                    pswrd = int(input("Password : "))

            return True
        else:
            print("Invalid Card")
            return False
            

    def Check_Account(self):
        if ATM.Check_PIN_num(self) == True:
            print("Choose account")
            for account in Bank.personal_data[self.card_num]["account"]:
                print(account)

            entered_account = int(input("Account : "))

            if entered_account not in Bank.personal_data[self.card_num]["account"].keys():
                while entered_account not in Bank.personal_data[self.card_num]["account"].keys():
                    print("Wrong Account, try again")
                    entered_account = int(input("Account : "))
            return entered_account

    def Controller(self):
        if ATM.Check_PIN_num(self) == True:
            entered_account = ATM(self.card_num).Check_Account()
            entered_action = input("Balance or Deposit or Withdraw : ").lower()

            if entered_action == "balance":
                print("======================")
                print("Account :", entered_account)
                print("Remaining amount :", Bank.personal_data[self.card_num]["account"][entered_account])
            elif entered_action == "deposit":
                money = int(input("Insert money : "))

                Bank.personal_data[self.card_num]["account"][entered_account] += money
                print("======================")
                print("Successfully Deposited")
                print("Account :", entered_account)
                print("Remaining amount :", Bank.personal_data[self.card_num]["account"][entered_account])
            elif entered_action == "withdraw":
                money = int(input("How much : "))

                if money > Bank.personal_data[self.card_num]["account"][entered_account]:
                    while money > Bank.personal_data[self.card_num]["account"][entered_account]:
                        print("No money")
                        print("Your balance is :", Bank.personal_data[self.card_num]["account"][entered_account])
                        money = int(input("How much : "))

                Bank.personal_data[self.card_num]["account"][entered_account] -= money
                print("======================")
                print("Successfully Withdrawn")
                print("Account :", entered_account)
                print("Remaining amount :", Bank.personal_data[self.card_num]["account"][entered_account])

       
if __name__ == "__main__":
    card = int(input("Insert Card : "))
    ATM(card).Controller()
                

                


            
            
            




        

