import arcade
import Door_Buttons

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

        self.quit_list = arcade.SpriteList()
        self.quit = arcade.AnimatedTimeBasedSprite()
        self.quit.textures = []

        self.quit.textures.append(arcade.load_texture('B1.png'))
        self.quit.textures.append(arcade.load_texture('B2.png'))
        self.quit.textures.append(arcade.load_texture('B3.png'))
        self.quit.textures.append(arcade.load_texture('B4.png'))
        self.quit.textures.append(arcade.load_texture('B5.png'))

        self.quit.center_x = 640
        self.quit.center_y = 360


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

        if self.button.collides_with_point((x, y)):
            self.button.click()
            print('Start')

        elif self.button2.collides_with_point((x, y)):
            self.button2.click()
            print('Quit')




class DoorOS(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

        #Background image will be stored here
        self.background = None

    def setup(self):
        button_normal = arcade.load_texture('Trash.png')
        hovered_texture = arcade.load_texture('Trash2.png')
        pressed_texture = arcade.load_texture('Trash2.png')
        button3 = arcade.gui.UIImageButton(
            center_x=60,
            center_y=670,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )

        self.ui_manager.add_ui_element(button3)

        button_normal = arcade.load_texture('E.png')
        hovered_texture = arcade.load_texture('E.png')
        pressed_texture = arcade.load_texture('E.png')
        button4 = arcade.gui.UIImageButton(
            center_x=60,
            center_y=530,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )

        self.ui_manager.add_ui_element(button4)
        button_normal = arcade.load_texture('Sh1.png')
        hovered_texture = arcade.load_texture('Sh2.png')
        pressed_texture = arcade.load_texture('Sh1.png')
        button5 = arcade.gui.UIImageButton(
            center_x=60,
            center_y=410,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )

        self.ui_manager.add_ui_element(button5)

        button_normal = arcade.load_texture('DoorG1.png')
        hovered_texture = arcade.load_texture('DoorG2.png')
        pressed_texture = arcade.load_texture('DoorG1.png')
        button6 = arcade.gui.UIImageButton(
            center_x=60,
            center_y=270,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
        )

        self.ui_manager.add_ui_element(button6)

    def on_draw(self):
        arcade.set_background_color(Light_Blue)
        arcade.start_render()

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()


def Main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    title_screen = Title()
    window.show_view(title_screen)
    arcade.run()


Main()