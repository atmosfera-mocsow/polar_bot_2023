import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.flushall()
r.set("locations", 12)
r.set("prefix", "pr1")

print("test import:")
from user import User

print("test useradd")
u = User(r, 12345)

print("New user in game?", u.inGame())

print("test userget")
z = User(r, 12345)
print("Existing user in game?", z.inGame())

print("testing fields")
z.id
z.stage
z.stages

print("testing methods")
z.save()
z.location()
z.isEnd()

print("testing switching")
for i in range(0, 15):
    print("Loc:", i, "isEnd? ", z.isEnd())
    z.switchStage()

