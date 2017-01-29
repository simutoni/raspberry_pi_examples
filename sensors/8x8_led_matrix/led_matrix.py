from time import sleep
from max7219.font import proportional, LCD_FONT
import max7219.led as led

hearth_matrix = [[0, 1, 1, 0, 0, 1, 1, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]
                 ]
smile_matrix = [[0, 0, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 1, 0, 0]
                ]
sad_matrix = [[0, 0, 1, 1, 1, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 1, 1, 0, 0, 1],
              [1, 0, 1, 0, 0, 1, 0, 1],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 1, 1, 0, 0]
              ]

device = led.matrix(cascaded=1)
device.brightness(0)

# var 1 if you want to write text
device.show_message("Hello", delay=0.2, font=proportional(LCD_FONT), )


# var 2 if you want to draw something
def draw_matrix(matrix):
    for row, row_list in enumerate(matrix):
        for column, column_value in enumerate(row_list):
            device.pixel(column, row, column_value)

draw_matrix(hearth_matrix)
sleep(2)
draw_matrix(smile_matrix)
sleep(2)
draw_matrix(sad_matrix)
sleep(2)

device.clear()


