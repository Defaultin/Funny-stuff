import pyautogui
import keyboard


class PianoTiles:
    '''Python bot for Piano Tiles autoclicking'''
    def __init__(self):
        # print('Welcome to the Piano Tiles Autoclicker! Press ESC to exit.')
        # x1 = self._mouse_pos('LEFT')[0]
        # while keyboard.is_pressed('enter'): pass
        # x2 = self._mouse_pos('RIGHT')[0]
        # self.left_x, self.right_x = min(x1, x2), max(x1, x2)
        self.left_x, self.right_x = 430, 700
        self.center_y = pyautogui.size()[1] // 2
        self.tiles = self._tiles_pos()


    def _mouse_pos(self, border):
        print(f'Place the cursor on the {border} border of the playing field and press ENTER:')
        x, y = 0, 0
        while not keyboard.is_pressed('enter') and not keyboard.is_pressed('esc'):
            x, y = pyautogui.position()
            position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(position, end='')
            print('\b' * len(position), end='', flush=True)

        print(f'{border} border: {x, y}')
        return x, y


    def _tiles_pos(self):
        length = self.right_x - self.left_x
        step = length // 4
        return [(self.left_x + i, self.center_y) for i in range(step // 2, length, step)]


    def _is_tile(self, pixel, threshold):
        color = pyautogui.pixel(*pixel)
        return True if color[0] <= threshold else False
        # return True if all([c < threshold for c in color]) else False


    def run(self, *, tile_rgb=1):
        while not keyboard.is_pressed('esc'):
            for pos in self.tiles:
                if self._is_tile(pos, tile_rgb):
                    pyautogui.click(pos[0], pos[1] - 3)
                    break
        

if __name__ == '__main__':
    PianoTiles().run()