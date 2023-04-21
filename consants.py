from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT


SIZE = 10
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9E948a"

BACKGROUND_COLOR_DICT = { 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179",
                        16:"#f59563", 32:"#f67c5f", 64:"#f65e3b",
                        128:"#edcf72", 256:"edcc61", 128:"#edc850",
                        1024:"#edc53f", 2048:"edcc22e", 

                        4096:"#eee4da", 8192:"#edc22e", 16384:"#f2b179",
                        32768:"#f59563", 665536:"#f67c5f"

}
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2",
                        16:"#f9f6f2", 32:"#f9f6f2", 64:"#f9f6f2",
                        128:"#f9f6f2", 256:"#f9f6f2", 128:"#f9f6f2",
                        1024:"#f9f6f2", 2048:"#f9f6f2", 

                        4096:"#776e65", 8192:"#f9f6f2", 16384:"#776e65",
                        32768:"#776e65", 665536:"#f9f6f2"

}

FONT = ("Verdana", 40, "bold")

KEY_UP = "w"
KEY_DOWN = "S"
KEY_LEFT = "A"
KEY_RIGHT = "D"