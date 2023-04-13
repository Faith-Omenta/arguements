def add(a,b):
    x=a+b
    print(x)

add(234,345)

def student(name,age):
    print(name)
    print(age)

student(name="Melvin",age=24)

def my_pet(pet="Artemis"):
    print(f"The name of my pet is {pet}")

my_pet("Artemis")

def greetings(*names):
    for name in names:
        print(f"Hello {name}")

greetings("Melvin")
greetings("Glenah")
greetings("Phylis")
greetings("Darlene")

def sum_multipication(sum,multiplication):
    return(f"the sum of 16 and 3 is {sum} and their product is {multiplication}") 

print(sum_multipication(16+3,16*3))





