# Võ Tá Cường , MSV: 245752021610100
# sortmodule.py
# Module chứa hàm bubble sort

def bubbleSort(nlist):
    """
    Sắp xếp danh sách nlist theo thứ tự tăng dần bằng thuật toán Bubble Sort
    """
    loop = len(nlist)
    for i in range(loop):
        swapped = False
        for j in range(0, loop - i - 1):  # Lưu ý tránh vượt quá index
            if nlist[j] > nlist[j+1]:
                # Trao đổi hai phần tử
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không có phần tử nào bị tráo đổi → mảng đã sắp xếp
        if not swapped:
            break
    return nlist
