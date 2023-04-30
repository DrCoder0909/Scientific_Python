hrs = input("Enter Hours:")
rate= input("Enetr rate per hour")
h = float(hrs)
r= float(rate)
if h<=40:
    pay1=h*r
else:
    h1=h-40
    pay1=(40*r) + (h1*r*1.5)
print(pay1)
