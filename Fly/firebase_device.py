from firebase_solve_gps import *
import pyrebase
# from firebase_admin import db
config = {
 "apiKey":"AIzaSyCCsryyC8xhyGvv0AZH6JeBrgixMedzUwQ",
 "authDomain":"gsc-ptit-2023.firebaseapp.com",
 "databaseURL":"https://gsc-ptit-2023-default-rtdb.asia-southeast1.firebasedatabase.app",
 "storageBucket":"gsc-ptit-2023.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def push_data(mac_temp,dis_temp):
    # i=1
    data_devices = db.child("device").get()
    check=False
    bool_gps=bool(db.child("fly").child().get())
    dis_cnt=""
    for addr in data_devices.each():
        if(addr.val()["mac_addr"]==mac_temp):
            check=True
            key=addr.key()
            cnt=addr.val()["cnt"]
            print(str(cnt))
            if(cnt==5):
                break
            if(cnt==4):
                dis_1=addr.val()["dis_1"]
                dis_2=addr.val()["dis_2"]
                dis_3=addr.val()["dis_3"]
                lat,lon,alti=solve_gps(dis_1,dis_2,dis_3)
                db.child("device").child(key).update({"lat":lat})
                db.child("device").child(key).update({"lon":lon})
                db.child("device").child(key).update({"alti":alti})
                db.child("device").child(key).update({"cnt":cnt+1})
            if(bool_gps==True and cnt<=3):
                print(bool_gps)
                dis_cnt="dis_"+str(cnt)
                db.child("device").child(key).update({dis_cnt:dis_temp})
                db.child("device").child(key).update({"cnt":cnt+1})
                break
    if check==False:
        new_data={"mac_addr":mac_temp,"dis_1":dis_temp,"dis_2":1,"dis_3":1,"cnt":1,"lat":1,"lon":1,"alti":1}
        db.child("device").push(new_data)
