import datetime
import time


class A:
    
    

    def aa(self,num):
        print("a",num)

class B:
    def bb(self):
        print("b")



inst = A()

inst1 =B()

inst2 =A()

inst3 =B()

inst.aa(1)

inst1.bb()

inst2.aa(2)

inst3.bb()


inst00 = [inst,inst2]


for inst0 in inst00:
    print(inst0)


# import datetime

# # device1 = 1

# # device2 = 2

# # imp1 = 100

# # imp2 = 200


# # for n in range(1,11):
# #     print(n)

# # increase = {1:0,2:0}



# # print("value is :",increase[device1])
# # today = datetime.date.today()
# # quarter = (today.month-1) // 3 + 1
# # dayOfWeek = datetime.datetime.now().isoweekday()
# # year_quarter='{}Q{}'.format(today.year, quarter)
# # week_count=datetime.datetime.now().isocalendar()[1]
# # print(today)

# # print(quarter)

# # print(year_quarter)

# # print(dayOfWeek)

# # print(week_count)
# import time

# minute_lists = [0,5,10,15,20,25,30,35,40,45,50,55]
# cur_time_minute = datetime.datetime.now().minute
# cur_time_second = datetime.datetime.now().second

# for minute_list in minute_lists:

#     if cur_time_minute % 5 == 0:
#         sleep_time=0
#         print("0",sleep_time)
#     elif cur_time_minute < minute_list and minute_list - cur_time_minute < 5:
#         sleep_time = (minute_list-cur_time_minute)*60 - cur_time_second
#         print("5",sleep_time)
#     elif cur_time_minute > 55:
#         sleep_time = (60-cur_time_minute)*60 - cur_time_second
#         print("55",sleep_time)
# time.sleep(sleep_time)