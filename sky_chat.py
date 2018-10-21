import sqlite3
import pdb
import os
def printProfile(skypeDB):
    #os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
    conn=sqlite3.connect(skypeDB)
    c = conn.cursor()
    os.chdir("C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL")
    fname=raw_input("Enter the filename u want to save the Info. :")
    f=open(fname+".txt","w+")
    c.execute("SELECT author, body_xml FROM messages;")
    for row in c:
        print '[*] -- CHAT FOUND --'
        print '[+] author: '+str(row[0])
        print '[+] Skype chat: '+str(row[1])
        f.write('\n\n[+] author: '+str(row[0]+'   [-] Skype chat: '+str(row[1])))
       

                
def main():
    skypeDB="C:\Users\Singh_Ashminder\Desktop\PRJT(FORENSICS_TOOL\DATABASES\main.db"
    printProfile(skypeDB)
    print "YOUR FILE IS CREATED AT YOUR DESKTOP"
#if __name__ == "__main__":
 #   main()
