class sorting:
    def quick_sort(self,A):
        self.quick_sort2(A,0,len(A)-1)

    def quick_sort2(self,A,low,high):
        if low < high:
            self.P = self.partition(A,low,high)
            self.quick_sort2(A,low,self.P-1)
            self.quick_sort2(A,self.P+1,high)
            
    def get_pivot(self,A,low,high):
        middle =low+high//2
        pivot = high
        if A[low]<A[middle]:
            if A[middle]<A[high]:
                pivot = middle
        elif A[low] > A[middle]:
            pivot = low
        return pivot

    def partition(self,A,low,high):
        pivot_index = self.get_pivot(A,low,high)
        pivot_value = A[pivot_index]
        A[pivot_index],A[low]=A[low],A[pivot_index]
        border =low
        for i in range(low,high+1):
            if A[i] < pivot_value:
                border = border+1
                A[i],A[border] =A[border],A[i]
        A[low],A[border]=A[border],A[low]
        return border

a =sorting()
mylist =[17,4,8,3,11,2,22,6]
a.quick_sort(mylist)

        
    
        
