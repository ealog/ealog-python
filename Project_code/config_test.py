import configparser

conf=configparser.ConfigParser()

conf.read('config.ini')

print(conf.get('SECTION1','age'))
print(conf.get('SECTION2','sex'))
