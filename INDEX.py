import sqlite3
import moz_cook
import moz_his
import sky_chat

import sqlconn
import ipt
#import pc


         
def indmain():
 print"--------------------------------------"   
 print "WANNA KNOW THE DETAILS ABOUT :\n1.FIREFOX Website Visited\n2.Cookies Generated\n3.SKYPE User Logged In\n4.Chats NETWORK\n5.Ip Location \n6.Source & Dest IP Extractor\ne-exit"
 opt =str(raw_input("enter the choice:"))
 if opt == '1':
              moz_his.main()
 if opt == '2':
              moz_cook.main()

 if opt == '3':
              sqlconn.main()
 if opt == '4':
              sky_chat.main()
 if opt == '5':
              ipt.main()
 if opt == '6':
              import pc
              pc.main()
 if opt != 'e':
              indmain()

if __name__ == "__main__":
	indmain()
