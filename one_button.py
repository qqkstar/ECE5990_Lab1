import RPi.GPIO as GPIO

def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  
  print "waiting for button press"
  while True:
    if(GPIO.input(17)==0):
      print "17 Pressed"
      break

if __name__=='__main__':
  main()
