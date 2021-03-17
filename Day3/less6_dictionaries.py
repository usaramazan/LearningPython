# we do like map in java, we use key,value parts. And key must be unique
customer ={
    "name":"Ramazan",
    "age":30,
    "is_verified":True
}
print(customer["name"])
print(customer.get('name'))
print(customer.get("birthdate")) #it returns NONE, none is an obj also. but if I make like in below
#it gives error
#print(customer['birthdate'])

#lets update the name
customer['name']='Cemile'
print(customer['name'])

# we can add new key and value
customer['birthdate']= 'March 12 1987'
print(customer['birthdate'])