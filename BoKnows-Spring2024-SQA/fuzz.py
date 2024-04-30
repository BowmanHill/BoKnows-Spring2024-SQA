from empirical.report import Average, Median, reportProp
from empirical.frequency import reportProportion
import random


def simpleFuzzer():
    ls = [145.3,'123', 123]

    # Initialize a list to store crash messages
    crash_messages = []
    
    try:
        Average(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))

    try:
        reportProportion(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))

    try:
        Median(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))
        
    try:
        reportProp(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))
        
    try:
        modls = ls + str( random.randint(1,10))
        reportProportion(ls, modls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))        
        
    # Print the crash messages
    print("Crash messages:")
    for msg in crash_messages:
        print(msg)

if __name__ == '__main__':
    simpleFuzzer()