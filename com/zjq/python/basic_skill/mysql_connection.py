# 封装一个 MySQL 连接类，继承自 MySQLConnector，请先完成【Python MySQL Connector】

# -*- coding: UTF-8 -*-
import logging
from error_code import ErrorCode
from mysql.connector import Error
from mysql_connector import MySQLConnector
logger = logging.Logger(__name__)
mysql_connection_pool = None

class MySQLConnection(MySQLConnector):
    def __init__(self, host, port, user, password, database) -> None:
        super().__init__(host, port, user, password, database)

    def execute(self, sql, args):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, args)
            results = cursor.fetchall() or []
            self.conn.commit()
            return {
                'err': ErrorCode.SUCCESS,
                'results': list(map(lambda t: t[0], results))
            }
        except Error as e:
            self.conn.rollback()
            logger.error('execute mysql query exception:', str(e))
            return {'err': ErrorCode.DB_QUERY_EXCEPT}
        finally:
            cursor.close()

if __name__ == '__main__':
    kv = MySQLConnection(
        "127.0.0.1", 3306,
        "root", "WNpx8c\zr!fF",
        "test"
    )

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.execute("select * from test")
    assert ret['err'] == ErrorCode.SUCCESS
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS