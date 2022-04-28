count_tickets = int(input('Укажите количество билетов:'))
sum_tickets = 0
for client in range(0, count_tickets):
    age = int(input('Укажите возраст посетителя'))
    ticket_price = 0
    if 25 > age > 18:
        ticket_price = 990
    if age > 25:
        ticket_price = 1390
    sum_tickets += ticket_price
if count_tickets > 3:
    sum_tickets *= 0.9
print(sum_tickets)