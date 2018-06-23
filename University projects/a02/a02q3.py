import check

# Useful constants for pressure trends
steady = "Steady"
rising_s = "Rising Slowly"
rising_f = "Rising Quickly"
falling_s = "Falling Slowly"
falling_f = "Falling Quickly"

# Useful constants for forecasts
no_change = "No Change"
sun = "Sunny"
storm = "Storms"
tornado = "Tornado Watch"
wind = "Windy"
rain = "Rain"
cloud = "Cloudy"

# weather_forcast(pressure, trend) returns the incoming weather condition
# by measuring the current pressure and the tendency of change of the pressure
# weather_forcast: Float String -> String
# requires: 80.0 <= pressure <= 120.0
# Example: weather_forcast(101.7,"Falling Slowly") => "Rain"

def weather_forecast(pressure,trend):
    if pressure > 103.0:
        pressure = "High"
    elif pressure < 100.0:
        pressure = "Low"
    else:
        pressure = "Moderate"
    if trend == steady:
        return no_change
    elif trend == rising_s:
        if pressure == "Low":
            return no_change
        elif pressure == "Moderate":
            return sun
        else:
            return sun
    elif trend == rising_f:
        if pressure == "Low":
            return sun
        elif pressure == "Moderate":
            return wind
        else:
            return sun
    elif trend == falling_s:
        if pressure == "Low":
            return storm
        elif pressure == "Moderate":
            return rain
        else:
            return no_change
    else:
        if pressure == "Low":
            return tornado
        elif pressure == "Moderate":
            return storm
        else:
            return cloud

# Tests:
check.expect("Q3T1", weather_forecast(95.4, "Rising Slowly"), "No Change")
check.expect("Q3T2", weather_forecast(98.4, "Rising Quickly"), "Sunny")
check.expect("Q3T3", weather_forecast(98.7, "Falling Slowly"), "Storms")
check.expect("Q3T4", weather_forecast(83.5, "Falling Quickly"), "Tornado Watch")
check.expect("Q3T5", weather_forecast(100.0, "Rising Slowly"), "Sunny")
check.expect("Q3T6", weather_forecast(101.8, "Rising Quickly"), "Windy")
check.expect("Q3T7", weather_forecast(101.4, "Falling Slowly"), "Rain")
check.expect("Q3T8", weather_forecast(103.0, "Falling Quickly"), "Storms")
check.expect("Q3T9", weather_forecast(104.5, "Rising Slowly"), "Sunny")
check.expect("Q3T10", weather_forecast(104.5, "Rising Quickly"), "Sunny")
check.expect("Q3T11", weather_forecast(104.5, "Falling Slowly"), "No Change")
check.expect("Q3T12", weather_forecast(104.5, "Falling Quickly"), "Cloudy")
check.expect("Q3T13", weather_forecast(109.5, "Steady"), "No Change")
check.expect("Q3T14", weather_forecast(102.5, "Steady"), "No Change")
check.expect("Q3T15", weather_forecast(96.5, "Steady"), "No Change")