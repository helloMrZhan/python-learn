# 对 sqlite3 做一个基本的封装，支持 open/close，打开的时候配置检查后续操作在同一个线程

import logging
import sqlite3
from error_code import ErrorCode
logger = logging.Logger(__name__)

class SqliteConnector():
    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.conn = None

    def open(self):
        try:
            self.conn = sqlite3.connect(self.db_file, check_same_thread=True)
            return {"err": ErrorCode.SUCCESS}
        except Exception as e:
            logger.error('open sqlite exception:', str(e))
            self.close()
            return {"err": ErrorCode.DB_OPEN_FAILED}

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        return {'err': ErrorCode.SUCCESS}


if __name__ == '__main__':
    kv = SqliteConnector("/tmp/test.db")

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS