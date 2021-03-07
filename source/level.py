try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import maps

class Level:
    def __init__(self, grid):
        self.CANVAS_WIDTH = 720
        self.CANVAS_HEIGHT = 720
        self.WALL = 1
        self.grid = grid
        self.grid_width = len(grid[0])
        self.grid_height = len(grid)
        self.cell_width = self.CANVAS_WIDTH // self.grid_width
        self.cell_height = self.CANVAS_HEIGHT // self.grid_height



    def draw(self, canvas):
        for y in range(self.grid_height):
            for x in range (self.grid_width):
                self.draw_cell(x, y, canvas)

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


class Interaction:
    def __init__(self, level):
        self.level = level
    def draw(self, canvas):
        self.level.draw(canvas)

if __name__ == "__main__":
    level_start = Level(maps.LEVEL_GRID_CENTRE)
    level_1 = Level(maps.LEVEL_GRID_1)
    level_2 = Level(maps.LEVEL_GRID_2)
    interaction = Interaction(level_start)

    frame = simplegui.create_frame("My Level", 720, 720)
    frame.set_draw_handler(interaction.draw)
    frame.start()