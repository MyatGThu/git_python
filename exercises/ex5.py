def compenrate(hours, rate):
    # print(fh, fr)
    if hours > 40:
        # print('Overtime')
        reg = rates * hours
        otpay = (hours - 40.0) * (rate * 0.5)
        # print(pay, otpay)
        pay = reg + otpay
    else:
        # print('Regular')
        pay = hours * rate
     # print('Retruning: ', pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fr = float(sr)
    fh = float(sh)
except:
    print("Error, Require numeric input.")
    quit()

xp = compenrate(fh,fr)


print("Pay: ", xp)
