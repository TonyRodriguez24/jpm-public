import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(api_key, from_email, to_email, subject, content):
    """This handles the sending of an email through sendgrids API client"""

    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    email = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )  # type: ignore

    try:
        # Send the email and get the response
        response = sg.send(email)
        
        # Log detailed response for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.body.decode('utf-8') if response.body else 'No body content'}")
        print(f"Headers: {response.headers}")

        # Check if the status code is 202 (success)
        if response.status_code != 202:
            raise Exception(f"Email failed to send with status code: {response.status_code}")
        
        return response  # Return the full response object

    except Exception as err:
        # Log the error and return None for further debugging
        print(f"An error has occurred: {err}")
        return None  # Return None if an error occurs