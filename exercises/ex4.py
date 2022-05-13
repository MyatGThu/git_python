sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fr = float(sr)
    fh = float(sh)
except:
    print("Error, Require numeric input.")
    quit()

# print(fh, fr)
if sh > 40:
    # print('Overtime')
    pay = fr * fh
    otpay = (fh - 40.0) * (fr * 0.5)
    # print(pay, otpay)
    pay = pay + otpay
elif fh < 40:
    # print('Regular')
    pay = fh * fr

print("Pay: ", pay)
