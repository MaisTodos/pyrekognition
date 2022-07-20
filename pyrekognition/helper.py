import boto3
import requests

from pyrekognition.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

rekognition_client = boto3.client(
    "rekognition",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


class HelperBotoClient:
    client = None

    def _convert_url_to_bytes(self, url):
        return requests.get(url).content

    def detect_labels(self, url):
        return rekognition_client.detect_labels(
            Image={"Bytes": self._convert_url_to_bytes(url)}, MaxLabels=123,
        )
