count_of_tikets = int(input("Введите количество билетов:"))
total_price = 0
for i in range(count_of_tikets):
    person_age = int(input("Введите возраст посетителя:"))
    if person_age<18:
        price_for_tiket = 0
    elif 18<=person_age<25:
        total_price += 990
    else:
        total_price += 1390
if count_of_tikets > 3:
    total_price -= total_price*0.10
print(f"Сумма к оплате: {int(total_price)} руб.")