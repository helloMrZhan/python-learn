# 封装一个 MySQL 的连接器，支持 open/close

# -*- coding: UTF-8 -*-
import logging
from error_code import ErrorCode
from mysql.connector import pooling
from mysql.connector import Error
logger = logging.Logger(__name__)
mysql_connection_pool = None

class MySQLConnector():
    def __init__(self, host, port, user, password, database) -> None:
        global mysql_connection_pool
        if mysql_connection_pool is None:
            mysql_connection_pool = pooling.MySQLConnectionPool(
                pool_name="some_pool_name",
                pool_size=10,
                pool_reset_session=True,
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )

        self.conn = None


    def open(self):
        try:
            self.conn = mysql_connection_pool.get_connection()
            if self.conn.is_connected():
                db_Info = self.conn.get_server_info()
                print("db info: ", db_Info)
                return {"err": ErrorCode.SUCCESS}
            else:
                self.conn = None
                logger.error('open mysql connection failed, can not connect:')
                return {"err": ErrorCode.DB_OPEN_FAILED}
        except Error as e:
            logger.error('open mysql connection exception:', str(e))
            self.close()
            return {"err": ErrorCode.DB_OPEN_FAILED}

    def close(self):
        if self.conn is not None:
            if self.conn.is_connected():
                self.conn.close()
            self.conn = None
        return {'err': ErrorCode.SUCCESS}

if __name__ == '__main__':
    kv = MySQLConnector(
        "127.0.0.1", 3306,
        "root", "WNpx8c\zr!fF",
        "test"
    )

    ret = kv.open()
    if ret['err'] == ErrorCode.SUCCESS:
        print("数据库打开成功")
        kv.close()