import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
sensor_pin = 17  # Adjust to the actual GPIO pin you've connected the sensor to

# Initialize the GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

def read_ir_sensor_value():
    try:
        ir_sensor_value = GPIO.input(sensor_pin)
        return ir_sensor_value
    except Exception as e:
        print(f"Error reading IR sensor: {str(e)}")
        return None

# Example usage
try:
    while True:
        value = read_ir_sensor_value()
        if value is not None:
            if value == GPIO.HIGH:
                print("Obstacle detected")
            else:
                print("No obstacle")
        time.sleep(1)


except KeyboardInterrupt:
    print("Stopped by the user")

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()
