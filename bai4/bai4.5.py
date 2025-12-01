# Võ Tá Cường , MSV: 245752021610100
# Module mylistmodule.py
# Chứa các hàm sắp xếp và tìm phần tử lớn nhất

def sort_list(lst):
    """Sắp xếp danh sách theo thứ tự tăng dần"""
    return sorted(lst)

def max_element(lst):
    """Trả về phần tử lớn nhất"""
    if not lst:
        return None
    return max(lst)
