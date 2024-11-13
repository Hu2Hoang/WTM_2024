import pyrebase
import bmpsensor
from gps2 import *
# from firebase_admin import db
config = {
 "apiKey":"AIzaSyCCsryyC8xhyGvv0AZH6JeBrgixMedzUwQ",
 "authDomain":"gsc-ptit-2023.firebaseapp.com",
 "databaseURL":"https://gsc-ptit-2023-default-rtdb.asia-southeast1.firebasedatabase.app",
 "storageBucket":"gsc-ptit-2023.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
i=1
while True:
    lat,lon,metter,check=get_gps()
    temp, pressure, alti = bmpsensor.readBmp180()
    bool_gps=bool(db.child("fly").child().get())
    if(check==True):
        name="loc_"+str(i)
        db.child("fly").child(name).update({"pressure":float(pressure)})
        db.child("fly").child(name).update({"temp":float(temp)})
        db.child("fly").child(name).update({"lon":float(lon)})
        db.child("fly").child(name).update({"lat":float(lat)})
        db.child("fly").child(name).update({"alti":float(alti)})
        i+=1
        if(i==4):
            break