import serial
import time


LOG_FRQ = 5

################# LOG

def initialize_serial_connection(port='/dev/ttyUSB2', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud.")
        return ser
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

def send_at_command(ser, command, delay=0.5):
    ser.write((command + '\r\n').encode())
    time.sleep(delay)
    if ser.in_waiting > 0:
        response = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
        return response
    return ""

def get_network_delay(ser):
    print("Measuring network delay...")
    start_time = time.time()
    response = send_at_command(ser, 'AT+COPS?')
    delay = time.time() - start_time
    if "OK" in response:
        return delay
    return None

def get_connection_type(ser):
    print("Getting connection type...")
    response = send_at_command(ser, 'AT+COPS?')
    if '+COPS:' in response:
        # Parse the response to extract the connection type (e.g., LTE, GSM)
        try:
            access_technology = int(response.split(",")[-1])
            if access_technology == 0:
                return "GSM"
            elif access_technology == 2:
                return "UTRAN (3G)"
            elif access_technology == 7:
                return "LTE"
            else:
                return f"Unknown (Code: {access_technology})"
        except Exception as e:
            print(f"Error parsing connection type: {e}")
            return "Unknown"
    return "Failed to retrieve connection type."

def log_gps_and_network_data(port='/dev/ttyUSB2'):
    ser = initialize_serial_connection(port)
    if not ser:
        return
    try:
        while True:                
            # Network Delay Measurement
            network_delay = get_network_delay(ser)
            
            # Connection Type
            connection_type = get_connection_type(ser)
            log_entry = {}
            
            if network_delay is not None:
                log_entry['network_delay'] = f"Network Delay: {network_delay:.2f} seconds\n"

            if connection_type:
                log_entry['connection_type'] = f"Connection Type: {connection_type}\n"

            time.sleep(10)  # Log every 10 seconds            
            return log_entry
    except KeyboardInterrupt:
        print("Logging stopped.")
    finally:
        ser.close()

if __name__ == '__main__':
    log_gps_and_network_data()
