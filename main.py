mc = input("Do you have a medical cause Y= yes N=no")
if mc == "Y" or mc =="y":    
    print("You are allowed to take the exam")

else:
    a = int(input("Enter your attendance"))
    if a  > 75: 
        print("You are eligible for exam")
    else:
        print("You are not eligible")

    