#Best print results with libreoffice "Liberation Mono" 10pt > 64 lines a 80 characters
#usage in terminal: python3 devision_12x12.py > math_sheet.txt

import random

for i in range(64):
	n1 = random.randint(2,12)
	n2 = random.randint(2,12)
	n3 = random.randint(2,12)
	n4 = random.randint(2,12)
	n5 = random.randint(2,12)
	n6 = random.randint(2,12)
	r1 = n1 * n2
	r2 = n3 * n4
	r3 = n5 * n6
	print(f"{r1:>3} : {n1:>2} =_|_|_|_|_|_|_{n2:>2}  {r2:>3} : {n3:>2} =_|_|_|_|_|_|_{n4:>2}  {r3:>3} : {n5:>2} =_|_|_|_|_|_|_{n6:>2}")
	



	
	
