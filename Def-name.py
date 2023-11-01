def print_Tellazone():
    text = "Tellazone is the chief excecutive officcer"
    print(text)
    print(text)
    print(text)

print_Tellazone()
print_Tellazone()
print_Tellazone()

#
def school_age_calculator(age,name):
    if age<5:
        print("enjoy your learning",name,'is only',age)
    elif age == 5:
        print("Enjoy grade1",name)
    else:
        print("they grow very fast")

school_age_calculator(5,'Abdon')

# how old will be in 10 years

def add_ten_age(age):
    new_age = age + 10
    return new_age
how_old_will_i_be = add_ten_age(3)
print(how_old_will_i_be)

#while loop
x=0
while(x<5):
    print(x)
    x=x+1

# for loop
for x in range(5,10):
    print(x)

days = ["Mon","Tue","Wed","Thu","Fry","Sat","Sun"] 
for d in days:
    if (d=="Thu"):continue
    print(d)



