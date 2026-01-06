# ============================================
# ATM MACHINE  PROJECT
# ============================================

class ATM:
    def __init__(self):
        self.cards = { 
            "1234": {"pin": 1234, "balance": 50000},
            "3333": {"pin": 3333, "balance": 2000},
            "2222": {"pin": 2222, "balance": 3000}
        }
        self.current_user = None
        self.current_balance = 0 

    def verify_card(self, card_number):
        if card_number in self.cards:
            self.current_user = card_number 
            return True
        else:
            return False 

    def verify_pin(self, card_number, pin_code):
        if card_number not in self.cards:
            return False 
        stored_pin = self.cards[card_number]["pin"]
        return pin_code == stored_pin
    
    def check_balance(self, card_number):
        if card_number in self.cards:
            balance = self.cards[card_number]["balance"]
            self.current_balance = balance
            return balance
        else:
            return None

    def withdraw_money(self, card_number, amount):
        if card_number not in self.cards:
            return "Card not found"
        
        current_balance = self.cards[card_number]["balance"]
        if amount > current_balance:
            return f"Insufficient balance! Available: {current_balance}"
        if amount <= 0:
            return "Enter valid amount"
        
        self.cards[card_number]["balance"] -= amount
        new_balance = self.cards[card_number]["balance"]
        return f"Withdrawal successful! Amount: {amount}, Balance: {new_balance}"


def main():
    print("Welcome to ATM SERVICE")
    atm = ATM()
    
    print("\nInsert card")
    card = input("Enter your card number: ")
    
    if not atm.verify_card(card):
        print("Please enter valid card number")
        return
    
    print("Card successfully verified")

    print("\nEnter PIN")
    attempts = 5
    
    while attempts > 0:
        pin = int(input(f"Enter your PIN (Attempts left: {attempts}): "))
        
        if atm.verify_pin(card, pin):
            print("PIN verified!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong PIN! Try again.")
            else:
                print("All attempts failed! Card blocked.")
                return
    
    while True:
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("=" * 40)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        print("=" * 40)
        
        choice = input("Choose option (1/2/3): ")
        
        if choice == "1":
            balance = atm.check_balance(card)
            print(f"\nYour Balance: {balance}")
        
        elif choice == "2":
            amount = int(input("Enter withdrawal amount: "))
            result = atm.withdraw_money(card, amount)
            print(f"\n{result}")
        
        elif choice == "3":
            print("\nThank you for using ATM! Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3")


if __name__ == "__main__":
    main()
