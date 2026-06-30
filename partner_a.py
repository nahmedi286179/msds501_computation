# ============================================================
# MSDS 501 – Day 2 Exercise  |  Partner A
# ============================================================
# SCENARIO: A sensor logs daily temperature readings as strings.
# Some readings are corrupt (non-numeric). The script tries to
# convert every reading to a float so we can compute the average.
#
# YOUR TASK (Task 2): Run this script and read the error.
#   - What type of error is it?
#Value Error 
#   - Which line causes it?
#35
#   - Write a comment below explaining the cause.
#'N/A' and 'sensor_error' cannot convert into a float type
# YOUR TASK (Task 3): Wrap the risky conversion in try/except.
#   - Catch the specific error type (not bare except:)
#   - When a bad value is caught, print a message that includes
#     the index and the bad value — e.g.:
#         [index 3] Skipped bad reading: 'N/A'
#   - The script should complete without crashing.
#
# EXPECTED OUTPUT (after your fix):
#   Reading [0]: 72.1
#   Reading [1]: 68.5
#   [index 2] Skipped bad reading: 'N/A'
#   Reading [3]: 74.0
#   [index 4] Skipped bad reading: 'sensor_error'
#   Reading [5]: 69.3
#   Average of valid readings: 70.98
# ============================================================

readings = ['72.1', '68.5', 'N/A', '74.0', 'sensor_error', '69.3']

valid = []

for i, r in enumerate(readings):
    try:
        temp = float(r)           # <-- this line crashes on bad strings
        print(f'Reading [{i}]: {temp}')
        valid.append(temp)
    except ValueError:
        print(f'Value [{i}] could not be converted')
    except Exception as oh: 
        print(f'Unexpected Error is [{oh}]')

average = sum(valid) / len(valid)
print(f'Average of valid readings: {round(average, 2)}')
