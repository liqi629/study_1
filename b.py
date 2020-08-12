from faker import Faker
f = Faker('zh_CN')
print(f.name())
print( f.date_time())
# print("date_time: " + f.time_object())
# print("date_time: " + f.time())