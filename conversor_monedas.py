def converter(currency, usd):
    currency_amount = float(input("Type the amount: \n"))
    usd_amount = currency_amount / usd
    print("The amount of {} you have is: USD {:.3f}.".format(currency, usd_amount))


menu = '''
Welcome to my Currency Converter 🤑
1 - COP
2 - MXN
3 - ARS
Please choose one:
'''
choose = int(input(menu))

if choose == 1:
    converter("COP", 3746)
elif choose == 2:
    converter("MXN", 20.10)
elif choose == 3:
    converter("ARS", 115.75)
else:
    print("Ey Please check your option again 🤪")