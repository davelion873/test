# import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes=70))

# import fmath
# fmath.add(1, 2)
# fmath.substract(1, 2)

from colorama import Fore, Style
print(Fore.RED + "Hello World")

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello World")