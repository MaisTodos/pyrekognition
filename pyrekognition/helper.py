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
    
    def compare_faces(self, url_origin, url_compare):
        return rekognition_client.compare_faces(
            SourceImage={'Bytes': self._convert_url_to_bytes(url_origin)},
            TargetImage={'Bytes': self._convert_url_to_bytes(url_compare)},
        )
    
    def detect_text(self, url):
        return rekognition_client.detect_text(
            Image={'Bytes': self._convert_url_to_bytes(url)}
        )
        
    def detect_labels(self, url, min_confidence=55):
        return rekognition_client.detect_labels(
            Image={"Bytes": self._convert_url_to_bytes(url)},
            MaxLabels=123,
            MinConfidence=min_confidence,
        )


class KYCValidate(HelperBotoClient):
    def validate_label_in_document(self, url, label_name, min_confidence):
        response = self.detect_labels(url, min_confidence)
        return label_name in [label["Name"] for label in response["Labels"]]

    def extract_driver_license_data(self, url):
        return  [item['DetectedText'] for item in self.detect_text(url)["TextDetections"]]

    def validate_id_cards(self, url, min_confidence=95):
        return self.validate_label_in_document(url, "Id Cards", min_confidence)

    def validate_driver_license(self, url, min_confidence=95):
        return self.validate_label_in_document(url, "Driving License", min_confidence)

    def validade_faces(self, image_source, image_target, min_confidence=98):
        try:
            return self.compare_faces(image_source, image_target)["FaceMatches"][0]["Similarity"] > min_confidence
        except (KeyError, IndexError):
            return False
