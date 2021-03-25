from source.clock import Clock
import random

class Stats:
    '''
    Stats class used to give Player, Enemy and Projectile a
    standardised set of properties
    '''
    def __init__(self):
        self.alive = True
        self.speed = 1

    def die(self):
        '''
        method updates self.alive value dependent to False
        '''
        self.alive = False

    def get_speed(self):
        '''
        returns objects speed
        '''
        return self.speed

    def set_speed(self, value):
        '''
        sets objects speed
        '''
        self.speed += value

    def get_score(self):
        '''
        returns objects score
        '''
        return self.score


class PlayerStats(Stats):
    '''
    Class inherits from Stats but is specialised for Player object
    '''
    def __init__(self, speedMul = 3):
        Stats.__init__(self)
        self.speed = self.speed * speedMul
        self.lives = 3
        self.can_remove_life = True
        self.time_between_life_loss = 50
        self.score = 0
        self.bullets = []
        self.can_shoot = True
        self.time_between_shots = 10

    def set_life(self,value):
        '''
        method updates the players lives and kills the player
        if this value reaches 0
        '''
        if value > 0:
            self.lives += value
        else:
            if self.can_remove_life: # only removes life if a sufficient amount of time has passed.
                self.last_time_remove_life = Clock.time
                self.can_remove_life = False
                self.lives += value
            if self.lives <= 0:
                self.die()

    def get_lives(self):
        '''
        returns players lives
        '''
        return self.lives

    def set_score(self, value):
        '''
        sets players score
        '''
        self.score += value

    def get_bullets(self):
        '''
        returns players bullets as a list
        '''
        return self.bullets
    
    def add_bullets(self, bullet):
        '''
        appends projectile to players list of projectiles
        '''
        self.bullets.append(bullet)

    def remove_bullets(self, bullet):
        '''
        removes projectile from list
        '''
        self.bullets.remove(bullet)


class EnemyStats(Stats):
    '''
    Class inherits from Stats but is specialised for Enemy object
    '''
    def __init__(self, healthMul = 1, speedMul = 1, scoreMul = 1):
        Stats.__init__(self)
        self.health = 100 * healthMul
        self.speed = self.speed * speedMul
        self.score = 5 * scoreMul

    def set_health(self, amount):
        '''
        sets enemies health
        '''
        self.health += amount
        if self.health <= 0:
            self.die()

    def get_health(self):
        '''
        returns enemies health
        '''
        return self.health


class ProjectileStats(Stats):
    '''
    Class inherits from Stats but is specialised for Projectile object
    '''
    def __init__(self, color = "red"):
        Stats.__init__(self)
        self.damage = 50
        self.color = color

    def get_damage(self):
        '''
        returns damage value of projectile
        '''
        return self.damage

class PickupStats:
    '''
    Class inherits from Stats but is specialised for Pickup object
    '''
    def __init__(self, valueMul = 1):
        self.value = 1 * valueMul