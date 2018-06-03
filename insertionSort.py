def displaySortedNumbers(arr,num):
	print("Output:")
	for i in range(num):
		print arr[i]

def performInsertionSort(arr,num):
	for i in range(1,num):
		key = arr[i]
		j = i-1;
		while j>=0 and arr[j]>key:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = key
	displaySortedNumbers(arr,num)

def insertNumbers():
	arr = list()
	num = input("How many numbers?")
	for i in range(num):
		arr.append(input())
	performInsertionSort(arr,num)



insertNumbers()
if __name__ == "__main__":
	print("***** Insertion Sort *****")
else:
	print("***** Using Insertion Sort *****")

goro export --branch=cloud-big-data-blog-kcs --nouse_kcs_published --file="cloud.google.com/en/blog/big-data/index.html" \
--file="cloud.google.com/en/blog/big-data/feed.xml" \
--file="cloud.google.com/en/blog/big-data/archive/2017.html" \
--file="cloud.google.com/en/blog/big-data/2017/06/guide-to-common-cloud-dataflow-use-case-patterns-part-1.html" \
--file="cloud.google.com/blog/uploads/149756210681386/dataflow-patterns-2.png" \
--file="cloud.google.com/blog/uploads/149756210681386/dataflow-patterns-5.png" \
--file="cloud.google.com/blog/uploads/149756210681386/dataflow-patterns-1.png" \
--file="cloud.google.com/blog/uploads/149756210681386/dataflow-patterns-6.png" \
--file="cloud.google.com/blog/uploads/149756210681386/dataflow-patterns-3.png" --force --cl=new

/google/data/ro/projects/devsite/devsite stage "googledata/devsite/site-cloud/en/blog/big-data/index.html" \
"googledata/devsite/site-cloud/en/blog/big-data/feed.xml" \
"googledata/devsite/site-cloud/en/blog/big-data/archive/2017.html" \
"googledata/devsite/site-cloud/en/blog/big-data/2017/06/guide-to-common-cloud-dataflow-use-case-patterns-part-1.html" \
"googledata/devsite/site-cloud/blog/uploads/149756210681386/dataflow-patterns-2.png" \
"googledata/devsite/site-cloud/blog/uploads/149756210681386/dataflow-patterns-5.png" \
"googledata/devsite/site-cloud/blog/uploads/149756210681386/dataflow-patterns-1.png" \
"googledata/devsite/site-cloud/blog/uploads/149756210681386/dataflow-patterns-6.png" \
"googledata/devsite/site-cloud/blog/uploads/149756210681386/dataflow-patterns-3.png"