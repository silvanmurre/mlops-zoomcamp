import os

from dotenv import load_dotenv
from prefect_email import EmailServerCredentials


load_dotenv()

credentials = EmailServerCredentials(
    username=os.getenv("EMAIL-ADDRESS-PLACEHOLDER"),
    password=os.getenv("PASSWORD-PLACEHOLDER"), # must be an app password
)
credentials.save("my-email")