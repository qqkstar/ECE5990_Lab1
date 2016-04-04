import RPi.GPIO as GPIO

def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  
  print "waiting for button press"
  in_17 = 1
  prev_in_17 = 1

  in_22 = 1
  in_23 = 1
  in_27 = 1
  prev_in_22 = 1
  prev_in_23 = 1
  prev_in_27 = 1

  
 
  while True:

    in_17 = GPIO.input(17)
    in_22 = GPIO.input(22)
    in_23 = GPIO.input(23)
    in_27 = GPIO.input(27)
  
    if(not (in_17) and prev_in_17):
      print "17 Pressed"
    if(not (in_22) and prev_in_22):
      print "22 Pressed"
    if(not (in_23) and prev_in_23):
      print "23 Pressed"
    if(not (in_27) and prev_in_27):
      print "27 Pressed"

    prev_in_17 = in_17
    prev_in_22 = in_22
    prev_in_23 = in_23
    prev_in_27 = in_27
if __name__=='__main__':
  main()
