# Võ Tá Cường , MSV: 245752021610100
n = int(input("Nhập n: "))

# Tạo và in tam giác Pascal
triangle = []

for i in range(n):
    row = [1] * (i + 1)   # Tạo dòng toàn số 1
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]  # Tính các giá trị bên trong
    triangle.append(row)
    print(row)

