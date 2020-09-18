
#22 ug/m^3 PM2.5 = 1 cig/day

import sys
import math

def analyze_air(concentration):
    if(concentration > 0):
        cigs_per_day = concentration / pm25
        cigs_per_hour = round(cigs_per_day / 24.0, 2)
        hours_per_cig = round(1/ cigs_per_hour, 2)
        unit_of_time = "hours"

        if hours_per_cig < 1.0:
            hours_per_cig *= 60  # convert to minutes
            unit_of_time = "minutes"

            frac, whole = math.modf(hours_per_cig)
            if frac > 0.0: # there are seconds
                seconds = 60*frac
                hours_per_cig = int(whole)
                unit_of_time += " and " + str(round(seconds)) + " seconds"

        if(concentration > 10000):
            print("RIP you")
        else:
            print(cigs_per_hour, "cigs per hour by breathing")
            print("1 cig every", hours_per_cig, unit_of_time)
    else:
        print("No it's not lmao.")

if len(sys.argv) == 2:
    pm25 = 22.0  # 1 cig per day
    try:
        concentration = float(sys.argv[1])  # PM2.5 concentration in the air
        analyze_air(concentration)
    except:
        print("Wtf man, give me your AQI")
else:
    print("Get your cigs by calling me with your air AQI like 'python cigs_by_breathing.py 134'")
