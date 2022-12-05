#Best print results with libreoffice "Liberation Mono" 10pt > 64 lines a 80 characters
#usage in terminal: python3 plus_minus_hundrets.py > math_sheet.txt

import random

initial = 7777
hundret = 0

for i in range(64):
	n1 = random.randint(1,999)
	n2 = random.randint(1,999)
	n3 = random.randint(1,999)
	n4 = random.randint(1,999)
	n5 = random.randint(1,999)
	n6 = random.randint(1,999)
	n7 = random.randint(1,999)
	n8 = random.randint(1,999)
	result = initial - i - hundret + n1 - n2 + n3 - n4 + n5 - n6 + n7 - n8
	print(f"{initial - i - hundret:>4} + {n1:>3} - {n2:>3} + {n3:>3} - {n4:>3} + {n5:>3} - {n6:>3} + {n7:>3} - {n8:>3}=|_|_|_|_|_|_|_|_|_|_|_{result:>5}")
	hundret = hundret + 100


	
	
