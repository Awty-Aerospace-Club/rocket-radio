# receiver.py's purpose is to decode serialized data from the Arduino, then write it to csv
from csvquery import open_csv
from math import degrees
from serial import Serial, SerialException

fields = [
    "time",
    "altitude",
    "accelX",
    "accelY",
    "accelZ",
    "gyroX",
    "gyroY",
    "gyroZ",
]


def serial_ports():
    result = []
    for i in range(1, 257):
        port = f"COM{i}"
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
            pass
    return result


def validate(line):
    try:
        line = line.decode("ASCII")
        assert len(line) > 3 and line.count(",") == len(fields) and line[-2:] == "\r\n"

        line = line[:-3]
        for num in line.split(","):
            float(num)

        return line
    except (AssertionError, ValueError):
        print("[ERROR] received bad data")
        return False


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
    file = open("output.csv", "w+", newline="")

    print(",".join(fields), file=file)
    while True:
        line = s.readline()
        if not line:
            break

        line = validate(line)
        if not line:
            continue

        print(line)
        print(line, file=file)

    file.close()

    dataset = open_csv("output.csv")
    dataset.replace(["gyroX", "gyroY", "gyroZ"], degrees)
    dataset.save_csv("output.csv")


if __name__ == "__main__":
    main()
