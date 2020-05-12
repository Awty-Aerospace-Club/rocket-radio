# receiver.py's purpose is to decode serialized data from the Arduino, then write it to csv
from serial import Serial, SerialException

def serial_ports():
    result = []
    for i in range(1, 257):
        port = f"COM{i}"
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
           print(f"error: {OSError}; {SerialException}") 
    return result

def main():
    print()
    ports = serial_ports()
    if len(ports) == 0:
        print("No ports found")
        exit(-1)

    port = ports[0]
    if len(ports) > 1:
        print("Multiple ports found, select one:")
        print(", ".join(ports))
        port = input(">> ")
    else:
        print(f"Selected only available port: {port}")

    s = Serial(port)
    s.write("a".encode("ASCII"))

    while True:
        line = s.readline()
        if not line:
            break
        ping = int(line.decode("ASCII"))
        print(f"ping: {ping}")
        s.write("a".encode("ASCII"))
        s.readline()


if __name__ == "__main__":
    main()
