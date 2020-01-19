from faker import Faker
from fake_redis_command import redis_command

f = Faker()
f.add_provider(redis_command)

for _ in range(1000):
    print(f.random_command())
