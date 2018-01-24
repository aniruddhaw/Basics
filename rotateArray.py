
def rotateArray(array,num):
	rotateFactor = input('enter the rotate factor:')
	for i in range(gcd(rotateFactor,num)):
		temp = array[i]
		j = i

		while 1:
			k = j+rotateFactor
			if k >= num:
				k = k - num
			if k == i:
				break
			array[j] = array[k]
			j = k
		
		array[j] = temp
	printArray(array,num)

def printArray(array,num):
	for i in range(num):
		print ("%d" % array[i])
		#print ("\n")


def gcd(a,b):
	if b==0:
		return a;
	else:
		return gcd(b, a%b)


def main():
	array = list()
	num = input('How many numbers?')
	print 'Please enter the numbers:'
	for i in range(num):
		array.append(input())
	rotateArray(array,num)

main()