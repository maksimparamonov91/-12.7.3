money = int(input("Введите сумму, которую планируете положить под проценты (money):"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values = list(per_cent.values())
print("deposit =",list(map(lambda x: x * money // 100, per_cent_values)))
print("Максимальная сумма, которую вы можете заработать —",max(list(map(lambda x: x * money // 100, per_cent_values))))

