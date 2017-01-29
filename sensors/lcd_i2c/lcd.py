from lcd_i2c.lcd_config import *
import lcd_i2c.settings as settings

if __name__ == '__main__':

    lcd = LCD_i2c()
    try:
        while True:
            lcd.lcd_string("$$$$$", settings.LCD_LINE_1)
            lcd.lcd_string("....", settings.LCD_LINE_2)
            time.sleep(5)
    except Exception as e :
        print(e)
    finally:
        lcd.lcd_byte(0x01, settings.LCD_CMD)
