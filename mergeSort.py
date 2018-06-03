def merge(arr,first,mid,last):
	num1 = mid-first+1
	num2 = last-mid
	arr2 = list()
	arr3 = list()

	for x in range(num1):
		arr2.append(arr[first+x])

	for y in range(num2):
		arr3.append(arr[mid+1+y])
	arr2.append(9999);
	arr3.append(9999);

	i=0
	j=0	
	for k in range(first,last+1):
			if arr2[i]<=arr3[j] :
				arr[k] = arr2[i]
				i+=1
			else:
				arr[k] = arr3[j]
				j+=1

def mergeSort(arr,first,last):
	if first<last:
		mid = (first+last)/2
		mergeSort(arr,first,mid)
		mergeSort(arr,mid+1,last)
		merge(arr,first,mid,last)

def display(arr,num):
	print "Sorted Array:"
	for i in range(num):
		print arr[i] 

def main():
	arr = list()
	num = input('how many numbers?')
	for i in range(num):
		arr.append(int(input()))
	mergeSort(arr,0,num-1)
	display(arr,num)

main()

