import RPi.GPIO as GPIO
import time
import numpy
from ADCDevice import *

class Matrix():
    dataPin  = 11
    latchPin = 13
    clockPin = 15
    adc = ADS7830()
    Z_Pin = 12
    buzzerPin = 18

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.dataPin, GPIO.OUT)
        GPIO.setup(self.latchPin, GPIO.OUT)
        GPIO.setup(self.clockPin, GPIO.OUT)
        GPIO.setup(self.Z_Pin, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.buzzerPin, GPIO.OUT)
        GPIO.output(self.buzzerPin,GPIO.LOW)

    def displayMatrix(self, matrix):
        for idx, column in enumerate(numpy.transpose(matrix)):
            GPIO.output(self.latchPin,GPIO.LOW)

            for column_value in column:
                GPIO.output(self.clockPin,GPIO.LOW)
                GPIO.output(self.dataPin,GPIO.HIGH if column_value == 1 else GPIO.LOW)
                GPIO.output(self.clockPin,GPIO.HIGH)
            
            for column_number in self.columns[idx]:
                GPIO.output(self.clockPin,GPIO.LOW)
                GPIO.output(self.dataPin,GPIO.LOW if column_number == 1 else GPIO.HIGH)
                GPIO.output(self.clockPin,GPIO.HIGH)

            GPIO.output(self.latchPin,GPIO.HIGH)
            time.sleep(0.001)

    def buzz(self):
        GPIO.output(self.buzzerPin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(self.buzzerPin, GPIO.LOW)

    def buzz_won(self):
        GPIO.output(self.buzzerPin, GPIO.HIGH)
        time.sleep(0.03)
        GPIO.output(self.buzzerPin, GPIO.LOW)
        time.sleep(0.03)

    def destroy(self):
        self.displayMatrix(self.resetMatrix)
        self.adc.close()
        GPIO.cleanup()
