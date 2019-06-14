def main():
	cardNumber = input('Card Number: ').replace(' ', '')
	digits = [int(char) for char in cardNumber]
	digits = digits[::-1]

	# step1: double alternating digits from RHS
	doubledDigits = []
	for (count,digit) in enumerate(digits):
		if (count+1)%2==0:
			doubledDigits.append(digit*2)
		else:
			doubledDigits.append(digit)

	#step2: take mod10 if the number is two digit
	arrayToBeSummed = []
	for num in doubledDigits:
		if num < 10:
			arrayToBeSummed.append(num)
		else:
			arrayToBeSummed.append(num-9)

	#step3: add all the numbers of arr and mod10
	if sum(arrayToBeSummed)%10==0:
		print('Valid Card')
	else:
		print('Invalid Card')

if __name__ == '__main__':
	main()