# 继承自SqliteConnector，增加执行sql接口，请先完成【Python SQLITE Connector】

import logging
from error_code import ErrorCode
from sqlite_connector import SqliteConnector
logger = logging.Logger(__name__)

class SqliteConnection(SqliteConnector):
    def __init__(self, db_file) -> None:
        super().__init__(db_file)

    # 在此实现查询代码
    def execute(self, sql, arg=None):
        results = []
        try:
            cursor = self.conn.execute(sql, arg or tuple())
            if cursor is not None:
                results = cursor.fetchall()
            self.conn.commit()
            return {'err': ErrorCode.SUCCESS, 'results': results}
        except Exception as e:
            logger.error(
                f'execute sql exception, sql:{sql}, arg:{arg}, exception:{str(e)}')
            self.conn.rollback()
            return {'err': ErrorCode.DB_QUERY_EXCEPT, 'results': results}


if __name__ == '__main__':
    kv = SqliteConnection("/tmp/test.db")

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    sql = '''create table if not exists key_value (
        _key varchar(32) primary key not null,
        value text not null
    );'''
    ret = kv.execute(sql)
    assert ret['err'] == ErrorCode.SUCCESS
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS