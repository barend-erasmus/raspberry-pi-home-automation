import schedule
import time
import RPi.GPIO as GPIO

def setupAsOutput(pinNumber):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pinNumber, GPIO.OUT)
  GPIO.output(pinNumber, GPIO.LOW)

def destroyOutput(pinNumber):
  GPIO.output(pinNumber, GPIO.LOW)
  GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
  setupAsOutput(12)

  schedule.every(6).minutes.do(lambda: (
    GPIO.output(12, GPIO.LOW)
  ))
  
  schedule.every(4).minutes.do(lambda: (
    GPIO.output(12, GPIO.HIGH)
  ))

  while 1:
      schedule.run_pending()
      time.sleep(1)