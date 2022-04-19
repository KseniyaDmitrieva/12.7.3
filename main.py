per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = 100000
deposit_element = per_cent['ТКБ'] * money / 100
deposit.append(deposit_element)
deposit_element = per_cent['СКБ'] * money / 100
deposit.append(deposit_element)
deposit_element = per_cent['ВТБ'] * money / 100
deposit.append(deposit_element)
deposit_element = per_cent['СБЕР'] * money / 100
deposit.append(deposit_element)
print(deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')









