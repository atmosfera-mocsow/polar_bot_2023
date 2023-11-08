class User():
    import json
    def __init__(self, redis, id):
        ### Здесь нельзя ничего трогать
        prefix = redis.get("prefix")
        userId = str(prefix)+str(id)

        self.ingame = True
        self.redis = redis

        if not redis.lrange(userId, 0, 2):
            redis.rpush(userId, 0, self.genStages())
            self.ingame = False

        self.id = userId
        self.stage = int(redis.lrange(userId, 0, 2)[0])
        self.stages = self.json.loads(redis.lrange(userId, 0, 2)[1])

    def save(self):
        ### Это нельзя/бесполезно вызывать
        self.redis.rpush(self.id, self.stage, self.json.dumps(self.stages))

    def genStages(self):
        ### Сюда тоже не лезь
        import random
        stages = [i for i in range(0, int(self.redis.get("locations")))]
        random.shuffle(stages)
        return self.json.dumps(stages)

    def switchStage(self):
        ### Отправляет игрока на следующий этап
        self.stage += 1
        self.save()

    def location(self):
        ### Скажет тебе куда игроку СЕЙЧАС идти
        return self.stages[self.stage]
    
    def isEnd(self):
        ### Если True — игрок прошёл ещё не все этапы
        if self.stage > int(self.redis.get("locations")):
            return True
        else:
            return False
        
    def inGame(self):
        ### Возвращает False если только что была регистрация. Не удерживается в базе.
        return self.ingame

