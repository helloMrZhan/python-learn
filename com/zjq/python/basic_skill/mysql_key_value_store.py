# 使用 MySQL 实现一个 key-value(string:json) 读写库，请先完成【Python MySQL 安装说明】、【Python MySQL Connector】和【Python MySQL Connection】

import logging
import json
from error_code import ErrorCode
from mysql_connection import MySQLConnection
logger = logging.Logger(__name__)
mysql_connection_pool = None

class MySQLKeyValueStore(MySQLConnection):
    def __init__(self, host, port, user, password, database) -> None:
        super().__init__(host, port, user, password, database)

    def set(self, key, value):
        if self.conn is None:
            return {'err': ErrorCode.DB_OPEN_FAILED}

        try:
            value = json.dumps(value)
            sql = 'insert into key_value set _key=%s, value=%s on duplicate key update value=%s'
            args = (key, value, value)
            return self.execute(sql, args)
        except Exception as e:
            logger.error(f'set key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


    def get(self, key):
        if self.conn is None:
            return {'err': ErrorCode.DB_NOT_OPEN}

        try:
            sql = 'select value from key_value where _key=%s'
            ret = self.execute(sql, (key,))
            if ret['err'] != ErrorCode.SUCCESS:
                return ret
            results = ret['results']
            if len(results) == 0:
                logger.warning(f'get key:{key}, empty.')
                return {"err": ErrorCode.NOT_FOUND}
            else:
                return {"err": ErrorCode.SUCCESS, "key": key, "value": json.loads(results[0])}
        except Exception as e:
            logger.error(f'get key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


if __name__ == '__main__':
    kv = MySQLKeyValueStore(
        "127.0.0.1", 3306,
        "root", "WNpx8c\zr!fF",
        "test"
    )

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.set('test', {"number": 0})
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.get('test')
    print(ret)
    assert ret['err'] == ErrorCode.SUCCESS
    assert ret['value']['number'] == 0
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS