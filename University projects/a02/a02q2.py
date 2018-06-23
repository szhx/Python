import check
import math

# feels_like(temp, wind, hum) returns the temperature that you feels like 
# during the day in Canada, and the humidity and the wind chill factors are 
# considered
# feels_like: Float Float Nat -> Float 
# requires: wind(wind_speed) >= 0
#           0 <= hum <= 100
# Example:  feels_like(-9.5,1.9,91) => -9.5

def feels_like(temp, wind, hum):
    windchill = 13.12 + 0.6125 * temp - 11.37 * (wind ** 0.16) +0.3965 * temp * (wind ** 0.16)
    vapour_pressure = 6.112 * (10 ** ((7.5 * temp) / (237.7 + temp))) * (hum / 100)
    humidex = temp + (5 / 9) * (vapour_pressure - 10)
    if temp <= humidex + 1 and temp >= 15:
        feeling = humidex
    elif temp >= windchill + 1 and temp < 15:
        feeling = windchill
    else:
        feeling = temp
    return feeling

# Tests:
check.within("Q2T1", feels_like(-9.5, 1, 91), -9.5, 0.001)  
check.within("Q2T2", feels_like(20.1, 1.9, 12), 20.1, 0.001)
check.within("Q2T3", feels_like(13.5, 100, 13), 8.817, 0.001)
check.within("Q2T4", feels_like(13.5, 1, 13), 13.5, 0.001)
check.within("Q2T5", feels_like(13.5, 19, 91), 11.750, 0.001)

