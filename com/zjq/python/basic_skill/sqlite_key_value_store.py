# 使用 SQLITE 实现一个 key-value(string:json) 读写库，请先完成【Python SQLITE Connector】和【Python SQLITE Connection】

# -*- coding: UTF-8 -*-
import logging
import json
from error_code import ErrorCode
from sqlite_connection import SqliteConnection
logger = logging.Logger(__name__)

class SqliteKeyValueStore(SqliteConnection):
    def __init__(self, db_file) -> None:
        super().__init__(db_file)

    def open(self):
        ret = super().open()
        if ret['err'] != ErrorCode.SUCCESS:
            return ret

        sql = '''create table if not exists key_value (
            _key varchar(32) primary key not null,
            value text not null
        );'''
        return self.execute(sql)

    # TODO(You): 请在此实现Sqlite写入key-value代码，其中value是json
    def set(self, key, value):
        if self.conn is None:
            return {'err': ErrorCode.DB_OPEN_FAILED}

        try:
            value = json.dumps(value)
            sql = 'insert or replace into key_value values(?, ?)'
            return self.execute(sql, [key, value])
        except Exception as e:
            logger.error(f'set key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}

    def get(self, key):
        if self.conn is None:
            return {'err': ErrorCode.SQLITE_NOT_OPEN}

        try:
            sql = 'select value from key_value where _key=?'
            ret = self.execute(sql, [key])
            if ret['err'] != ErrorCode.SUCCESS:
                return ret

            results = ret['results']
            if len(results) == 0:
                return {"err": ErrorCode.NOT_FOUND}
            else:
                value = json.loads(results[0][0])
                return {"err": ErrorCode.SUCCESS, "key": key, "value": value}
        except Exception as e:
            logger.error(f'get key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


if __name__ == '__main__':
    kv = SqliteKeyValueStore("/tmp/test.db")

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