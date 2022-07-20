import os

# AWS SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get("REKOGNITION_AWS_ACCESS_KEY_ID") or os.environ.get(
    "AWS_ACCESS_KEY_ID"
)
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "REKOGNITION_AWS_SECRET_ACCESS_KEY"
) or os.environ.get("AWS_SECRET_ACCESS_KEY")
