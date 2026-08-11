# ============================================
#         🏦 BANKING APPLICATION 🏦
# ============================================

# Dictionary to store all accounts: {account_number: {details}}
accounts = {}

# Welcome message
print("=" * 60)
print("        🏦 WELCOME TO PYTHON BANK 🏦")
print("=" * 60)


# ---------- CREATE ACCOUNT ----------
print("\n➕ CREATE NEW ACCOUNT")
print("-" * 50)

name = input("Enter account holder name: ").strip()
if not name:
    print("❌ Name cannot be empty.")
else:
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("❌ Account number must be numeric.")
        acc_num = None

    if acc_num is not None:
        # Prevent duplicate account numbers
        if acc_num in accounts:
            print(f"❌ Account number {acc_num} already exists.")
        else:
            try:
                initial_balance = float(input("Enter initial deposit amount: ₹"))
                if initial_balance < 0:
                    print("❌ Initial balance cannot be negative.")
                else:
                    accounts[acc_num] = {
                        "name": name.title(),
                        "balance": initial_balance
                    }
                    print(f"✅ Account created successfully for {name.title()}!")
                    print(f"   Account Number : {acc_num}")
                    print(f"   Initial Balance: ₹{initial_balance}")
            except ValueError:
                print("❌ Invalid amount.")


# ---------- MENU LOOP ----------
while True:
    print("\n" + "=" * 60)
    print("                  📋 MAIN MENU")
    print("=" * 60)
    print("  1. ➕ Create Account")
    print("  2. 💰 Deposit")
    print("  3. 💸 Withdraw")
    print("  4. 🧾 Check Balance")
    print("  5. 🔄 Transfer Money")
    print("  6. 📊 Show All Accounts")
    print("  7. 🚪 Exit")
    print("=" * 60)

    choice = input("Enter your choice (1-7): ").strip()

    # ---------- CREATE ACCOUNT ----------
    if choice == "1":
        print("\n➕ CREATE NEW ACCOUNT")
        print("-" * 50)

        name = input("Enter account holder name: ").strip()
        if not name:
            print("❌ Name cannot be empty.")
        else:
            try:
                acc_num = int(input("Enter account number: "))
            except ValueError:
                print("❌ Account number must be numeric.")
            else:
                if acc_num in accounts:
                    print(f"❌ Account number {acc_num} already exists.")
                else:
                    try:
                        initial_balance = float(input("Enter initial deposit amount: ₹"))
                        if initial_balance < 0:
                            print("❌ Initial balance cannot be negative.")
                        else:
                            accounts[acc_num] = {
                                "name": name.title(),
                                "balance": initial_balance
                            }
                            print(f"✅ Account created successfully for {name.title()}!")
                            print(f"   Account Number : {acc_num}")
                            print(f"   Initial Balance: ₹{initial_balance}")
                    except ValueError:
                        print("❌ Invalid amount.")

    # ---------- DEPOSIT ----------
    elif choice == "2":
        print("\n💰 DEPOSIT MONEY")
        print("-" * 50)

        try:
            acc_num = int(input("Enter account number: "))
        except ValueError:
            print("❌ Account number must be numeric.")
            continue

        if acc_num not in accounts:
            print(f"❌ Account {acc_num} does not exist.")
        else:
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("❌ Deposit amount must be positive.")
                else:
                    accounts[acc_num]["balance"] += amount
                    print(f"✅ ₹{amount} deposited successfully.")
                    print(f"   New Balance: ₹{accounts[acc_num]['balance']}")
            except ValueError:
                print("❌ Invalid amount.")

    # ---------- WITHDRAW ----------
    elif choice == "3":
        print("\n💸 WITHDRAW MONEY")
        print("-" * 50)

        try:
            acc_num = int(input("Enter account number: "))
        except ValueError:
            print("❌ Account number must be numeric.")
            continue

        if acc_num not in accounts:
            print(f"❌ Account {acc_num} does not exist.")
        else:
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("❌ Withdrawal amount must be positive.")
                elif amount > accounts[acc_num]["balance"]:
                    print(f"❌ Insufficient balance. Available: ₹{accounts[acc_num]['balance']}")
                else:
                    accounts[acc_num]["balance"] -= amount
                    print(f"✅ ₹{amount} withdrawn successfully.")
                    print(f"   Remaining Balance: ₹{accounts[acc_num]['balance']}")
            except ValueError:
                print("❌ Invalid amount.")

    # ---------- CHECK BALANCE ----------
    elif choice == "4":
        print("\n🧾 CHECK BALANCE")
        print("-" * 50)

        try:
            acc_num = int(input("Enter account number: "))
        except ValueError:
            print("❌ Account number must be numeric.")
            continue

        if acc_num not in accounts:
            print(f"❌ Account {acc_num} does not exist.")
        else:
            acc = accounts[acc_num]
            print(f"\n   Account Holder : {acc['name']}")
            print(f"   Account Number : {acc_num}")
            print(f"   Current Balance: ₹{acc['balance']}")

    # ---------- TRANSFER ----------
    elif choice == "5":
        print("\n🔄 TRANSFER MONEY")
        print("-" * 50)

        try:
            from_acc = int(input("Enter sender account number: "))
            to_acc = int(input("Enter receiver account number: "))
        except ValueError:
            print("❌ Account numbers must be numeric.")
            continue

        if from_acc not in accounts:
            print(f"❌ Sender account {from_acc} does not exist.")
        elif to_acc not in accounts:
            print(f"❌ Receiver account {to_acc} does not exist.")
        elif from_acc == to_acc:
            print("❌ Cannot transfer to the same account.")
        else:
            try:
                amount = float(input("Enter amount to transfer: ₹"))
                if amount <= 0:
                    print("❌ Transfer amount must be positive.")
                elif amount > accounts[from_acc]["balance"]:
                    print(f"❌ Insufficient balance. Available: ₹{accounts[from_acc]['balance']}")
                else:
                    # Update both accounts
                    accounts[from_acc]["balance"] -= amount
                    accounts[to_acc]["balance"] += amount
                    print(f"✅ ₹{amount} transferred successfully.")
                    print(f"   From: {accounts[from_acc]['name']} (₹{accounts[from_acc]['balance']})")
                    print(f"   To  : {accounts[to_acc]['name']} (₹{accounts[to_acc]['balance']})")
            except ValueError:
                print("❌ Invalid amount.")

    # ---------- SHOW ALL ACCOUNTS ----------
    elif choice == "6":
        print("\n📊 ALL ACCOUNTS IN THE BANK")
        print("=" * 70)

        if not accounts:
            print("❌ No accounts in the bank yet.")
        else:
            print(f"{'Acc No.':<12}{'Name':<25}{'Balance':>20}")
            print("-" * 70)
            for acc_num, acc in accounts.items():
                print(f"{acc_num:<12}{acc['name']:<25}{'₹' + format(acc['balance'], ','):>20}")

            # Calculate total money and richest customer
            total_money = sum(acc["balance"] for acc in accounts.values())
            richest_acc = max(accounts.items(), key=lambda item: item[1]["balance"])
            richest_num, richest = richest_acc

            print("\n" + "=" * 70)
            print("                🏆 BANK STATISTICS")
            print("=" * 70)
            print(f"  💰 Total Money in Bank  : ₹{format(total_money, ',')}")
            print(f"  👑 Richest Customer     : {richest['name']}")
            print(f"     Account Number       : {richest_num}")
            print(f"     Balance              : ₹{format(richest['balance'], ',')}")
            print(f"  👥 Total Accounts       : {len(accounts)}")
            print("=" * 70)

    # ---------- EXIT ----------
    elif choice == "7":
        print("\n👋 Thank you for banking with Python Bank!")
        print("💰 Have a great day!\n")
        break

    # ---------- INVALID ----------
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 7.")
