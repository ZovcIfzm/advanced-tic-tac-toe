import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        # Draw the trunk
        height = 600
        width = 600
        #vertical
        arcade.draw_lrtb_rectangle_filled(width/3-10, width/3+10, \
          height - 20, 20, arcade.color.DARK_GRAY)
        arcade.draw_lrtb_rectangle_filled(width*2/3-10, width*2/3+10, \
          height - 20, 20, arcade.color.DARK_GRAY)
        
        #horizonal
        arcade.draw_lrtb_rectangle_filled(20, width - 20, \
          height/3+10, height/3-10, arcade.color.DARK_GRAY)
        arcade.draw_lrtb_rectangle_filled(20, width - 20, \
          height*2/3+10, height*2/3-10, arcade.color.DARK_GRAY)

        arcade.draw_lrtb_rectangle_filled(width+20, width+25, \
          height, 0, arcade.color.DARK_GRAY)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

'''
on_draw: All the code to draw the screen goes here.
update: All the code to move your items and perform game logic goes here. This is called about 60 times per second.
on_key_press: Handle events when a key is pressed, such as giving a player a speed.
on_key_release: Handle when a key is released, here you might stop a player from moving.
on_mouse_motion: This is called every time the mouse moves.
on_mouse_press: Called when a mouse button is pressed.
set_viewport: This function is used in scrolling games, when you have a world much larger than what can be seen on one screen. Calling set_viewport allows a programmer to set what part of that world is currently visible.

'''

'''
import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Set the background color to white.
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

'''