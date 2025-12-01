# Võ Tá Cường , MSV: 245752021610100
# searchmodule.py
# Module chứa hàm tìm kiếm tuyến tính

def Sequential_Search(dlist, item):
    """
    Tìm kiếm tuyến tính item trong danh sách dlist.
    Trả về tuple (True/False, index nếu tìm thấy)
    """
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)
