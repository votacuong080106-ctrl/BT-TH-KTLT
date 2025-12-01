# Võ Tá Cường , MSV: 245752021610100
import datetime as dt

# Định dạng ngày giờ
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In thông tin ngày, tháng, phút, giây
print('Day:', t1.day)
print('Month:', t1.month)
print('Minute:', t1.minute)
print('Second:', t1.second)

# Lấy thời gian hiện tại
t2 = dt.datetime.now()

# Tính hiệu giữa hai thời điểm
diff = t2 - t1

# In số ngày chênh lệch
print('How many days difference?', diff.days)
