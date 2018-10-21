
import os
import pygeoip
ip_tocoun_db='C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL\DATABASES\GeoLiteCity.dat'

gi = pygeoip.GeoIP(ip_tocoun_db)

def printRecord(tgt): 
	
	rec = gi.record_by_name(tgt) 
	
	
	city = rec['city'] 
	region = rec['region_code'] 
	country = rec['country_name'] 
       
	lonng = rec['longitude'] 
	lat = rec['latitude'] 
	print '[*] Target: ' + tgt + ' Geo-located. ' 
	print '[+] '+str(city)+','+str(region)+', '+str(country) 
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(lonng)
	
        


def main():
 IP=str(raw_input("ENTER THE IP :"))
 printRecord(IP)
#if __name__ == "__main__":
#	main()
