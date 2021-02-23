try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def draw(canvas):
    pass

frame = simplegui.create_frame("Game", 700 , 700)
frame.set_draw_handler(draw)
frame.start()