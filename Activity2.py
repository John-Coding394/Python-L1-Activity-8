u = int(input("Enter how many units you have consumed"))

if u<50:
    p = u * 2.6 + 25

elif 50<u<100:
    p = u * 3.25 + 35

elif 100<u<200:
    p = u * 5.26 + 45

else:
    p = u * 8.45 + 75

print(" You need to pay" ,  p)