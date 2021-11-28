import smtplib, ssl

import smtplib
def alert_mail(mail,d,name):

    a='https://docs.google.com/spreadsheets/d/11xebCcQMXHXinEBhFIjKv0j7WC-dh_rf9FApzmVpNHM/edit?usp=sharing'
    b='https://docs.google.com/spreadsheets/d/1A_5t-jQIzLgINL9jxnmX6trtKxOfUPxJek7L7V2MOB8/edit?usp=sharing'
    c='https://docs.google.com/spreadsheets/d/1DGV-giykyonPN1J3WWBbwvsabMcW_RDunE4LmAzdTqI/edit?usp=sharing'
    vd='https://docs.google.com/spreadsheets/d/1xJCqBfH9j1tnOJHe7ZOSbJIaMavmb9EEHCMA3D4hAAA/edit?usp=sharing'
    e='https://docs.google.com/spreadsheets/d/1lrwmpQxkmcnnrPKLPBWsURISOvk-ZDwmwH8yg7c6NWQ/edit?usp=sharing'
    k='https://docs.google.com/spreadsheets/d/1vMQWV_HnDmUgcfaxRswDfqHRuGL1VozwCsWjViF-5cw/edit?usp=sharing'

    l={}
    for i in d:
        if i=="Vitamin A":
            l[i]=a
        if i=="Vitamin B":
            l[i]=b
        if i=="Vitamin C":
            l[i]=c
        if i=="Vitamin D":
            l[i]=vd
        if i=="Vitamin E":
            l[i]=e
        if i=="Vitamin K":
            l[i]=k

    s = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
    sender_email = "njksnjkqjkn@gmail.com"
    password = 'apple@20'

    s.login(sender_email,password )

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    
        
    print(l)
    print(d)
    msg['From']="njksnjkqjkn@gmail.com"
    msg['To']=mail
    msg['Subject']="VitaMax Vitamin Pills"
    message=f"Dear {name} your vitamin pills intake refer -> {l}"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)


