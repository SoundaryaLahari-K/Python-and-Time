import time
print('Press Enter to begin. Afterward, press Enter to "Click" the stopwatch. Press Ctrl-C to quit')
input()
print('Started')
startTime=time.time()
lastTime = startTime
lapNum=1
try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print('Lap #%s: totaltime: %s laptime: (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    print('totalTime:',totalTime)
finally:
    print('Thank You for using this stopwatch')

