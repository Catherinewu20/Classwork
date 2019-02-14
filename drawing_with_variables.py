import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(540, 380, 50, arcade.color.YELLOW)
arcade.draw_rectangle_filled(320, 50, 640, 100, arcade.color.GREEN, 0)
arcade.draw_rectangle_filled(640-125, 87.5, 20, 150-75, arcade.color.BROWN, 0)
arcade.draw_rectangle_filled(640-200, 87.5, 20, 150-75, arcade.color.BROWN, 0)
arcade.draw_rectangle_filled(200, 87.5, 20, 150-75, arcade.color.BROWN, 0)
arcade.draw_triangle_filled(160, 125, 200, 200, 240, 125, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(160, 125, 200, 200, 240, 125, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(640-200-40, 125, 640-200, 200, 640-200+40, 125, arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(640-125-40, 125, 640-125, 200, 640-125+40, 125, arcade.color.DARK_GREEN)


# End drawing
arcade.finish_render()
arcade.run()