from decimal import Decimal, getcontext

# Set precision to 4 decimal places
getcontext().prec = 4

# Example of high-precision arithmetic
decimal_sum = Decimal('0.1234') + Decimal('0.5678')
print("Sum with Decimal precision:", decimal_sum)
# Example Output: Sum with Decimal precision: 0.6912

# Handling large financial calculations
amount = Decimal('123456.7891')
tax_rate = Decimal('0.05')
tax = amount * tax_rate
total_amount = amount + tax
print("Total amount with Decimal precision:", total_amount)
# Example Output: Total amount with Decimal precision: 129629.6286
