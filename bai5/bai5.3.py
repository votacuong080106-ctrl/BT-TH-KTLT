# Võ Tá Cường , MSV: 245752021610100
# Định nghĩa class cha
class Nguoi(object):
    def getGender(self):
        return "Unknown"

# Class con Nam kế thừa từ Nguoi
class Nam(Nguoi):
    def getGender(self):
        return "Nam"

# Class con Nu kế thừa từ Nguoi
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng
aNam = Nam()
aNu = Nu()

# Gọi phương thức getGender
print(aNam.getGender())  # In ra: Nam
print(aNu.getGender())   # In ra: Nữ
