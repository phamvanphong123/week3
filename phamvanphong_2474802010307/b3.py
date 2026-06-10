#selection sort 
import sys
# selection sort

arr = [140, 25, 15, 52, 10, 250, 55]

for i in range(len(arr)):
    # tìm vị trí phần tử nhỏ nhất
    min = i

    for j in range(i + 1, len(arr)):
        if arr[min] > arr[j]:
            min = j

    # đổi chỗ sau khi đã tìm xong phần tử nhỏ nhất
    arr[i], arr[min] = arr[min], arr[i]

print("sorted array", arr)
for i in range(len(arr)):
    print("%d"%arr[i])
