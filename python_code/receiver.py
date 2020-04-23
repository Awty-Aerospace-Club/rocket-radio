# receiver.py's purpose is to unencode received serialized data from the arduino, then write it to csv
import serial, csvquery, math

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
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

print()
ports = serial_ports()
if len(ports) == 0:
    print("No ports found")
    exit(0)

port = ports[0]
if len(ports) > 1:
    print("Multiple ports found, select one:")
    print(", ".join(ports))
    port = input(">> ")
else:
    print(f"Selected only available port: {port}")

s = serial.Serial(port)
file = open("output.csv", "w+", newline="")

def validate(line):
    try:
        line = line.decode("ASCII")
        assert len(line) > 3 and line.count(",") == len(fields) and line[-2:] == "\r\n"
        
        line = line[:-3]
        for num in line.split(","):
            float(num)
        
        return line
    except:
        print("[ERROR] received bad data")
        return False
        

print(",".join(fields), file=file)
while True:
    line = s.readline()
    if not line: break

    line = validate(line)
    if not line: continue

    print(line)
    print(line, file=file)

file.close()

# once the code gets here, arduino is unplugged and the mission is over, time for data analysis

dataset = csvquery.open_csv("output.csv")
dataset.replace(["gyroX", "gyroY", "gyroZ"], math.degrees)
dataset.save_csv("output.csv")