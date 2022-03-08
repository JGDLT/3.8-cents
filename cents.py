def MakeChange(a):
    print("number of quarters: ", int(a/25))
    b = a % 25
    print("number of dimes: ", int(b/10))
    c = b % 10
    print("number of nickles: ", int(c/5))
    d = c % 5
    print("number of pennies: ", int(d/1))

   
print("Give me an amount of cents")
money = int(input())
MakeChange(money)
