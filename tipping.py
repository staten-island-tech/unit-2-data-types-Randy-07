bill = float(input("what was the cost of your meal?"))
service = (input("was your service great, good, okay or bad?"))
if service == "great":
    print("your final cost:"(float(bill * 1.25)))
if service == "good":
    print(float(bill * 1.20))
if service == "okay":
    print(float(bill * 1.15))
if service == "bad":
    print(float(bill))