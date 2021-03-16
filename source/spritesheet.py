try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Spritesheet:
    def __init__(self, file_path, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols

        self.spritesheet = simplegui._load_local_image(file_path)
        self.spritesheet_dimensions = [self.spritesheet.get_height(), self.spritesheet.get_height()]

        self.frame_width = self.spritesheet_dimensions[0] / num_rows
        self.frame_height = self.spritesheet_dimensions[1] / num_cols

        self.current_frame = 1
        self.current_col = 1

    def draw(self, canvas, pos_vector, rotation = 0, frame_index = None):
        if frame_index != None:
            self.current_frame = frame_index

        # finding the current frame dimensions
        while self.current_frame > self.num_rows:
            self.current_frame -= self.num_rows
            self.current_col += 1

        # selecting the current frame in the image
        center_source = ((self.frame_width / 2) + ((self.current_frame - 1) * self.frame_width),
                            ((self.frame_height / 2) + (self.current_col - 1) * self.frame_height))
        width_height_source = (self.frame_width, self.frame_height) # settings width and height of image
        
        width_height_dest = (self.frame_width, self.frame_height) # setting destination of image
        
        canvas.draw_image(self.spritesheet, center_source, width_height_source, pos_vector.get_p(), width_height_dest, rotation)

    def next_frame(self):
        if (self.current_frame * self.current_col) + 1 > self.num_rows * self.num_cols:
            self.current_col = 1
            self.current_frame = 1
        else:
            self.current_frame += 1
  

