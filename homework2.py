list=list()
Firstname=input("Enter Your Name")
list.append(Firstname)
Lastname=input("Enter Your Lastname")
list.append(Lastname)
Age=int(input("Enter Your Age"))
list.append(Age)
Birth=int(input("Enter Your Birth Year"))
list.append(Birth)

for i in range(len(list)):
    print(list[i],"\n")

if Age < 18 and Age >= 0:
    print("You can't go out because it's too dangerous")

elif Age >= 18:
    print("you can go out to the street")

else:
    print("İnvalid Age")
