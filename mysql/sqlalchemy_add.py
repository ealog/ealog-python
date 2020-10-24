#coding:utf-8
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import sqlalchemy.orm.session
import time

MYSQL_URL = "mysql+mysqlconnector://root:windows12@192.168.3.31:3306/prod_energy"


class Meters_data(sqlalchemy.ext.declarative.declarative_base()):
    __tablename__ = "meters_data"
    auto_id = sqlalchemy.Column(sqlalchemy.INT,primary_key=True)
    meter_value = sqlalchemy.Column(sqlalchemy.INT)
    get_date = sqlalchemy.Column(sqlalchemy.Date)
    get_date_time = sqlalchemy.Column(sqlalchemy.DateTime)
    get_date_stamp = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    meter_addr = sqlalchemy.Column(sqlalchemy.VARCHAR)
    


def main():
    engine = sqlalchemy.create_engine(MYSQL_URL,encoding="UTF8",echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = sqlalchemy.orm.session.Session()
    date = time.strftime("%Y-%m-%d",time.localtime())
    date_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    meters_data = Meters_data(meter_value=500,get_date=date,get_date_time=date_time,get_date_stamp=date_time,meter_addr="x9999")
    session.add(meters_data)
    session.commit()
    print("data add success,current id is :%s" % meters_data.auto_id)
    session.close()
if __name__ == "__main__":
    main()