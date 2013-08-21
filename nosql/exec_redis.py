import sys
import redis

# Tested against Redis 2.6.14

class RedisTest(object):
	"""Tests Redis."""

	def __init__(self, redis_client):
		self._redis_client = redis_client

	def execSet(self, count):
		for i in xrange(0, count):
			self._redis_client.set(i, i + 1)
	
	def execGet(self, count):
		x = 1
		for i in xrange(0, count):
			x = self._redis_client.get(i)

	def execDictSet(self, count, hname='test_hash'):
		for i in xrange(0, count):
			self._redis_client.hset(hname, i, i + 1)

	def execDictGet(self, count, hname='test_hash'):
		x = 1
		for i in xrange(0, count):
			x = self._redis_client.hget(hname, i)

	def execSetAdd(self, count, set_name='test_set'):
		for i in xrange(0, count):
			self._redis_client.sadd(set_name, i)

	def execSetRem(self, count, set_name='test_set'):
		for i in xrange(0, count):
			x = self._redis_client.srem(set_name, i)

	def execListPush(self, count, list_name='test_list'):
		for i in xrange(0, count):
			self._redis_client.lpush(list_name, i)

	def execListPop(self, count, list_name='test_list'):
		x = 0
		for i in xrange(0, count):
			x = self._redis_client.lpop(list_name)


def main():
	redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
	redis_test = RedisTest(redis_client)
	count  = 1000* 1000
	print 'Testing with %d objects' % count
	assert sys.argv >= 2, 'Please pass set or get as second argument.'
	if sys.argv[1] == 'set':
		redis_test.execSet(count)
	elif sys.argv[1] == 'get':
		redis_test.execGet(count)
	elif sys.argv[1] == 'dict_set':
		redis_test.execDictSet(count)
	elif sys.argv[1] == 'dict_get':
		redis_test.execDictGet(count)
	elif sys.argv[1] == 'set_add':
		redis_test.execSetAdd(count)
	elif sys.argv[1] == 'set_rem':
		redis_test.execSetRem(count)
	elif sys.argv[1] == 'list_push':
		redis_test.execListPush(count)
	elif sys.argv[1] == 'list_pop':
		redis_test.execListPop(count)
	else:
		print 'ERROR: incorrect option specified.'

if __name__ == '__main__':
	main()
