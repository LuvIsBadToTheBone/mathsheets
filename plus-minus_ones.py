#Best print results with libreoffice "Liberation Mono" 10pt > 64 lines a 80 characters
#usage in terminal: python3 plus_minus_ones.py > math_sheet.txt

import random

initial = 77

for i in range(64):
	n1 = random.randint(1,9)
	n2 = random.randint(1,9)
	n3 = random.randint(1,9)
	n4 = random.randint(1,9)
	n5 = random.randint(1,9)
	n6 = random.randint(1,9)
	n7 = random.randint(1,9)
	n8 = random.randint(1,9)
	result = initial - i + n1 - n2 + n3 - n4 + n5 - n6 + n7 - n8
	print(f"{initial - i:>2} + {n1} - {n2} + {n3} - {n4} + {n5} - {n6} + {n7} - {n8}=|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_{result:>3}")


	
	
