class Stats:
    def __init__(self):
        self.alive = True
        self.speed = 1

    def die(self):
        self.alive = False
        return self.score

    def set_speed(self, value):
        self.speed += value

    def get_score(self):
        return self.score


class PlayerStats(Stats):
    def __init__(self, speedMul):
        Stats.__init__(self)
        self.speed = self.speed * speedMul
        self.lives = 3
        self.score = 0
        self.bullets = []

    def set_life(self,value):
        if value > 0:
            self.lives += 0
        else:
            if self.can_remove_life: # only removes life if a sufficient amount of time has passed.
                self.last_time_remove_life = self.time
                self.can_remove_life = False
                self.lives -= value
            if self.lives <= 0:
                self.die()

    def get_lives(self):
        return self.lives

    def set_score(self, value):
        self.score += value


    def get_bullets(self):
        return self.bullets


class EnemyStats(Stats):
    def __init__(self, healthMul = 1, speedMul = 1, scoreMul = 1):
        Stats.__init__(self)
        self.health = 100 * healthMul
        self.speed = self.speed * speedMul
        self.score = 5 * scoreMul

    def set_health(self, amount):
        self.health += amount
        if self.health <= 0:
            self.die()

    def get_health(self):
        return self.health


class Bullet(Stats):
    def __init__(self, color = "red"):
        Stats.__init__(self)
        self.damage = 100
        self.color = color

    def die(self):
        #link with out_of_bounds method in movement
        self.alive = False

    def get_damage(self):
        return self.damage