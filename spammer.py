from posixpath import split
from random import randint
import smtplib
import time

with open("copypastas.txt", "r", encoding = "utf-8") as f:
    copypastas = f.read()
copypastasList = copypastas.split(">>>>")



with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('uravspare@gmail.com', 'lnppowmkuuptzweq')
    
    while True:
        try:     
            pastaRaw = copypastasList[randint(0,len(copypastasList))].split(";;;;")
            subject = pastaRaw[1]
            body = pastaRaw[2]
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail('uravspare@gmail.com', 'uravspare3@gmail.com', msg.encode("utf-8"))
            time.sleep(1)
        except:
            continue

