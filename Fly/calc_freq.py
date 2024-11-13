from math import *
sum_mac = {}
cnt = {}
avg = {}
data = {}

def add(mac, freq):
    if(mac in sum_mac) :
        sum_mac[mac] = sum_mac[mac] + freq
    else:
        sum_mac[mac] = freq
    if(mac in cnt) :
        cnt[mac] = cnt[mac] + 1
    else:
        cnt[mac] = 1
    
    for mac in sum_mac:
        avg[mac] = (sum_mac[mac]/cnt[mac])


    return avg[mac]



