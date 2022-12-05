#Best print results with libreoffice "Liberation Mono" 10pt > 64 lines a 80 characters
#usage in terminal: python3 plus_minus_hundrets.py > math_sheet.txt

import random

initial = 777
ten = 0

for i in range(64):
	n1 = random.randint(1,99)
	n2 = random.randint(1,99)
	n3 = random.randint(1,99)
	n4 = random.randint(1,99)
	n5 = random.randint(1,99)
	n6 = random.randint(1,99)
	n7 = random.randint(1,99)
	n8 = random.randint(1,99)
	result = initial - i - ten + n1 - n2 + n3 - n4 + n5 - n6 + n7 - n8
	print(f"{initial - i - ten:>3} + {n1:>2} - {n2:>2} + {n3:>2} - {n4:>2} + {n5:>2} - {n6:>2} + {n7:>2} - {n8:>2}=|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_{result:>4}")
	ten = ten + 10


	
	
