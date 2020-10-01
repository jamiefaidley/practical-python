# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 1

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = payment + extra_payment
    if principal <= payment:
        payment = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment

    total_paid = total_paid + payment
    payment = 2684.11
    month += 1
    print(f'After month {month} we have paid {total_paid} and have {principal} left!')

print('Total paid', round(total_paid,2))
