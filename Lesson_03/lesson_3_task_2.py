from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79111111111"),
    Smartphone("Samsung", "Galaxy S24", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79333333333"),
    Smartphone("Huawei", "P60", "+79444444444"),
    Smartphone("Honor", "Magic 6", "+79555555555"),
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
