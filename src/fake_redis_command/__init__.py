import random
from faker.providers import BaseProvider


class Provider(BaseProvider):
    from faker import Faker
    from faker.providers import internet, geo, date_time, ssn, address, phone_number, company, currency
    f = Faker()
    f.add_provider(internet)  # f.ipv4_private()
    f.add_provider(date_time)  # str(f.date_time())
    f.add_provider(ssn)  # str(f.date_time())
    f.add_provider(address)  # address country
    f.add_provider(currency)  # currency_name
    f.add_provider(company)  # catch_phrase()
    f.add_provider(geo)
    f.add_provider(phone_number)  # phone_number

    def __init__(self, nothing):
        self._cmd = [self.append, self.bitcount, self.bitop, self.bitpos, self.set, self.setbit, self.setex, self.setnx, self.setrange, self.strlen, self.substr,
                     #'bitfield','blpop', 'brpop', 'brpoplpush', 'bzpopmax', 'bzpopmin',
                     self.decr, self.decrby, self.expire, self.expireat,
                     self.geoadd, self.geodist, self.geohash, self.geopos, self.georadius, self.georadiusbymember,
                     self.get, self.getbit, self.getrange, self.getset,
                     self.hdel, self.hexists, self.hget, self.hgetall, self.hincrby, self.hincrbyfloat, self.hkeys, self.hlen, self.hmget, self.hmset, self.hset, self.hsetnx, self.hstrlen, self.hvals,
                     self.incr, self.incrby, self.incrbyfloat,
                     self.lindex, self.linsert, self.llen, self.lpop, self.lpush, self.lpushx, self.lrange, self.lrem, self.lset, self.ltrim, self.rpop, self.rpoplpush, self.rpush, self.rpushx,
                     self.mget, self.mset, self.msetnx, self.psetex,
                     self.persist, self.pexpire, self.pexpireat, self.pfadd, self.pfcount, self.pfmerge,
                     #'publish', 'pubsub',
                     self.sadd, self.scard, self.sdiff, self.sdiffstore,  self.sinter, self.sinterstore, self.sismember, self.smembers, self.smove, self.spop, self.srandmember, self.srem, self.sunion, self.sunionstore,
                     self.ttl, self.pttl,
                     self.xack, self.xadd, self.xclaim, self.xdel, self.xlen, self.xrange, self.xread, self.xrevrange, self.xtrim, self.xreadgroup, self.xpending,
                     self.xgroup_create, self.xgroup_delconsumer, self.xgroup_destroy,  # self.xgroup_setid,
                     self.xinfo_consumers, self.xinfo_groups, self.xinfo_stream,
                     self.zadd, self.zcard, self.zcount, self.zincrby, self.zlexcount, self.zpopmax, self.zpopmin, self.zrange, self.zrangebylex, self.zrangebyscore, self.zrank, self.zrem, self.zremrangebylex,
                     self.zremrangebyrank, self.zremrangebyscore, self.zrevrange, self.zrevrangebylex, self.zrevrangebyscore, self.zrevrank,  self.zscore, self.zunionstore, self.zinterstore,
                     ]

    def size(self):
        return len(self._cmd)
    '''fake helper begins..'''

    def _text(self):
        s = '"' + self.f.text() + '"'
        s = s.replace('\n', ' ')
        return s

    def _random_int(self):
        return self.f.random_int()

    def _data_time(self):
        return '"' + str(self.f.date_time()) + '"'

    def _fake_name(self):
        return '"' + self.f.name() + '"'

    def _fake_inner_ip(self):
        return self.f.ipv4_private()

    def _fake_latitude(self):
        return self.f.latitude()

    def _fake_longitude(self):
        return self.f.longitude()

    def _fake_coordinate(self):
        return self.f.coordinate()

    def _fake_address(self):
        s = self.f.address().replace('\n', ' ')
        return '"' + s + '"'

    def _random_bigint(self):
        return self.f.random_int(18446744073709551615, 18446744073709551615000000)

    def _random_smallint(self):
        begin = [-100, -50, -20, -5, -1, 0]
        end = [100, 50, 20, 5, 1, 0]
        return self.f.random_int(random.choice(begin), random.choice(end))

    def _random_01(self):
        return self.f.random_int(0, 1)

    def _lexify(self):
        return self.f.lexify()

    def _random_double(self):
        return random.uniform(self._random_int(), self._random_int())

    def _random_element(self):
        return self.f.random_element()

    def _fake_ssn(self):
        return self.f.ssn()

    def _random_string(self):
        meta = [self._fake_ssn, self._random_double, self._lexify, self._fake_address,
                self._random_bigint, self._data_time, self._fake_name, self._text, self._random_01, self._random_int
                ]
        s = '{}'.format((random.choice(meta))())
        return s

    def stream_id(self):
        """Returns random stream id."""

        ts = self.f.random_int(0, 18446744073709551615)
        seq = self.f.random_int(0, 18446744073709551615)
        return str(ts) + '-' + str(seq)

    def random_command(self):
        """random entry."""
        return (random.choice(self._cmd))()

    '''fake command implement, should not use directly'''

    def xadd(self):
        meta = ['xadd {} {} {} {}'.format(self._text(), self.stream_id(), self._random_double(), self._random_int()),
                'xadd {} {} {} {} {} {}'.format(self._data_time(), self.stream_id(
                ), self._random_double(), self._data_time(), self._random_double(), self._random_int()),
                'xadd {} {} {} {} {} {} {} {}'.format(self._fake_inner_ip(), self.stream_id(), self._random_double(), self._fake_inner_ip(),
                                                      self._random_double(), self._text(), self._random_double(), self._data_time()),
                'xadd {} {} {} {} {} {} {} {} {} {}'.format(self._fake_name(), self.stream_id(), self._random_double(), self._random_int(),
                                                            self._random_double(), self.stream_id(), self._random_double(), self._fake_ssn(), self._random_double(), self._random_bigint()),
                'xadd {} {} {} {} {} {} {} {} {} {} {} {}'.format(self._random_int(), self.stream_id(), self._random_double(), self._fake_name(),
                                                                  self._random_double(), self._fake_address(), self._random_double(),
                                                                  self._fake_ssn(), self._random_double(), self._random_element(), self._lexify(), self._random_01()),
                ]
        return random.choice(meta)

    def xack(self):
        meta = ['xack {} {} {}'.format(self._text(), self._text(), self.stream_id()),
                'xack {} {} {}'.format(self._random_string(
                ), self._random_string(), self.stream_id()),
                ]
        return random.choice(meta)

    def xgroup_create(self):
        meta = ['xgroup create {} {} {}'.format(self._random_string(), self._random_string(), self.stream_id()),
                'xgroup create {} {} $'.format(
                    self._random_string(), self._random_string()),
                ]
        return random.choice(meta)

    def xgroup_setid(self):
        meta = ['xgroup setid {} {} {}'.format(self._random_string(), self._random_string(), self.stream_id()),
                'xgroup setid {} {} $'.format(
                    self._random_string(), self._random_string()),
                ]
        return random.choice(meta)

    def xgroup_delconsumer(self):
        return 'xgroup delconsumer {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def xgroup_destroy(self):
        return 'xgroup destroy {} {}'.format(self._random_string(), self._random_string())

    def xinfo_consumers(self):
        return 'xinfo consumers {} {}'.format(self._random_string(), self._random_string())

    def xinfo_groups(self):
        return 'xinfo groups {}'.format(self._random_string())

    def xinfo_stream(self):
        return 'xinfo stream {}'.format(self._random_string())

    def xclaim(self):
        return 'xack {} {} {} {} {}'.format(self._random_string(), self._random_string(), self._fake_name(), self._random_int(), self.stream_id())

    def xpending(self):
        meta = ['xpending {} {}'.format(self._text(), self._text()),
                'xpending {} {} {} {} {}'.format(self._data_time(), self._data_time(
                ), self.stream_id(), self.stream_id(), self._random_smallint()),
                'xpending {} {} - + {}'.format(self._fake_inner_ip(),
                                               self._random_string(), self._random_int()),
                'xpending {} {} - + {} {}'.format(self._random_string(
                ), self._fake_name(), self._random_int(), self._random_string()),
                ]
        return random.choice(meta)

    def xread(self):
        """NOTE.

        no block
        """
        meta = [
            'xread count {} streams {} {} {} {}'.format(self._random_smallint(
            ), self._fake_name(), self._random_string(), self.stream_id(), self.stream_id()),
            'xread count {} streams {} {}'.format(
                self._random_smallint(), self._random_string(), self.stream_id()),
        ]
        return random.choice(meta)

    def xreadgroup(self):
        """NOTE.

        no block
        """
        meta = [
            'xreadgroup group {} {} count {} streams {} {} {} {}'.format(self._random_string(), self._fake_name(), self._random_smallint(),
                                                                         self._random_string(), self._random_string(), self.stream_id(), self.stream_id()),
            'xreadgroup group {} count {} streams {} {}'.format(self._random_string(
            ), self._random_smallint(), self._random_string(), self.stream_id()),
        ]
        return random.choice(meta)

    def zincrby(self):
        return 'zincrby {} {} {}'.format(self._random_string(), self._random_int(), self._random_string())

    def zscore(self):
        return 'zscore {} {}'.format(self._random_string(), self._random_string())

    def zadd(self):
        meta = ['zadd {} {} {}'.format(self._text(), self._random_double(), self._random_int()),
                'zadd {} {} {} {} {}'.format(self._data_time(), self._random_double(
                ), self._data_time(), self._random_double(), self._random_int()),
                'zadd {} {} {} {} {} {} {}'.format(self._fake_inner_ip(), self._random_double(), self._fake_inner_ip(),
                                                   self._random_double(), self._text(), self._random_double(), self._data_time()),
                'zadd {} {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._random_double(), self._random_int(),
                                                         self._random_double(), self.stream_id(), self._random_double(), self._fake_ssn(), self._random_double(), self._random_bigint()),
                'zadd {} {} {} {} {} {} {} {} {} {} {}'.format(self._random_int(), self._random_double(), self._fake_name(),
                                                               self._random_double(), self._fake_address(), self._random_double(),
                                                               self._fake_ssn(), self._random_double(), self._random_element(), self._lexify(), self._random_01()),
                ]
        return random.choice(meta)

    def geoadd(self):
        meta = ['geoadd {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_address()),
                'geoadd {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                     self._fake_longitude(), self._fake_latitude(), self._fake_address()),
                'geoadd {} {} {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                              self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                              self._fake_longitude(), self._fake_latitude(), self._fake_address()),
                'geoadd {} {} {} {}'.format(self._fake_name(), self._fake_longitude(
                ), self._fake_latitude(), self._fake_address()),
                'geoadd {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                     self._fake_longitude(), self._fake_latitude(), self._fake_address()),
                'geoadd {} {} {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                              self._fake_longitude(), self._fake_latitude(), self._fake_address(),
                                                              self._fake_longitude(), self._fake_latitude(), self._fake_address()),
                ]
        return random.choice(meta)

    def geohash(self):
        return 'geohash {} {} {}'.format(self._fake_name(), self._fake_address(), self._fake_address())

    def geopos(self):
        return 'geopos {} {} {}'.format(self._fake_name(), self._fake_address(), self._fake_address())

    def geodist(self):
        return 'geodist {} {} {}'.format(self._fake_name(), self._fake_address(), self._fake_address())

    def georadius(self):
        m = ['km', 'ft', 'm', 'mi']
        w = ['withcoord', 'withdist', 'withdist WITHCOORD']
        return 'georadius {} {} {} {} {} {}'.format(self._fake_name(), self._fake_longitude(), self._fake_latitude(), self._fake_coordinate(), random.choice(m), random.choice(w))

    def georadiusbymember(self):
        m = ['km', 'ft', 'm', 'mi']
        w = ['withcoord', 'withdist', 'withdist WITHCOORD']
        return 'georadiusbymember {} {} {} {} {}'.format(self._fake_name(), self._fake_address(), self._fake_coordinate(), random.choice(m), random.choice(w))

    def lindex(self):
        return 'lindex {} {}'.format(self._random_string(), self._random_int())

    def sdiff(self):
        return 'sdiff {} {}'.format(self._random_string(), self._random_string())

    def sdiffstore(self):
        return 'sdiffstore {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def smove(self):
        return 'smove {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def sinter(self):
        return 'sinter {} {}'.format(self._random_string(), self._random_string())

    def sinterstore(self):
        return 'sinterstore {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def sunion(self):
        return 'sunion {} {}'.format(self._random_string(), self._random_string())

    def sunionstore(self):
        return 'sunionstore {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def zunionstore(self):
        return 'zunionstore {} {} {} {} weights {} {}'.format(self._random_string(), self._random_smallint(), self._random_string(
        ), self._random_string(), self._random_smallint(), self._random_smallint())

    def zinterstore(self):
        return 'zinterstore {} {} {} {} weights {} {}'.format(self._random_string(), self._random_smallint(), self._random_string(
        ), self._random_string(), self._random_smallint(), self._random_smallint())

    def hset(self):
        '''NOTE: not support multiple k-v pair'''
        return 'hset {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def lrange(self):
        return 'lrange {} {} {}'.format(self._random_string(), self._random_smallint(), self._random_smallint())

    def zrange(self):
        meta = ['zrange {} {} {} withscore'.format(self._text(), self._random_smallint(), self._random_smallint()),
                'zrange {} {} {}'.format(
                    self._data_time(), self._random_smallint(), self._random_smallint()),
                'zrange {} {} {} withscore'.format(
                    self._fake_inner_ip(), self._random_smallint(), self._random_smallint()),
                'zrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'zrange {} {} {} withscore'.format(
                    self._random_int(), self._random_smallint(), self._random_smallint()),
                'zrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def xrange(self):
        meta = ['xrange {} {} {} count {}'.format(self._text(), self._random_smallint(), self._random_smallint(), self._random_smallint()),
                'xrange {} - +'.format(self._data_time()),
                'xrange {} {} {} count {}'.format(self._fake_inner_ip(
                ), self._random_smallint(), self._random_smallint(), self._random_smallint()),
                'xrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'xrange {} - + count {}'.format(self._random_int(),
                                                self._random_smallint()),
                'xrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def xrevrange(self):
        meta = ['xrevrange {} {} {} count {}'.format(self._text(), self._random_smallint(), self._random_smallint(), self._random_smallint()),
                'xrevrange {} + -'.format(self._data_time()),
                'xrevrange {} {} {} count {}'.format(self._fake_inner_ip(
                ), self._random_smallint(), self._random_smallint(), self._random_smallint()),
                'xrevrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'xrevrange {} + - count {}'.format(
                    self._random_int(), self._random_smallint()),
                'xrevrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def zremrangebyrank(self):
        return 'zremrangebyrank {} {} {}'.format(self._random_string(), self._random_smallint(), self._random_smallint())

    def zrangebyscore(self):
        meta = ['zrangebyscore {} ({} {} withscore'.format(self._text(), self._random_smallint(), self._random_smallint()),
                'zrangebyscore {} {} {}'.format(
                    self._data_time(), self._random_smallint(), self._random_smallint()),
                'zrangebyscore {} {} ({} withscore'.format(
                    self._fake_inner_ip(), self._random_smallint(), self._random_smallint()),
                'zrangebyscore {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'zrangebyscore {} {} ({} withscore'.format(
                    self._random_int(), self._random_smallint(), self._random_smallint()),
                'zrangebyscore {} ({} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def zrangebylex(self):
        meta = ['zrangebylex {} ({} {}'.format(self._text(), self._random_element(), self._random_element()),
                'zrangebylex {} {} {}'.format(
                    self._data_time(), self._random_element(), self._random_element()),
                'zrangebylex {} {} ({}'.format(self._fake_inner_ip(
                ), self._random_element(), self._random_element()),
                'zrangebylex {} {} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                'zrangebylex {} {} ({}'.format(
                    self._random_int(), self._random_element(), self._random_element()),
                'zrangebylex {} ({} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                ]
        return random.choice(meta)

    def zrevrangebylex(self):
        meta = ['zrevrangebylex {} ({} {}'.format(self._text(), self._random_element(), self._random_element()),
                'zrevrangebylex {} {} {}'.format(
                    self._data_time(), self._random_element(), self._random_element()),
                'zrevrangebylex {} {} ({}'.format(
                    self._fake_inner_ip(), self._random_element(), self._random_element()),
                'zrevrangebylex {} {} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                'zrevrangebylex {} {} ({}'.format(
                    self._random_int(), self._random_element(), self._random_element()),
                'zrevrangebylex {} ({} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                ]
        return random.choice(meta)

    def zlexcount(self):
        meta = ['zlexcount {} ({} {}'.format(self._text(), self._random_element(), self._random_element()),
                'zlexcount {} {} {}'.format(
                    self._data_time(), self._random_element(), self._random_element()),
                'zlexcount {} {} ({}'.format(self._fake_inner_ip(
                ), self._random_element(), self._random_element()),
                'zlexcount {} {} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                'zlexcount {} {} ({}'.format(
                    self._random_int(), self._random_element(), self._random_element()),
                'zlexcount {} ({} {}'.format(self._fake_name(),
                                             self._random_element(), self._random_element()),
                ]
        return random.choice(meta)

    def zremrangebylex(self):
        meta = ['zremrangebylex {} ({} {}'.format(self._text(), self._random_element(), self._random_element()),
                'zremrangebylex {} {} {}'.format(
                    self._data_time(), self._random_element(), self._random_element()),
                'zremrangebylex {} {} ({}'.format(
                    self._fake_inner_ip(), self._random_element(), self._random_element()),
                'zremrangebylex {} {} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                'zremrangebylex {} {} ({}'.format(
                    self._random_int(), self._random_element(), self._random_element()),
                'zremrangebylex {} ({} {}'.format(
                    self._fake_name(), self._random_element(), self._random_element()),
                ]
        return random.choice(meta)

    def zremrangebyscore(self):
        meta = ['zrangebyscore {} ({} {} withscore'.format(self._text(), self._random_int(), self._random_int()),
                'zrangebyscore {} {} {}'.format(
                    self._data_time(), self._random_int(), self._random_int()),
                'zrangebyscore {} {} ({} withscore'.format(
                    self._fake_inner_ip(), self._random_int(), self._random_int()),
                'zrangebyscore {} {} {}'.format(
                    self._fake_name(), self._random_int(), self._random_int()),
                'zrangebyscore {} {} ({} withscore'.format(
                    self._random_int(), self._random_int(), self._random_int()),
                'zrangebyscore {} ({} {}'.format(
                    self._fake_name(), self._random_int(), self._random_int()),
                ]
        return random.choice(meta)

    def zrevrangebyscore(self):
        meta = ['zrevrangebyscore {} ({} {} withscore'.format(self._text(), self._random_smallint(), self._random_smallint()),
                'zrevrangebyscore {} {} {}'.format(
                    self._data_time(), self._random_smallint(), self._random_smallint()),
                'zrevrangebyscore {} {} ({} withscore'.format(
                    self._fake_inner_ip(), self._random_smallint(), self._random_smallint()),
                'zrevrangebyscore {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'zrevrangebyscore {} {} ({} withscore'.format(
                    self._random_string(), self._random_smallint(), self._random_smallint()),
                'zrevrangebyscore {} ({} {}'.format(
                    self._random_string(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def zrevrange(self):
        meta = ['zrevrange {} {} {} withscore'.format(self._text(), self._random_smallint(), self._random_smallint()),
                'zrevrange {} {} {}'.format(
                    self._data_time(), self._random_smallint(), self._random_smallint()),
                'zrevrange {} {} {} withscore'.format(
                    self._fake_inner_ip(), self._random_smallint(), self._random_smallint()),
                'zrevrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                'zrevrange {} {} {} withscore'.format(
                    self._random_int(), self._random_smallint(), self._random_smallint()),
                'zrevrange {} {} {}'.format(
                    self._fake_name(), self._random_smallint(), self._random_smallint()),
                ]
        return random.choice(meta)

    def zcount(self):
        return 'zcount {} {} {}'.format(self._random_string(), self._random_int(), self._random_int())

    def linsert(self):
        meta = ['linsert {} before {} {}'.format(self._random_string(), self._fake_name(), self._random_smallint()),
                'linsert {} AFTER {} {}'.format(self._random_string(
                ), self._random_string(), self._random_smallint()),
                ]
        return random.choice(meta)

    def ltrim(self):
        return 'ltrim {} {} {}'.format(self._random_string(), self._random_smallint(), self._random_smallint())

    def xtrim(self):
        meta = ['xtrim {} maxlen ~ {}'.format(self._random_string(), self._random_int()),
                'xtrim {} maxlen {}'.format(
                    self._random_string(), self._random_bigint()),
                ]
        return random.choice(meta)

    def hsetnx(self):
        '''Q: is this command support multiple k-v set??'''
        return 'hsetnx {} {} {}'.format(self._random_string(), self._random_string(), self._random_string())

    def hget(self):
        return 'hget {} {}'.format(self._random_string(), self._random_string())

    def zrank(self):
        return 'zrank {} {}'.format(self._random_string(), self._random_string())

    def zrevrank(self):
        return 'zrevrank {} {}'.format(self._random_string(), self._random_string())

    def hmget(self):
        meta = ['hmget {} {}'.format(self._data_time(), self._fake_name()),
                'hmget {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'hmget {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'hmget {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'hmget {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def sadd(self):
        meta = ['sadd {} {}'.format(self._data_time(), self._fake_name()),
                'sadd {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'sadd {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'sadd {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'sadd {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def pfadd(self):
        meta = ['pfadd {} {}'.format(self._data_time(), self._fake_name()),
                'pfadd {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'pfadd {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'pfadd {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'pfadd {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def pfmerge(self):
        meta = ['pfmerge {} {}'.format(self._data_time(), self._fake_name()),
                'pfmerge {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'pfmerge {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'pfmerge {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'pfmerge {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def pfcount(self):
        meta = ['pfcount {}'.format(self._fake_name()),
                'pfcount {} {}'.format(self._data_time(), self._fake_name()),
                'pfcount {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'pfcount {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'pfcount {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'pfcount {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def hmset(self):
        meta = ['hmset {} {} {}'.format(self._text(), self._text(), self._random_element()),
                'hmset {} {} {} {} {}'.format(self._data_time(), self._data_time(
                ), self._fake_name(), self._fake_ssn(), self._fake_name()),
                'hmset {} {} {} {} {} {} {}'.format(self._fake_inner_ip(), self._fake_inner_ip(), self._fake_name(), self._text(),
                                                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'hmset {} {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text(),
                                                          self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'hmset {} {} {} {} {} {} {} {} {} {} {}'.format(self._random_int(), self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint(),
                                                                self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint()),
                'hmset {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(self._fake_name(),
                                                                      self._fake_name(), self._text(), self._fake_inner_ip(
                ), self._lexify(), self._random_int(), self._data_time(),
            self._fake_name(), self._text(), self._fake_inner_ip(
                ), self._lexify(), self._random_int(), self._data_time()
        ),
        ]
        return random.choice(meta)

    def hstrlen(self):
        return 'hstrlen {} {}'.format(self._random_string(), self._random_string())

    def hexists(self):
        return 'hexists {} {}'.format(self._random_string(), self._random_string())

    def hlen(self):
        return 'hlen {}'.format(self._random_string())

    def hgetall(self):
        return 'hgetall {}'.format(self._random_string())

    def hkeys(self):
        return 'hkeys {}'.format(self._random_string())

    def hvals(self):
        return 'hvals {}'.format(self._random_string())

    def hdel(self):
        meta = ['hdel {} {}'.format(self._data_time(), self._fake_name()),
                'hdel {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'hdel {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'hdel {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'hdel {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def xdel(self):
        meta = ['xdel {} {}'.format(self._data_time(), self.stream_id()),
                'xdel {} {} {}'.format(
                    self._fake_inner_ip(), self.stream_id(), self.stream_id()),
                'xdel {} {} {} {}'.format(
                    self._fake_name(), self.stream_id(), self.stream_id(), self.stream_id()),
                'xdel {} {} {} {} {}'.format(self._random_int(), self.stream_id(
                ), self.stream_id(), self.stream_id(), self.stream_id()),
                'xdel {} {} {} {} {} {}'.format(self._fake_name(), self.stream_id(
                ), self.stream_id(), self.stream_id(), self.stream_id(), self.stream_id()),
                ]
        return random.choice(meta)

    def zrem(self):
        meta = ['zrem {} {}'.format(self._data_time(), self._fake_name()),
                'zrem {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'zrem {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'zrem {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'zrem {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def hincrby(self):
        return 'hincrby {} {} {}'.format(self._random_string(), self._random_string(), self._random_int())

    def lrem(self):
        return 'lrem {} {} {}'.format(self._random_string(), self._random_smallint(), self._random_int())

    def srem(self):
        return 'srem {} {}'.format(self._random_string(), self._random_string())

    def hincrbyfloat(self):
        """NOTE, str(double) is scientific notation."""
        return 'hincrbyfloat {} {} {}'.format(self._random_string(), self._random_string(), str(self._random_double()))

    def append(self):
        return 'append {} {}'.format(self._random_string(), self._random_string())

    def sismember(self):
        return 'sismember {} {}'.format(self._random_string(), self._random_string())

    def bitcount(self):
        meta = ['bitcount {}'.format(self._random_string()),
                'bitcount {} {} {}'.format(
                    self._random_string(), self._random_01(), self._random_01()),
                ]
        return random.choice(meta)

    def bitop(self):
        meta = ['bitop and {} {} {}'.format(self._random_string(), self._random_string(), self._random_string()),
                'bitop or {} {} {}'.format(self._random_string(
                ), self._random_string(), self._random_string()),
                'bitop xor {} {} {}'.format(self._random_string(
                ), self._random_string(), self._random_string()),
                'bitop not {} {} {}'.format(self._random_string(
                ), self._random_string(), self._random_string()),
                ]
        return random.choice(meta)

    def bitpos(self):
        meta = ['bitpos {} 0'.format(self._random_string()),
                'bitpos {} 1 0'.format(self._random_string()),
                'bitpos {} 1 2'.format(self._random_string()),
                'bitpos {} 1'.format(self._random_string()),
                ]
        return random.choice(meta)

    def decr(self):
        return 'decr {}'.format(self._random_string())

    def decrby(self):
        return 'decrby {} {}'.format(self._random_string(), self._random_int())

    def incr(self):
        return 'incr {}'.format(self._random_string())

    def incrby(self):
        return 'incrby {} {}'.format(self._random_string(), self._random_int())

    def spop(self):
        meta = ['spop {} {}'.format(self._random_string(), self._random_int()),
                'spop {}'.format(self._random_string()),
                ]
        return random.choice(meta)

    def srandmember(self):
        meta = [
            'srandmember {}'.format(self._random_string()),
            'srandmember {} {}'.format(
                self._random_string(), self._random_int()),
        ]
        return random.choice(meta)

    def incrbyfloat(self):
        """NOTE, str(double) is scientific notation."""
        return 'incrbyfloat {} {}'.format(self._random_string(), str(self._random_double()))

    def set(self):
        return 'set {} {}'.format(self._random_string(), self._random_string())

    def setnx(self):
        return 'setnx {} {}'.format(self._random_string(), self._random_string())

    def getset(self):
        return 'getset {} {}'.format(self._random_string(), self._random_string())

    def rpoplpush(self):
        return 'rpoplpush {} {}'.format(self._random_string(), self._random_string())

    def get(self):
        return 'get {}'.format(self._random_string())

    def zpopmax(self):
        return 'zpopmax {}'.format(self._random_string())

    def zpopmin(self):
        return 'zpopmin {}'.format(self._random_string())

    def scard(self):
        return 'scard {}'.format(self._random_string())

    def zcard(self):
        return 'zcard {}'.format(self._random_string())

    def smembers(self):
        return 'smembers {}'.format(self._random_string())

    def ttl(self):
        return 'ttl {}'.format(self._random_string())

    def pttl(self):
        return 'pttl {}'.format(self._random_string())

    def persist(self):
        return 'persist {}'.format(self._random_string())

    def mget(self):
        meta = ['mget {}'.format(self._text()),
                'mget {} {}'.format(self._data_time(), self._fake_name()),
                'mget {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'mget {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'mget {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'mget {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def mset(self):
        meta = ['mset {} {}'.format(self._text(), self._random_element()),
                'mset {} {} {} {}'.format(
                    self._data_time(), self._fake_name(), self._fake_ssn(), self._fake_name()),
                'mset {} {} {} {} {} {}'.format(self._fake_inner_ip(), self._fake_name(), self._text(),
                                                self._fake_inner_ip(), self._fake_name(), self._text()),
                'mset {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text(),
                                                      self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'mset {} {} {} {} {} {} {} {} {} {}'.format(self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint(),
                                                            self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint()),
                'mset {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                    self._fake_name(), self._text(), self._fake_inner_ip(
                    ), self._lexify(), self._random_int(), self._data_time(),
                    self._fake_name(), self._text(), self._fake_inner_ip(
                    ), self._lexify(), self._random_int(), self._data_time()
        ),
        ]
        return random.choice(meta)

    def msetnx(self):
        meta = ['msetnx {} {}'.format(self._text(), self._random_element()),
                'msetnx {} {} {} {}'.format(
                    self._data_time(), self._fake_name(), self._fake_ssn(), self._fake_name()),
                'msetnx {} {} {} {} {} {}'.format(self._fake_inner_ip(), self._fake_name(), self._text(),
                                                  self._fake_inner_ip(), self._fake_name(), self._text()),
                'msetnx {} {} {} {} {} {} {} {}'.format(self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text(),
                                                        self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'msetnx {} {} {} {} {} {} {} {} {} {}'.format(self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint(),
                                                              self._random_int(), self._lexify(), self._fake_name(), self._text(), self._random_bigint()),
                'msetnx {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                    self._fake_name(), self._text(), self._fake_inner_ip(
                    ), self._lexify(), self._random_int(), self._data_time(),
                    self._fake_name(), self._text(), self._fake_inner_ip(
                    ), self._lexify(), self._random_int(), self._data_time()
        ),
        ]
        return random.choice(meta)

    def strlen(self):
        return 'strlen {}'.format(self._random_string())

    def llen(self):
        return 'llen {}'.format(self._random_string())

    def xlen(self):
        return 'xlen {}'.format(self._random_string())

    def rpop(self):
        return 'rpop {}'.format(self._random_string())

    def lpop(self):
        return 'lpop {}'.format(self._random_string())

    def lpush(self):
        meta = ['lpush {} {}'.format(self._data_time(), self._fake_name()),
                'lpush {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'lpush {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'lpush {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'lpush {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def rpush(self):
        meta = ['rpush {} {}'.format(self._data_time(), self._fake_name()),
                'rpush {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'rpush {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'rpush {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'rpush {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def rpushx(self):
        meta = ['rpushx {} {}'.format(self._data_time(), self._fake_name()),
                'rpushx {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'rpushx {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'rpushx {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'rpushx {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def lpushx(self):
        meta = ['lpushx {} {}'.format(self._data_time(), self._fake_name()),
                'lpushx {} {} {}'.format(
                    self._fake_inner_ip(), self._fake_name(), self._text()),
                'lpushx {} {} {} {}'.format(
                    self._fake_name(), self._fake_inner_ip(), self._random_int(), self._text()),
                'lpushx {} {} {} {} {}'.format(self._random_int(), self._lexify(
                ), self._fake_name(), self._text(), self._random_bigint()),
                'lpushx {} {} {} {} {} {}'.format(self._fake_name(), self._text(
                ), self._fake_inner_ip(), self._lexify(), self._random_int(), self._data_time()),
                ]
        return random.choice(meta)

    def expire(self):
        return 'expire {} {}'.format(self._random_string(), self._random_int())

    def expireat(self):
        return 'expireat {} {}'.format(self._random_string(), self._random_int())

    def pexpire(self):
        return 'pexpire {} {}'.format(self._random_string(), self._random_int())

    def pexpireat(self):
        return 'pexpireat {} {}'.format(self._random_string(), self._random_int())

    def getbit(self):
        return 'getbit {} {}'.format(self._random_string(), self._random_int())

    def setbit(self):
        return 'setbit {} {} {}'.format(self._random_string(), self._random_int(), self._random_01())

    def lset(self):
        return 'lset {} {} {}'.format(self._random_string(), self._random_int(), self._random_string())

    def getrange(self):
        return 'getrange {} {} {}'.format(self._random_string(), self._random_int(), self._random_int())

    def setrange(self):
        return 'setrange {} {} {}'.format(self._random_string(), self._random_int(), self._random_string())

    def setex(self):
        return 'setex {} {} {}'.format(self._random_string(), self._random_int(), self._text())

    def psetex(self):
        return 'psetex {} {} {}'.format(self._random_string(), self._random_int(), self._text())

    def substr(self):
        return 'substr {} {} {}'.format(self._random_string(), self._random_int(), self._random_int())


redis_command = Provider
