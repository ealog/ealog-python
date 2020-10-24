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
    def __repr__(self) ->str:
        return "auto_id:%s meter_value: %s get_date: %s get_date_time: %s get_date_stamp: %s meter_addr: %s" %(self.auto_id,self.meter_value,self.get_date,self.get_date_time,
        self.get_date_stamp,self.meter_addr)

def main():
    engine = sqlalchemy.create_engine(MYSQL_URL,encoding="UTF8",echo=True)
    sqlalchemy.orm.session.Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = sqlalchemy.orm.session.Session()
    meters_data = session.query(Meters_data).get(500)
    print(meters_data)
    session.commit()
    session.close()
if __name__ == "__main__":
    main()