import configparser

conf=configparser.ConfigParser()

conf.read('config.ini',encoding='utf-8')


dic=conf._sections

# for i in dic:
#     dic[i]=dict(dic[i])
didi = dic['METER_PORT_ADDR']

print(dic['METER_PORT_ADDR'])

baudrate = conf.getint('METER_INIT','baudrate')

timeout = conf.getint('METER_INIT','timeout')
ip_addr =conf.get('DATABASE_IP','ip_addr')
print(baudrate,timeout,ip_addr)

print(type(didi))

