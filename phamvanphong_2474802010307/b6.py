arr = ["Phong", "An", "Tuan", "Binh", "Huy", "Khanh"]

n = len(arr)

for i in range(n - 1):
    min_index = i

    # Tìm chuỗi nhỏ nhất theo thứ tự từ điển
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Hoán đổi
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Mảng sau khi sắp xếp:")
for x in arr:
    print(x)