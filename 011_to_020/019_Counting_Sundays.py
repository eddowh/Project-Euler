"""
Counting Sundays
"""

import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
from classes.Date import Date


if __name__ == '__main__':
    # inputs
    lowerLimit = 1901
    upperLimit = 2000
    # initialize running time
    start = time.time()
    # dates that are beginning of the month and is Sunday
    sundayDates = []
    for year in range(lowerLimit, upperLimit + 1):
        for month in range(1, 12 + 1):
            currentDate = Date(year, month, 1)
            if currentDate.get_weekday() == "Sunday":
                # print currentDate
                sundayDates.append(currentDate)
    # print len(sundayDates)
    if (time.time() - start > 30):
        raise Exception("Timeout: Running of script aborted.")
    # finalize running time
    stop = time.time()
    # print results
    print "Number of Sundays: \t %s" %(len(sundayDates))
    print "Running Time:      \t %.2f sec" % (stop - start)
