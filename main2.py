per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = 100000
for bank_percent in per_cent.values():
    deposit_element = bank_percent * money / 100
    deposit.append(deposit_element)
print(deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')









