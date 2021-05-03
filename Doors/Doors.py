import arcade

import arcade.gui
from arcade.gui import UIFlatButton, UIGhostFlatButton, UIManager
from arcade.gui.ui_style import UIStyle

# Variables
Light_Blue = (28, 147, 156)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Doors.stu'

# Title Screen for the Game
class Title(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

        #Background image will be stored here
        self.background = None

    # Setting up what the player can see
    def setup(self):
        # Adds the image to the background
        self.background = arcade.load_texture('mmr.png')

        button_normal = arcade.load_texture('P1.png')
        hovered_texture = arcade.load_texture('P2.png')
        pressed_texture = arcade.load_texture('P3.png')
        button = arcade.gui.UIImageButton(
            center_x = 350,
            center_y = 523,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )
        self.ui_manager.add_ui_element(button)

        button_normal = arcade.load_texture('DL1.png')
        hovered_texture = arcade.load_texture('DL2.png')
        pressed_texture = arcade.load_texture('DL2.png')
        button2 = arcade.gui.UIImageButton(
            center_x=800,
            center_y=470,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )

        self.ui_manager.add_ui_element(button2)

        self.sprite1 = arcade.Sprite('B1.png', center_x=640, center_y=360)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_mouse_press(self,x,y,button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            Gameview()



class DoorOS(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_location(400,200)


    def on_draw(self):
        arcade.set_background_color(Light_Blue)
        arcade.start_render()



def TitleScreen():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,title='Doors')
    window.show_view(Title())
    arcade.run()

def Gameview():
    DoorOS(SCREEN_WIDTH,SCREEN_HEIGHT,'DoorOS')
    arcade.run()

TitleScreen()