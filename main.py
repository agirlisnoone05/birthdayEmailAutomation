import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL= ""
PASSWORD= ""

now = dt.datetime.now()
today = (now.month,now.day)


df = pd.read_csv("birthdays.csv")

birthdaysdict = {
    (data_row["month"],data_row["day"]):data_row for (index, data_row) in df.iterrows()
}
if today in birthdaysdict:
    birthday_person = birthdaysdict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
         contents = letter_file.read()
         contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection: #simple mail transfer protocol
        connection.starttls() #transport layer security
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: HAPPY BIRTHDAY!!\n\n{contents}"
        )



