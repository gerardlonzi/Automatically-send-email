##################### Extra Hard Starting Project ######################
import pandas as pd
import random as rd
import smtplib 

## 1. Ajout du contenu des fichiers dans un tableau
data = []
for i in range(1,4):
    with open(f"./letter_templates/letter_{i}.txt",'r') as file:
        text = file.read()
        text.strip()
        data.append(text)
        
       
# 2. lecture du fichiers birthdays.csv avec pandas

pd = pd.read_csv('birthdays.csv')
print(pd)

# 3. importation du module DataTime
import datetime as dt
dt = dt.datetime.now()

# 4. Saisir l'email d'envoie
my_email = "entree une adresse email"
password = "Activer la verification en deux etapes dans votre compte google ,cliquer sur choisir un appariels et saisir le code proposer"

# 5. verifier si la date corespond a la date d'aujourd'hui
for (i,row) in pd.iterrows():
     if dt.day == row.day and dt.month == row.month:
         choice = rd.choice(data)
         message = choice.replace('[NAME]',f"{pd['name'][row.name]}")
         connect = smtplib.SMTP('smtp.gmail.com')
         connect.starttls()
         connect.login(user=my_email,password=password)
         connect.sendmail(from_addr=my_email, to_addrs= f"{row.email}", msg=f"Subject:Happy Birthday\n\n {message}" )
         
        




