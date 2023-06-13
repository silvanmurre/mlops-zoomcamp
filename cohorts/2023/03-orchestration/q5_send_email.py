from prefect import flow
from prefect_email import EmailServerCredentials, email_send_message


@flow
def send_email_hw_m3_q5():
    email_server_credentials = EmailServerCredentials.load("my-email")
    email_send_message(
        email_server_credentials=email_server_credentials,
        email_to=email_server_credentials.username,
        subject="[mlops-zoomcamp homework] 03-orchestration question 5",
        msg="Hi! You succesfully finished question 5."
    )


if __name__ == "__main__":
    send_email_hw_m3_q5()
