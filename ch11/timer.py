#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start = datetime.now()
    start_time = start.strftime("%H:%M:%S:%f")
    print("Start time:", start_time)
    print()
    
    # stop timer
    input("Press Enter to stop...")  
    stop = datetime.now()  
    stop_time = stop.strftime("%H:%M:%S:%f")
    print("Stop time: ", stop_time)
    print()

    # calculate elapsed time
    elapsed_time = stop - start
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds)

    # display results
    print("ELAPSED TIME")
    if days > 0:
        print("Days:", days)
    if time_object > 0:
        print("Time:", time_object)
    else:
        print("Please try again detected no non-zero values!")

if __name__ == "__main__":
    main()
