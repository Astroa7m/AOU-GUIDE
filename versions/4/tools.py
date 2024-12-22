import smtplib
from email.message import EmailMessage

from langchain_core.tools import Tool, tool
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
@tool
def send_email(input_data: SendEmailInput) -> str:
    """
    Sends an email. Provide subject, content, and recipient email. In the following JSON format\n{email_sending_json_format}\nNote that the email and email app password of the sender is included within the context
    :param input_data:
    :return:
    """
    # email = "fake.dr.abrar@outlook.com"
    # password = "ItsFake8DoctorAbrar"
    # print("\nBEGINNING OF THE INPUT")
    # for item in input_data.split():
    #     print(item)
    # print("END OF THE INPUT")

    print("Received email")
    print(input_data.email)
    print("Received password")
    print(input_data.password)
    print("Received recipient")
    print(input_data.recipient)
    print("Received subject")
    print(input_data.subject)
    print("Received content")
    print(input_data.content)


    try:
        # formatted_input = eval(input_data)

        # print("printing vars")
        # email = formatted_input['Email']
        # password = formatted_input['EmailAppPassword']
        # subject = formatted_input['Subject']
        # content = formatted_input['Content']
        # recipient = formatted_input['Recipient']

        # Initialize Outlook

        msg = EmailMessage()
        msg["From"] = input_data.email
        msg["To"] = input_data.recipient
        msg["Subject"] = input_data.subject
        msg.set_content(input_data.content)

        # Connect to Outlook's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(input_data.email, input_data.password)
            server.send_message(msg)


        print(f"Email sent to {input_data.recipient} successfully!")

        return f"Email sent to {input_data.recipient}!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

# Register tool
send_email_tool = Tool.from_function(
    func=send_email,
    name="send_email",
    description=f"Sends an email. Provide subject, content, and recipient email. In the following JSON format\n{email_sending_json_format}\nNote that the email and email app password of the sender is included within the context"
)

tools = [send_email_tool]
