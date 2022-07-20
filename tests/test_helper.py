from unittest.mock import patch

import pytest

from pyrekognition.helper import HelperBotoClient


@pytest.mark.vcr
def test_helper_convert_url_to_bytes():
    url_ = "https://ctn-cidades.s3.sa-east-1.amazonaws.com/Imagem+do+iOS+(2).jpg"
    assert HelperBotoClient()._convert_url_to_bytes(url_) is not None


@pytest.mark.vcr
@patch("pyrekognition.helper.rekognition_client.detect_labels")
def test_detect_labels(mock_detect_labels, aws_detect_labels):
    mock_detect_labels.return_value = mock_detect_labels
    url_ = "https://ctn-cidades.s3.sa-east-1.amazonaws.com/Imagem+do+iOS+(2).jpg"
    assert HelperBotoClient().detect_labels(url_) is not None
