# _*_ coding: utf-8 _*_

import pymysql
import importlib
import smtplib
import sys
import subprocess
import os
from random import choice
from string import ascii_uppercase as uc, digits as dg
importlib.reload(sys)
# sys.setdefaultencoding('utf-8')


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

databaseName = 'sakila'
host = '172.16.161.128'
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
    for j in range(75):
        print(j)
        sql="""INSERT INTO `sms_code_150` (`code`) VALUES """;
        for i in range(20000):
            part3 = ''.join(choice(dg + uc) for j in range(6)) 
            sql=sql+"('"+part3+"')"
            if(i<19999):
                sql=sql+","  #多个sql，使用逗号隔开。20000个一组，一起执行
        execSql(conn, sql)

    

def main():
    sendMail()
main()