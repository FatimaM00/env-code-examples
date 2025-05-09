def calculate_average(temps):
    total = sum(temps)
    count = len(temps)     
    average = total / count 
    return average

stations = [['A1', 62], ['B5', 97], ['C3', 155]]
for station in stations:
    print(station[0] + " → " + str(station[1]))
  
def report_status(stations, threshold):
    for station in stations:
        station_id = station[0]
        pm25 = station[1]
        if pm25 < threshold:
            print(station_id + " → " + str(pm25) + " ug/m3 (safe)")
        else:
            print(station_id + " → " + str(pm25) + " ug/m3 (DANGER)")

report_status(stations, 100)
