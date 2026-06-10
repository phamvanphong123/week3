def selection_sort(array, n):
    for index in range(n):

        min_index = index

        for j in range(index + 1, n):

            # tìm phần tử nhỏ nhất
            if array[j] < array[min_index]:
                min_index = j

        # hoán đổi sau khi tìm xong
        array[index], array[min_index] = array[min_index], array[index]


arr = [-25, 40, 0, 15, -90, 80, -92, -210, 747, 500, 1050, 999]

n = len(arr)

selection_sort(arr, n)

print("Array sau khi sắp xếp:")
print(arr)