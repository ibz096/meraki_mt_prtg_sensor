import requests
import sys
import json

from paesslerag_prtg_sensor_api.sensor.result import CustomSensorResult
from paesslerag_prtg_sensor_api.sensor.units import ValueUnit


if __name__ == "__main__":
    try:
        url = "https://api.meraki.com/api/v1/organizations/<orgID>/sensor/readings/latest?serials[]="

        headers = {
            'X-Cisco-Meraki-API-Key': '<APIKEY>'
        }
        prtg_data = json.loads(sys.argv[1])
        
        serialNumber = prtg_data["params"]

        url += serialNumber

        # Make the GET request with custom headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Your JSON response string
            data = response.json()

            # Accessing elements in the parsed data
            serial = data[0]['serial']
            network_id = data[0]['network']['id']
            network_name = data[0]['network']['name']
            readings = data[0]['readings']

            #Create PRTG-compatible JSON
            csr = CustomSensorResult(text="This sensor runs on Meraki")
            # Accessing readings data
            for reading in data[0]['readings']:
                timestamp = reading['ts']
                metric = reading['metric']

                if metric == 'battery':
                    battery_percentage = reading['battery']['percentage']
                    csr.add_channel(name="Battery",
                                value=battery_percentage,
                                unit=ValueUnit.PERCENT)
                elif metric == 'humidity':
                    humidity_percentage = reading['humidity']['relativePercentage']
                    csr.add_channel(name="Humidity",
                                    value=humidity_percentage,
                                    unit=ValueUnit.PERCENT)
                elif metric == 'temperature':
                    temperature_celsius = reading['temperature']['celsius']
                    csr.add_channel(name="Temp.(Celsius)",
                                value=temperature_celsius,
                                unit=ValueUnit.TEMPERATURE)
                    temperature_fahrenheit = reading['temperature']['fahrenheit']
                    csr.add_channel(name="Temp.(Fahrenheit)",
                                value=temperature_fahrenheit,
                                unit=ValueUnit.TEMPERATURE)
            
            # Print the PRTG-compatible JSON
            print(csr.json_result)
    
    except Exception as e:
        csr = CustomSensorResult(text="Python Script execution error")
        csr.error = "Python Script execution error: %s" % str(e)
        print(csr.json_result)