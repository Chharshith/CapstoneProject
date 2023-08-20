import time
import serial  # For communicating with the GSM module
from geopy.geocoders import Nominatim  # For obtaining location coordinates
from detection import read_ir_sensor_value
from Message import Emailer
email = Emailer()
sens=read_ir_sensor_value()
# Initialize the serial connection to the GSM module (adjust the port and baud rate)
ser = serial.Serial('/dev/ttyS0', 9600)

# Initialize the Geolocator
geolocator = Nominatim(user_agent="railway_track_monitor")
threshold_value = 30
latitude = ''
longitude = ''
# Function to read data from actual sensors
def read_sensor_data():
    # Replace with code to read data from your sensors
    # For example, if you are using an IR sensor, read its value
    ir_sensor_value = email.read_ir_sensor_value()

    # Similarly, read values from other sensors (ultrasonic, UV, GPS, etc.)

    return ir_sensor_value, other_sensor_values


while True:
    # Read data from actual sensors
    ir_sensor_value, other_sensor_values = read_sensor_data()

    # Replace the following condition with your logic based on sensor readings
    if ir_sensor_value > threshold_value:
        # Get location information based on latitude and longitude
        location = geolocator.reverse((latitude, longitude))
        location_address = location.address if location else "Location not found"

        # Compose SMS message
        sms_message = f"Alert: Obstacle detected on railway track at {location_address}. Coordinates: Lat={latitude}, Long={longitude}"
        #compose Email
        # email_body = f"Obstacle detected on railway track at {location_address}.Coordinates Lat={latitude}, Long={longitude}"
        # Send SMS using GSM module (AT commands)
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        ser.write('AT+CMGF=1\r\n'.encode())  # Set SMS text mode
        time.sleep(1)
        ser.write(f'AT+CMGS="station_manager_phone_number"\r\n'.encode())  # Replace with station manager's phone number
        time.sleep(1)
        ser.write(f'{sms_message}\r\n'.encode())
        ser.write(chr(26).encode())  # Ctrl+Z to send SMS
        time.sleep(2)

        print("SMS sent to station manager:")
        print(sms_message)
        # email.sendEmail(email_body)
    # Wait for some time before checking sensors again (adjust as needed)
    time.sleep(300)  # Check every 5 minutes


