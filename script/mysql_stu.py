# _*_ coding: utf-8 _*_

import pymysql
import importlib
import smtplib
import sys
import subprocess
import os
import random
from faker import Faker
from random import choice
from string import ascii_uppercase as uc, digits as dg
importlib.reload(sys)
# sys.setdefaultencoding('utf-8')





f = Faker(locale='zh_cn')
# name_m = f.name()
# # 性别0 1  男女
# gender = random.randint(0,1)
# addres = f.address()
# print(f.date_time())
# print(f.phone_number())
# print(f.country())
# print(f.province())

# print(f.password(special_chars = False, digits = False, upper_case=True, lower_case=True))


'''
CREATE TABLE `sms_code_10` (
`id` INT(10) NOT NULL AUTO_INCREMENT,
`code` VARCHAR(50) NOT NULL COMMENT '内部邀请码',
`type` INT(10) NOT NULL DEFAULT '1' COMMENT '1未使用2已使用3已过期',
`status` INT(10) NOT NULL DEFAULT '1' COMMENT '1：有效，0删除',
`update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
`created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '当前时间',
PRIMARY KEY (`id`),
INDEX `code` (`code`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1;
'''

databaseName = 'qc'
host = '172.16.161.119'
port = '3306'
userName = 'root'
password = 'root'


def openConn(hostStr, userStr, passwordStr, tableSchema):
    try:
        conn = pymysql.connect(host ='%s' %(hostStr), user ='%s' %(userStr), passwd = '%s' %(passwordStr), db ='%s' %(tableSchema), port = 3306, charset = 'utf8', use_unicode = 'True')
        return conn
    except Exception as e:
        print (str(e))
    
def execSql(conn, sql):
    try:
        cursor = conn.cursor()
        cnt = cursor.execute(sql)
        conn.commit()
        return cnt
    except Exception as e:
        print(e)
        pass
    finally:
        try:
            cursor.close()
        except:
            pass
    return -1

# range 数量 修改 调整 整体数据条数

def sendMail():
    conn = openConn(host, userName, password, databaseName)
    for j in range(10):
        print(j)
        # sql = """INSERT INTO asd (`name`,`address`,`time`) VALUES""";
        for i in range(1):
            # part3 = ''.join(f.name())
            # part4 = ''.join(f.address())
            # part5 = ''.join(str(f.date_time()))
            #
            # sql=sql+"('"+part3+"', '"+part4+"', '"+part5+"')"
            if(i<10):
                # sql=sql+","  #多个sql，使用逗号隔开。20000个一组，一起执行
                # sql1 = """INSERT INTO asd (`name`, `address`, `time`) VALUES('{}', '{}', '{}')""".format(f.name(), f.address(), str(f.date_time()));
                sql1 = """INSERT INTO big_chaifen (`name`, `address`, `company`, `email`, `phone`, `country`, `password`, `date_time`) 
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format\
                    (f.name(), f.address(), f.company(), f.email(), f.phone_number(), Faker().country(),
                     f.password(special_chars = False, digits = True, upper_case=True, lower_case=True), str(f.date_time()));

                # print(sql1)
                execSql(conn, sql1)

# sql =''
# for j in range(10):
#     print(j)
#     sql = """INSERT INTO stu_100w (`name`,`gender`) VALUES('{}',{})""".format(f.name(), random.randint(0, 1));
#     sql = sql+","
# print(sql)

def main():
    sendMail()
main()