import java.util.Scanner;

public class HeapProp {
	public static void main(String args[]){
		int n;
		Scanner cin = new Scanner(System.in);
		System.out.println("How many numbers?\n");
		n = cin.nextInt();
		int[] arr = new int[n];
		System.out.println("Enter the numbers:");
		for(int i=0;i<n;i++){
			arr[i] = cin.nextInt();
		}

		new HeapProp().heapSort(arr,n);


	}
	public void heapSort(int arr[],int n){
		buildMaxHeap(arr,n);
		int temp;
		for(int i=n-1;i>0;i--){
			temp = arr[0];
			arr[0] = arr[i];
			arr[i] = temp;
			maxHeapify(arr,0, i);
		}
		System.out.println("Result:");
		for(int j=0;j<n;j++){
			System.out.println(arr[j]);
		}
	}

	public void buildMaxHeap(int arr[], int n){
		for(int i=n/2;i>=0;i--){
			maxHeapify(arr,i,n);
		}
	}
	public void maxHeapify(int arr[], int i, int n){
		int left = (2*i)+1;
		int right = (2*i)+2;
		int largest = 0, temp;
		if(left<n && arr[i]<arr[left]){
				largest = left;
		}
		else{
			largest = i;
		}
		if(right<n && arr[largest]<arr[right]){
			largest = right;
		}
		if(i!=largest){
			temp = arr[largest];
			arr[largest] = arr[i];
			arr[i] = temp;
			maxHeapify(arr,largest,n);
		}

	}
}