from empirical.report import Average, Median

# Average and Median from the report.py take a list as a parameter

def simpleFuzzer():
    ls = [145.3,'123', 123]

    # Initialize a list to store crash messages
    crash_messages = []

    try:
        # Call the fuzzValues function
        Average(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))

    try:
        # Call the fuzzValues function
        Median(ls)
    except Exception as e:
            # Record the crash message
        crash_messages.append(str(e))
    # Print the crash messages
    print("Crash messages:")
    for msg in crash_messages:
        print(msg)

if __name__ == '__main__':
    simpleFuzzer()