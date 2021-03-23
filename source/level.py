try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import source.maps as maps
from source.collider import Collider
from source.vector import Vector
from source.enemy import Enemy
from source.pickup import HealthPickup, BonusPickup

LEVELS_ARRAY = [maps.LEVEL_GRID_1, maps.LEVEL_GRID_2, maps.LEVEL_GRID_3, maps.LEVEL_GRID_4, maps.LEVEL_GRID_5, maps.LEVEL_GRID_6]

class Level:
    def __init__(self, grid):
        """
        The init for Level includes many constants which have been defined to help determine locations of map elements
        """
        self.CANVAS_WIDTH = 720
        self.CANVAS_HEIGHT = 720
        self.WALL = 1
        self.ENEMY = 2
        self.DOOR = 3
        self.LIFE = 4
        self.BONUS = 5

        self.box_img = simplegui._load_local_image("source/images/metal_box.png")
        self.box_img_width = self.box_img.get_width()
        self.box_img_height = self.box_img.get_height()
        self.box_img_centre = [self.box_img_width/2, self.box_img_height/2]
        
        self.grid = grid
        self.grid_width = len(grid[0])
        self.grid_height = len(grid)
        self.cell_width = self.CANVAS_WIDTH // self.grid_width
        self.cell_height = self.CANVAS_HEIGHT // self.grid_height

        self.colliders = []
        self.enemy_array = []
        self.door_array = []
        self.pickup_array = []

        for y in range(self.grid_height):
            for x in range (self.grid_width):
                if self.is_wall(x, y):
                    self.colliders.append(Collider("rect", Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)), self.cell_height, self.cell_width))
                if self.is_enemy_spawn(x, y):
                    self.enemy_array.append(Enemy([(x*self.cell_width)+(self.cell_width/2),(y*self.cell_height)+(self.cell_height/2)]))
                if self.is_door(x, y):
                    self.door_array.append(Collider("wall", Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)), self.cell_height, self.cell_width))
                if self.is_life(x,y):
                    self.draw_health(x, y)
                if self.is_bonus(x,y):
                    self.draw_bonus(x, y)

    """
    Getters and Setters for enemies and 2d arrays
    """
    def get_enemies(self):
        return self.enemy_array

    def set_enemies(self, enemy_array):
        self.enermy_array = enemy_array

    def get_level(self):
        return self.grid

    def set_level(self, grid):
        self.grid = grid

    """
    The draw methods which use SimpleGUI to draw the level behind the character
    (this includes enemies and pickups)
    """
    def draw(self, canvas):
        for y in range(self.grid_height):
            for x in range (self.grid_width):
                self.draw_cell(x, y, canvas)

    def draw_cell (self, x, y, canvas):
        if self.is_wall(x, y):

            start_x = x * self.cell_width
            start_y = y * self.cell_height
            canvas.draw_image(self.box_img, self.box_img_centre, (self.box_img_width, self.box_img_height), (start_x + self.cell_width/2, start_y + self.cell_height/2), (self.box_img_width, self.box_img_height))

    def draw_health(self, x, y):
        if random.randint(0, 100) > 60:
            pickup = HealthPickup(Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)))
            self.pickup_array.append(pickup)

    def draw_bonus(self, x, y):
        if random.randint(0, 100) > 90:
            pickup = BonusPickup(Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)), 50)
            self.pickup_array.append(pickup)\

    """
    The 'is' functions which all return boolean values to determine where to draw them
    """
    def is_wall(self, x, y):
        return self.grid[y][x] == self.WALL
    
    def is_enemy_spawn(self, x, y):
        return self.grid[y][x] == self.ENEMY

    def is_door(self, x, y):
        return self.grid[y][x] == self.DOOR

    def is_life(self, x, y):      
        return self.grid[y][x] == self.LIFE

    def is_bonus(self, x, y):
        return self.grid[y][x] == self.BONUS

    def listWalls(self):
        return self.colliders

class Interaction:
    def __init__(self, level):
        self.level = level
    def draw(self, canvas):
        self.level.draw(canvas)