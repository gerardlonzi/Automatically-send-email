##################### Extra Hard Starting Project ######################
import pandas as pd
import random as rd
import smtplib 


data = []
for i in range(1,4):
    with open(f"./letter_templates/letter_{i}.txt",'r') as file:
        text = file.read()
        text.strip()
        data.append(text)
        
       
# 1. Update the birthdays.csv

pd = pd.read_csv('birthdays.csv')
print(pd)

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
dt = dt.datetime.now()

my_email = "lonzigerard@gmail.com"
password = "nmqorvkchuhtbpsc"

for (i,row) in pd.iterrows():
     if dt.day == row.day and dt.month == row.month:
         choice = rd.choice(data)
         message = choice.replace('[NAME]',f"{pd['name'][row.name]}")
         connect = smtplib.SMTP('smtp.gmail.com')
         connect.starttls()
         connect.login(user=my_email,password=password)
         connect.sendmail(from_addr=my_email, to_addrs= f"{row.email}", msg=f"Subject:Happy Birthday\n\n {message}" )
         
        

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.




