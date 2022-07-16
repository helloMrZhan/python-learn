from com.zjq.python.base.classuse.KeyValueSet import KeyValueSet

class HashKeyValueSet(KeyValueSet):
    def __init__(self) -> None:
        super().__init__()

    def hset(self, hash_key, key, value):
        self.set(hash_key, {key: value})

    def hget(self, hash_key, key):
        hash_set = self.get(hash_key)
        if hash_set is None:
            return None
        else:
            return hash_set.get(key)

    def hkeys(self, hash_key):
        hash_set = self.get(hash_key)
        if hash_set is None:
            return []
        else:
            return hash_set.keys()

if __name__ == '__main__':
    from com.zjq.python.base.classuse.HashKeyValueSet import HashKeyValueSet
    hashset = HashKeyValueSet()

    hashset.hset('puzzle', 'hello', 'world!')
    hashset.hset('puzzle', 'monkey', 'king!')
    hashset.hset('puzzle', 'tomorrow', 'is another day')
    hashset.hset('puzzle', 'good', 'bye!')

    keys = hashset.hkeys('puzzle')
    for key in keys:
        ret = input("猜一猜下半句是什么？ {} -> :".format(key))
        value = hashset.hget('puzzle', key)
        if ret == value:
            print('你太厉害了，这都能猜得到！')
        else:
            print('哈哈，肯定猜不到得啦：{}->{}'.format(key, value))