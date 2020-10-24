
import time

tuple1 = ((1,2,3),(4,5,6),(7,8,9))

print(tuple1[0][0])
for tuple_t1 in tuple1:
    print(tuple_t1[0])


tuple2 = ((1,100,'x111'),(2,200,'x111'),(3,300,'x111'))
print(tuple2)
for tuple_t2 in tuple2:
    print(tuple_t2[1])

tuple3 = ((1,2,3),(100,200,300),('x111','x111','x111'))
print(tuple3)

for tuple_t3 in tuple3:
    print(tuple_t3[0])

meter_value = 400
meter_addr = "x----1"

data_list = []

data_list.append(("%d,%s")%(meter_value,meter_addr))

print(data_list)


date = time.strftime("%Y-%m-%d",time.localtime())

date_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(date,date_time)