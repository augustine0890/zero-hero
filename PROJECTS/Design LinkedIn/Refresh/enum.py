import enum


class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3


print("The string representation of enum member is : ",end="")
print(Animal.dog)

# printing enum member as repr
print("The repr representation of enum member is : ",end="")
print(repr(Animal.dog))

# printing the type of enum member using type()
print("The type of enum member is : ",end ="")
print(type(Animal.dog))

# printing name of enum member using "name" keyword
print("The name of enum member is : ",end ="")
print(Animal.dog.name)

# printing all enum members using loop
print ("All the enum values are : ")
for Anim in (Animal):
    print(Anim)

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print("Enum is hashed")
else:
    print("Enum isn't hashed")

# Accessing enum member using value 
print("The enum member associated with value 2 is : ", end="")
print(Animal(2))

# Accessing enum member using name
print("The enum member associated with name lion is : ", end="")
print(Animal['lion'])

# Assigning enum member
mem = Animal.dog 

# Displaying value
print("The value associated with dog is : ", end="")
print(mem.value)

# Displaying name
print("The name associated with dog is : ", end="")
print(mem.name)

# Comparison using "is"
if Animal.dog is Animal.cat:
       print ("Dog and cat are same animals")
else:
    print ("Dog and cat are different animals")
  
# Comparison using "!="
if Animal.lion != Animal.cat:
    print ("Lions and cat are different")
else:
    print ("Lions and cat are same")