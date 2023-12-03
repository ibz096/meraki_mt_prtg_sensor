# Meraki MT Sensor Integration

This Python script serves as a custom sensor for PRTG (Paessler AG) and is specifically designed to fetch sensor readings from Cisco Meraki MT (MT - Meraki MT Sensors) devices. The script utilizes the Meraki API to obtain sensor data based on the provided organization ID and API key.

## Prerequisites
1. Obtain a valid Cisco Meraki API key.
2. Replace `<APIKEY>` in the script with your actual Meraki API key.
3. Replace `<orgID>` in the script with your organization's ID.
4. Ensure that the required Python modules (`requests`, `json`, `paesslerag_prtg_sensor_api`) are installed.

## Usage
1. Execute the script with the appropriate PRTG parameters.
   ```bash
   python meraki_sensor.py '{"params": "<rackId>"}'
   ```
   Replace `<rackId>` with the specific rack identifier.

### Additional Parameters
You can pass additional parameters to customize the behavior of the script. Here's an example of how to include additional parameters:

```bash
python meraki_sensor.py '{"params": "<rackId>", "additional_param": "<value>"}'
```

Replace `<value>` with the specific value for the additional parameter.

## Supported Devices
This script is tailored to fetch sensor readings specifically for Cisco Meraki MT devices. It may not work as intended for other Meraki device types.

## Script Overview
- The script constructs the Meraki API URL based on the provided organization ID, API key, and rack identifier.
- It performs a GET request to retrieve sensor data from the Meraki API.
- The script then processes the received JSON data, extracting relevant information such as serial number, network ID, network name, and sensor readings.
- PRTG-compatible JSON is created, including channels for battery percentage, humidity percentage, and temperature in both Celsius and Fahrenheit.
- The resulting JSON is printed to the console, which PRTG can parse and display appropriately.

## Error Handling
In case of any exceptions during script execution, an error message is generated and printed in the PRTG-compatible JSON format.

**Note:** Ensure that the script is configured with accurate Meraki API credentials and organization details before use. This script is specifically designed for Meraki MT devices; compatibility with other Meraki devices may vary.