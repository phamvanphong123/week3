# insertion sort

def insertion_s(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Dịch chuyển các phần tử lớn hơn key sang phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Mảng ban đầu
arr = [12, 31, 130, 15, 18, 150, 30]

# Gọi hàm sắp xếp
insertion_s(arr)

# In kết quả
for i in range(len(arr)):
    print(arr[i])