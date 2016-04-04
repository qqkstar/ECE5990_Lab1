import subprocess

def main():
  while True:
    key_pressed = raw_input("Enter a command: ")
    if key_pressed == 'p':
      subprocess.call("echo 'pause' > ~/Documents/lab1/video_fifo", shell=True)
    elif key_pressed == 'q':
      subprocess.call("echo 'quit' > ~/Documents/lab1/video_fifo", shell=True)
      break 

if __name__=="__main__":
  main()
