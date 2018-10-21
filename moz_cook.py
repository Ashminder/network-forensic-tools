
import pdb
import sqlite3
import os


def printCook(cookiesDB):
	try:
		conn = sqlite3.connect(cookiesDB)
		c = conn.cursor()
		os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
		fname=raw_input("Enter the filename u want to save the Info. :")
		f=open(fname+".txt","w+")
		c.execute("Select id,baseDomain,host from moz_cookies;")
		print '\n[*] -- Found COOKIES --'
		for row in c:
			id_i = str(row[0])
			base = str(row[1])
			host = str(row[2])
			print '[+] ' + id_i + ' - BASE: ' + base+' -HOST: '+host
			f.write('\n[+] ' + id_i + ' - BASE: ' + base+' -HOST: '+host)
	except Exception, e:
		if 'encrypted' in str(e):
			print '\n[*] Error reading your places database.'
			print '[*] Upgrade your Python-Sqlite3 Library'
			exit(0)

def main():
	
	
	cookiesDB="C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL\DATABASES\cookies.sqlite"
	

	printCook(cookiesDB)
	print "\n\nFILE IS CREATED AT YOUR DESKTOP"

#if __name__ == "__main__":
#	main()
