import pdb
import sqlite3
import os


def printHistory(placesDB):
	try:
		conn = sqlite3.connect(placesDB)
		c = conn.cursor()
		os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
		fname=raw_input("Enter the filename u want to save the Info. :")
		f=open(fname+".txt","w+")

		c.execute("select url, datetime(visit_date/1000000, \
		'unixepoch') from moz_places, moz_historyvisits \
		where visit_count > 0 and moz_places.id==\
		moz_historyvisits.place_id;")
		print '\n[*] -- Found History --'
		for row in c:
			url = str(row[0])
			date = str(row[1])
			print '[+] ' + date + ' - Visited: ' + url
			f.write('\n[+] ' + date + ' - Visited: ' + url)
	except Exception, e:
		if 'encrypted' in str(e):
			print '\n[*] Error reading your places database.'
			print '[*] Upgrade your Python-Sqlite3 Library'
			exit(0)

def main():
	
	
	placesDB="C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL\DATABASES\places.sqlite"
	

	printHistory(placesDB)
	print "\n\nYOUR FILE IS CREATED AT DESKTOP"

#if __name__ == "__main__":
#	main()
