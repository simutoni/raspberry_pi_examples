import smbus
import time
import lcd_i2c.settings as settings


# I2C interface
class LCD_i2c():

    def __init__(self):
        # Initialise display


        self.bus = smbus.SMBus(1) # for oldest vestion of raspberry pi you can use 0 instead.
        self.lcd_byte(0x33, settings.LCD_CMD)  # 110011 Initialise
        self.lcd_byte(0x32, settings.LCD_CMD)  # 110010 Initialise
        self.lcd_byte(0x06, settings.LCD_CMD)  # 000110 Cursor move direction
        self.lcd_byte(0x0C, settings.LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28, settings.LCD_CMD)  # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01, settings.LCD_CMD)  # 000001 Clear display
        time.sleep(settings.E_DELAY)

    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = the data
        # mode = 1 for data
        #        0 for command

        bits_high = mode | (bits & 0xF0) | settings.LCD_BACKLIGHT
        bits_low = mode | ((bits << 4) & 0xF0) | settings.LCD_BACKLIGHT

        # High bits
        self.bus.write_byte(settings.I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        # Low bits
        self.bus.write_byte(settings.I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self, bits):
        # Toggle enable
        time.sleep(settings.E_DELAY)
        self.bus.write_byte(settings.I2C_ADDR, (bits | settings.ENABLE))
        time.sleep(settings.E_PULSE)
        self.bus.write_byte(settings.I2C_ADDR, (bits & ~settings.ENABLE))
        time.sleep(settings.E_DELAY)

    def lcd_string(self, message, line):
        # Send string to display

        message = message.ljust(settings.LCD_WIDTH, " ")

        self.lcd_byte(line, settings.LCD_CMD)

        for i in range(settings.LCD_WIDTH):
            self.lcd_byte(ord(message[i]), settings.LCD_CHR)