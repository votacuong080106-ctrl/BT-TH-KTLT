# Võ Tá Cường , MSV: 245752021610100
# searchmodule.py
# Module chứa hàm tìm kiếm nhị phân

def binary_search(lst, value):
    """
    Tìm kiếm nhị phân value trong danh sách lst đã sắp xếp.
    Trả về True nếu tìm thấy, False nếu không.
    """
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1
    return False
