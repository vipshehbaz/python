eng =  int(input("Enter english marks "))
urdu = int(input("Enter urdu marks "))
math = int(input("Enter math marks "))

om = int(eng + urdu + math)
print ( "your total marks is ",om)
if om >= 90 :
    print("A+")
elif om >= 80:
    print("A")
elif om >= 70:
    print("B")
elif om >= 60:
    print("C")
elif om >= 50:
    print("D")
else:
    print("FAIL")