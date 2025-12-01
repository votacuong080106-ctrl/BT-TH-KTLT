# Võ Tá Cường , MSV: 245752021610100
def get_sum(*num):
    tmp = 0
    # duyệt các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
