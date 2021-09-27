#Python program to reverse the array using Recursive function
def reverse_array(A, start, end):
    if(start>=end):
        return
    A[start], A[end] = A[end], A[start]
    reverse_array(A, start + 1, end - 1)

A = [1, 2, 3, 4, 5]
start = 0
end = len(A) -1 
print(A)
print("The reversed Array is: ")
reverse_array(A, start, end)
print(A)
