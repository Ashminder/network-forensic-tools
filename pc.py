

import dpkt 
import socket
import os
#os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
PACP_FILE=raw_input("FILE PATH")
fname=raw_input("Enter the filename u want to save the Info. :")
os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
fil=open(fname+".txt","w+")
def printPcap(pcap): 
	for (ts, buf) in pcap:
		try:   
			eth = dpkt.ethernet.Ethernet(buf)   
			ip = eth.data   
			# read the source IP
			src = socket.inet_ntoa(ip.src)
			# read the dst ip is dst
			dst = socket.inet_ntoa(ip.dst)
			fil.write("\nsrc:"+src+"  dest:"+dst)

			

		except:   
			pass 
def main(): 
	f=open(PACP_FILE,'rb')
	
	
	pcap = dpkt.pcap.Reader(f) 
	printPcap(pcap)
	print "FILE IS CREATED AT YOUR DESKTOP"
#if __name__ == '__main__': 
#	main()

