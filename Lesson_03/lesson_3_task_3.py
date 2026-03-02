from address import Address
from mailing import Mailing


from_address = Address(
    "101000",
    "Москва",
    "Тверская",
    "1",
    "10"
)

to_address = Address(
    "190000",
    "Санкт-Петербург",
    "Невский",
    "5",
    "20"
)

mail = Mailing(
    to_address,
    from_address,
    350.50,
    "TR123456789RU"
)

print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, "
    f"{mail.from_address.city}, "
    f"{mail.from_address.street}, "
    f"{mail.from_address.house} - "
    f"{mail.from_address.apartment} "
    f"в {mail.to_address.index}, "
    f"{mail.to_address.city}, "
    f"{mail.to_address.street}, "
    f"{mail.to_address.house} - "
    f"{mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
