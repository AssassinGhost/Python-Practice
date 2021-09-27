#Python program to reverse the array using iterations
def reverse_array (array1, start, end):
    while (start<=end):
        array1[start], array1[end] = array1[end], array1[start]
        start += 1
        end -= 1

A = [1, 2, 2 , 3, 4]
start=0
end= len(A) -1
print(A)
print("The reversed Array is: ")
reverse_array(A, start, end)
print(A)
