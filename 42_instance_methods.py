# INSTANCE METHODS

class Payslips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return f"{self.name} has been paid {self.amount}"
        else:
            return f"{self.name} has not been paid yet"

# Create an instance of the Payslips class
nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 2000)

print(f"Nathan payment: {nathan.payment}") # Nathan payment: no
print(nathan.status())  # Nathan has not been paid yet
print(f"Roger payment: {roger.payment}") # Roger payment: no
print(roger.status())  # Roger has not been paid yet

# Pay Nathan
print(f"Paying {nathan.name}...")
nathan.pay()
print(f"Nathan payment: {nathan.payment}") # Nathan payment: yes
print(nathan.status())  # Nathan has been paid 1000
print(f"Roger payment: {roger.payment}") # Roger payment: no
print(roger.status())  # Roger has not been paid yet
