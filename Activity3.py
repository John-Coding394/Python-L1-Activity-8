r = int(input("Do you want a car or a bike 1=car 2=bike "))

if r == 1:
    a = int(input("Do you want a diesel car or electric car 1=diesel 2=electric "))
    if a == 1:
        print("You want a diesel car")
    else:
        print("You want an electric car")

else:
    b = int(input("Do you want a pedal bike or a motorized bike 1=pedal 2=motorized"))
    if b == 1:
        print("You want a pedal bike")
    else: 
        print("You want a motorized bike")
