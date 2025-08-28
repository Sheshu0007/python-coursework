import email_automation
rec_mail=input("enter the email")
subject=input("enter the subject:")
body=input("enter the body:")

csv_file=input("enter the path of file ")
email_automation.send_bulk_emails(csv_file,subject,body)ol