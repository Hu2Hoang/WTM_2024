import io
import serial
import pynmea2
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
lt=[0,0]
lg=[0,0]
maxlt=-1e9
maxlg=-1e9
def compare(a,b,c,d):
    # if(abs(a-b)>=0.00015349999999969555 and abs(c-d)>=1.2666666663108117e-05):
    if(abs(a-b)>=0 and abs(c-d)>=1.2666666663108117e-08):
        return True
    return False
def get_gps():
    while 1:
        try:
            line = sio.readline()
            msg = pynmea2.parse(line)
            if line[0:6] == "$GPGGA":
                newmsg=pynmea2.parse(line)
                lat=newmsg.latitude
                lng=newmsg.longitude
                alti=newmsg.altitude
                lt[0]=lt[1]
                lg[0]=lg[1]
                lt[1]=lat
                lg[1]=lng
                check=bool(db.child("fly").child().get())
                return lat,lng,alti,check
            time.sleep(0.1)
        except serial.SerialException as e:
            return 0,0,0
            break
        except pynmea2.ParseError as e:
            return 0,0,0
            continue  

# 0.00015349999999969555   1.2666666663108117e-05   6.666666685362088e-07   -8.333333312293689e-07
# 20.990995666666667 Longitude=105.7940685
# 20.991029333333334 Longitude=105.79402516666667