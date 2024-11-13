from math import *
from algr_locate import *
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

# locate=calc_locate(1,0,0,3.162277,0,2,0,3.605551,4,3,0,5.830951,0.0001)

loc_1 = db.child("fly").child("loc_1").get()
alti_1=loc_1.val()["alti"]
lon_1=loc_1.val()["lon"]
lat_1=loc_1.val()["lat"]

loc_2 = db.child("fly").child("loc_2").get()
alti_2=loc_2.val()["alti"]
lon_2=loc_2.val()["lon"]
lat_2=loc_2.val()["lat"]

loc_3 = db.child("fly").child("loc_3").get()
alti_3=loc_3.val()["alti"]
lon_3=loc_3.val()["lon"]
lat_3=loc_3.val()["lat"]

def solve_gps(dis_1,dis_2,dis_3):
    print(dis_1,dis_2,dis_3)
    x,y,z=calc_locate(lat_1,lon_1,alti_1,dis_1,lat_2,lon_2,alti_2,dis_2,lat_3,lon_3,alti_3,dis_3,0.0001)
    return x,y,z

# for gps in data_gps_1.each():
#     alti_1=(gps.val()["alti"])
    # cnt=addr.val()["cnt"]
    # lat_1=float(gps.val()["lat"])
    # lon_1=float(gps.val()["lon"])
    # alti_1=float(gps.val()["alti"])

# print(lat_1,' ',lon_1,' ',alti_1,'\n')
# print(lat_2,' ',lon_2,' ',alti_2,'\n')
# print(lat_3,' ',lon_3,' ',alti_3,'\n')

# print(solve_gps(4.36,5.18,3.56))