import time
print('Welcome to task tracker :)')
print('Press Enter to begin. Press Ctrl-c to quit')
input()
print('Started')
startTime=time.time()
try:
    while True:
       # input()
        totalTime=round(time.time()-startTime,2)
        tt=totalTime/60
      #  print('totaltime: %s', totalTime)
       # lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-c exception to keep its error message from displaying.
    print('\nDone.')
    print('TotalTime spent on the task in minutes:',round(tt))
finally:
    print('Thank You for using this Tracker')