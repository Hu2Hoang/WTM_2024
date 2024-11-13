
import time
import datetime as dt
import argparse
import netaddr
import sys
import logging
import math
from algr_locate import *
from calc_freq import *
from firebase_device import *
from decimal import *
from scapy.all import *
from scapy.all import RadioTap
from scapy.all import sniff
from pprint import pprint
from logging.handlers import RotatingFileHandler


NAME = 'GSC_PTIT_2023'
DESCRIPTION = "Finding people using Wifi probe quest"

DEBUG = False

parsed_mac=""
rssi_val=0
res_dis=0
def build_packet_callback(mac_info, rssi, distance):
	global parsed_mac,rssi_val,res_dis
	def packet_callback(packet):
		global parsed_mac,rssi_val,res_dis
		if not packet.haslayer(Dot11):
			return
		# we are looking for management frames with a probe subtype
		# if neither match we are done here
		if packet.type != 0 or packet.subtype != 0x04:
			return
		parsed_mac=""
		if mac_info:
			try:
				parsed_mac = netaddr.EUI(packet.addr2)
			except netaddr.core.NotRegisteredError as e:
				fields.append('UNKNOWN')

		# include the SSID in the probe frame
		res_dis=0
		if rssi:
			radiotap = packet.getlayer(RadioTap)
			rssi_val = radiotap.dBm_AntSignal
			avg_freq=add(parsed_mac, rssi_val)
			if rssi_val:
				distance=float(pow(10,((-42.4)-(rssi_val))/(10*2.3)))
				res_dis=distance
		mac_temp=str(parsed_mac)
		print(mac_temp,' ',rssi_val,' ',res_dis)
		# print(type(mac_temp))
		push_data(mac_temp,res_dis)
		# return res_dis
	return packet_callback
	# return parsed_mac,res_dis

# Note: iface we use is define with wlan0mon with monitor mode
def main():
	built_packet_cb = build_packet_callback( "True", "True", "True")
	sniff(iface="wlan0mon", prn=built_packet_cb, store=0)
if __name__ == '__main__':
	main()


