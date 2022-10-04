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

    def compare_faces(self, image_origin, image_compare):
        return rekognition_client.compare_faces(
            SourceImage={"Bytes": image_origin},
            TargetImage={"Bytes": image_compare},
        )

    def detect_text(self, image):
        return rekognition_client.detect_text(Image={"Bytes": image})

    def detect_labels(self, image, min_confidence=55):
        return rekognition_client.detect_labels(
            Image={"Bytes": image},
            MaxLabels=123,
            MinConfidence=min_confidence,
        )


class KYCValidate(HelperBotoClient):
    def convert_url_to_image(self, url):
        return requests.get(url).content

    def validate_label_in_document(self, image, label_name, min_confidence):
        response = self.detect_labels(image, min_confidence)
        return label_name in [label["Name"] for label in response["Labels"]]

    def extract_image_data(self, image):
        return [
            item["DetectedText"] for item in self.detect_text(image)["TextDetections"]
        ]

    def extract_driver_license_data(self, image):
        return self.extract_image_data(image)

    def validate_id_cards(self, image, min_confidence=95):
        return self.validate_label_in_document(image, "Id Cards", min_confidence)

    def validate_driver_license(self, image, min_confidence=95):
        return self.validate_label_in_document(image, "Driving License", min_confidence)

    def validade_faces(self, image_source, image_target, min_confidence=98):
        try:
            return (
                self.compare_faces(image_source, image_target)["FaceMatches"][0][
                    "Similarity"
                ]
                > min_confidence
            )
        except (KeyError, IndexError):
            return False
