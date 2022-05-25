"""
Add menus to you Mine Sweeper game to be able to
 - Start new game
 - Change game layout (5x5, 5x8, 8x8)
 - Close game
"""
import tkinter
from random import randint


class MineSweeper():
    title = 'Main Menu'

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Minesweeper")
        self.add_menu()
        for i in range(5):
            for j in range(5):
                self.__setattr__(f'label{i, j}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=3, height=2))
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text='o', command=self.do_nothing(5, 3)))
                self.__getattribute__(f'label{i, j}').grid(row=i, column=j)
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def is_bomb(self):
        return randint(0, 1)

    def do_nothing(self, n, k):
        pass
        # arr = [[0 for row in range(n)] for column in range(n)]
        # for num in range(k):
        #     x = randint(0, n - 1)
        #     y = randint(0, n - 1)
        #     arr[y][x] = 'X'
        #     if (x >= 0 and x <= 2) and (y >= 0 and y <= 3):
        #         if arr[y][x + 1] != 'X':
        #             arr[y][x + 1] += 1  # center right
        #     if (x >= 1 and x <= 3) and (y >= 0 and y <= 3):
        #         if arr[y][x - 1] != 'X':
        #             arr[y][x - 1] += 1  # center left
        #     if (x >= 1 and x <= n - 1) and (y >= 1 and y <= n - 1):
        #         if arr[y - 1][x - 1] != 'X':
        #             arr[y - 1][x - 1] += 1  # top left
        #     if (x >= 0 and x <= n - 2) and (y >= 1 and y <= n - 1):
        #         if arr[y - 1][x + 1] != 'X':
        #             arr[y - 1][x + 1] += 1  # top right
        #     if (x >= 0 and x <= n - 1) and (y >= 1 and y <= n - 1):
        #         if arr[y - 1][x] != 'X':
        #             arr[y - 1][x] += 1  # top center
        #     if (x >= 0 and x <= n - 2) and (y >= 0 and y <= n - 2):
        #         if arr[y + 1][x + 1] != 'X':
        #             arr[y + 1][x + 1] += 1  # bottom right
        #     if (x >= 1 and x <= n - 1) and (y >= 0 and y <= n - 2):
        #         if arr[y + 1][x - 1] != 'X':
        #             arr[y + 1][x - 1] += 1  # bottom left
        #     if (x >= 0 and x <= n - 1) and (y >= 0 and y <= n - 2):
        #         if arr[y + 1][x] != 'X':
        #             arr[y + 1][x] += 1  # bottom center
        #
        # for row in arr:
        #     print("\t".join(str(cell) for cell in row))
        #     print("")

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)
        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)
        main_l2.add_command(label='New Game', command=self.new_window)
        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='Change game layout (5x5, 5x8, 8x8)', menu=main_l3)
        main_l2.add_separator()
        main_l2.add_command(label='Close', command=self.main_window.destroy)

    def new_window(self):
        new_window = MineSweeper()
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)
        new_window.run()

    """
    0 1 0
    1 x 1
    0 1 0
    """

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()
