units=int(input())
if units<50:
    bill=(units*2)
elif units<150:
    bill=50*2+((units-50)*3)
elif units<250:
    bill=50*2+100*3+(units-150)*5
elif units>=250:
    bill=50*2+100*3+100*5+(units-250)*8
surcharge=bill*0.2
print(bill+surcharge)
