# While loop

# x=0
# while (x<=5):
#        print(x)
#        x=x+1

# For Loop
# for t in range(4,11):
#     print(t)

#array
days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]

for d in days:
    #if (d=="Fri"):break #loop stops
    if(d=="Fri"): continue #skip fri
    print(d)
