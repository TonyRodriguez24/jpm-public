import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(api_key, from_email, to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    email = Mail(from_email = from_email, to_emails = to_email, subject = subject, html_content = content) # type: ignore

    try:
        response = sg.send(email)
        return response.status_code
    
    except Exception as err:
        return f"An error has occurred: {err}"
    
