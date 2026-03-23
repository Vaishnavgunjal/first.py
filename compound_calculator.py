print("Compound Interest Calculator")

# Inputs
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (in years): "))
n = int(input("Enter number of times interest is compounded per year: "))

'''compound intrest formula'''
amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

# Output
print("\n--- Result ---")
print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {amount:.2f}")
