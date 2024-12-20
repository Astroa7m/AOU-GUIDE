import smtplib
from email.message import EmailMessage

from langchain_core.tools import Tool
from pydantic import BaseModel
email_sending_json_format ="""{
'Email': 'here comes the email',
'EmailAppPassword': 'here comes the email app password',
'Subject': 'Here comes the subject',
'Content': 'Here comes the content',
'Recipient': 'Here comes the recipient email'
}""".strip().replace("\n", "")


print(email_sending_json_format)

# Define input model for sending email
class SendEmailInput(BaseModel):
    email: str
    password: str
    subject: str
    content: str
    recipient: str

# Function to send email
def send_email(input_data: SendEmailInput) -> str:
    # email = "fake.dr.abrar@outlook.com"
    # password = "ItsFake8DoctorAbrar"
    print("\nBEGINNING OF THE INPUT")
    for item in input_data.split():
        print(item)
    print("END OF THE INPUT")



    try:
        formatted_input = eval(input_data)

        print("printing vars")
        email = formatted_input['Email']
        password = formatted_input['EmailAppPassword']
        subject = formatted_input['Subject']
        content = formatted_input['Content']
        recipient = formatted_input['Recipient']

        # Initialize Outlook

        msg = EmailMessage()
        msg["From"] = email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(content)

        # Connect to Outlook's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(email, password)
            server.send_message(msg)


        print(f"Email sent to {recipient} successfully!")

        return f"Email sent to {recipient}!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

# Register tool
send_email_tool = Tool.from_function(
    func=send_email,
    name="send_email",
    description=f"Sends an email. Provide subject, content, and recipient email. In the following JSON format\n{email_sending_json_format}\nNote that the email and email app password of the sender is included within the context"
)

tools = [send_email_tool]
