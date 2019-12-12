customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
#ooorrrr.....
print(customer.get("name"))
customer["name"] = "Joe Doe"
print(customer["name"])
#supplying default value;
print(customer.get("birthdate","Jan 1 1980"))
customer["birthdate"] = "Mar 13 1994"
print(customer.get("birthdate"))