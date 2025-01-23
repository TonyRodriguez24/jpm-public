import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(api_key, from_email, to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    email = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )  # type: ignore

    try:
        response = sg.send(email)
        
        # Log detailed response for debugging
        print("Status Code:", response.status_code)
        print("Response Body:", response.body.decode("utf-8") if response.body else "No body content")
        print("Headers:", response.headers)

        if response.status_code != 202:  # 202 is the expected success code
            raise Exception(f"Email failed with status code: {response.status_code}")
        
        return response.status_code

    except Exception as err:
        # Log the error and return it for further debugging
        print(f"An error has occurred: {err}")
        return f"An error has occurred: {err}"
