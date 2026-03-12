number = input("Enter your phone number: ")
kod = number[:2]
if kod =="93" or kod =="94":
    print("UCELL")
elif kod == "91" or kod =="90":
    print("BEELINE")
elif kod == "95" or kod == "99":
    print("UZmobile")
elif kod == "88" or kod == "97":
    print("MOBIUZ")
else:
    print("other numbers!")
