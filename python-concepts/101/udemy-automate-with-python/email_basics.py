import smtplib


def create_connection():
    return smtplib.SMTP_SSL("smtp.gmail.com", 465)


def email_read():
    email_sender = "jdoe@gmail.com"
    from_address = "jdoe@gmail.com"
    to_address = "jdoe@gmail.com"

    connection = create_connection()
    print(connection.ehlo())
    connection.login(email_sender, "blahblah")
    connection.sendmail(from_address,
                        to_address,
                        'Subject : Python testing \n\n Testing email body \n\n-Jdoe')
    connection.quit()


email_read()