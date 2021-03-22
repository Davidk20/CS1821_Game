try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import source.maps as maps
from source.collider import Collider
from source.vector import Vector
from source.enemy import Enemy
LEVELS_ARRAY = [maps.LEVEL_GRID_1, maps.LEVEL_GRID_2, maps.LEVEL_GRID_3, maps.LEVEL_GRID_4, maps.LEVEL_GRID_5, maps.LEVEL_GRID_6]

class Level:
    def __init__(self, grid):
        self.CANVAS_WIDTH = 720
        self.CANVAS_HEIGHT = 720
        self.WALL = 1
        self.ENEMY = 2
        self.DOOR = 3
        self.memory = -1
        self.grid = grid
        self.grid_width = len(grid[0])
        self.grid_height = len(grid)
        self.cell_width = self.CANVAS_WIDTH // self.grid_width
        self.cell_height = self.CANVAS_HEIGHT // self.grid_height
        self.colliders = []
        self.enemy_array = []
        self.doors = []
        for y in range(self.grid_height):
            for x in range (self.grid_width):
                if self.is_wall(x, y):
                    self.colliders.append(Collider("rect", Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)), self.cell_height, self.cell_width))
                if self.is_enemy_spawn(x, y):
                    self.enemy_array.append(Enemy([(x*self.cell_width)+(self.cell_width/2),(y*self.cell_height)+(self.cell_height/2)]))
                if self.is_wall(x, y):
                    self.colliders.append(Collider("wall", Vector((x*self.cell_width)+(self.cell_width/2), (y*self.cell_height)+(self.cell_height/2)), self.cell_height, self.cell_width))


    def get_enemies(self):
        return self.enemy_array

    def set_enemies(self, enemy_array):
        self.enermy_array = enemy_array

    def get_level(self):
        return self.grid

    def set_level(self, grid):
        self.grid = grid

    def draw(self, canvas):
        for y in range(self.grid_height):
            for x in range (self.grid_width):
                self.draw_cell(x, y, canvas)

    def switch_level(self):
        i = random.rantint(0, len(LEVELS_ARRAY))
        while self.memory == i:
            i = random.rantint(0, len(LEVELS_ARRAY))
        
        self.memory = i
        self.grid = LEVELS_ARRAY(i)
    

    def draw_cell (self, x, y, canvas):
        if self.is_wall(x, y):

            start_x = x * self.cell_width
            start_y = y * self.cell_height

            canvas.draw_polygon([[start_x, start_y], [start_x + self.cell_width, start_y], [start_x + self.cell_width, start_y + self.cell_height], [start_x, start_y + self.cell_height]], 0, 'Yellow', 'Orange')


    def is_wall(self, x, y):
        if x < 0:
            return False
        if x >= self.grid_width:
            return False
        if y < 0:
            return False
        if y >= self.grid_height:
            return False

        return self.grid[y][x] == self.WALL
    
    def is_enemy_spawn(self, x, y):
        if x < 2:
            return False
        if x >= self.grid_width:
            return False
        if y < 2:
            return False
        if y >= self.grid_height:
            return False
        
        return self.grid[y][x] == self.ENEMY

    def is_door(self, x, y):
        if x < 3:
            return False
        if x >= self.grid_width:
            return False
        if y < 3:
            return False
        if y >= self.grid_height:
            return False
        
        return self.grid[y][x] == self.DOOR


    def listWalls(self):
        return self.colliders

#TODO move into overall interaction class
class Interaction:
    def __init__(self, level):
        self.level = level
    def draw(self, canvas):
        self.level.draw(canvas)