import arcade
import timeit

class Console():

    def __init__(self, gameWindow, playerController):
        self.gameWindowReference = gameWindow
        self.playerControllerReference = playerController
        return

    def on_draw_start(self):
        self.draw_start_time = timeit.default_timer()

        fps_calculation_freq = 60

        if self.frame_count % fps_calculation_freq == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = fps_calculation_freq / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

    def on_draw_end(self):
        output = f"Drawing time: {timeit.default_timer() - self.draw_start_time:.3f}"
        arcade.draw_text(output, 20, self.gameWindowReference.SCREEN_HEIGHT - 50, arcade.color.BLACK, 12)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, self.gameWindowReference.SCREEN_HEIGHT - 75, arcade.color.BLACK, 12)

        output = self.playerControllerReference.get_debug_info()
        arcade.draw_text(output, 20, self.gameWindowReference.SCREEN_HEIGHT - 100, arcade.color.BLACK, 12)

    def on_update_start(self):
        self.processing_time_start = timeit.default_timer()

    def on_update_end(self):
        output = f"Processing time: {timeit.default_timer() - self.processing_time_start:.3f}"
        arcade.draw_text(output, 20, self.gameWindowReference.SCREEN_HEIGHT - 25, arcade.color.BLACK, 12)

    
    
    processing_time_start = 0
    draw_time = 0
    frame_count = 0
    fps_start_timer = None
    fps = None
    draw_start_time = 0