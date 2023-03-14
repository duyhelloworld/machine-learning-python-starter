car = {
    "name" : "Vinfast",
    "model": "VF8",
    "year": 2019
}

print(car["name"])

car["model"] = "VF9"
# Or
car.update({"year": 2020})
car.update({"color": "black"})

print(car.items())
print(car.values())
print(car.keys())

if "model" in car :
    print("Existed ", car["model"])

print(car.setdefault("owner", "Pham Duc Duy"))
print(car.setdefault("owner", "unknown"))
print(car)