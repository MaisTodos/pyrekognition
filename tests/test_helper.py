from unittest.mock import patch

from pyrekognition.helper import HelperBotoClient, KYCValidate


def test_helper_convert_url_to_bytes():
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    assert HelperBotoClient()._convert_url_to_bytes(url_) is not None


@patch("pyrekognition.helper.rekognition_client.detect_labels")
def test_detect_labels(mock_detect_labels, aws_detect_labels):
    mock_detect_labels.return_value = mock_detect_labels
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    assert HelperBotoClient().detect_labels(url_) is not None


def test_validate_id_cards_success():
    url = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    validator = KYCValidate()
    response = validator.validate_id_cards(url)

    assert response is True


def test_validate_id_cards_failed():
    url = "https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f984.png"
    validator = KYCValidate()
    response = validator.validate_id_cards(url)

    assert response is False


def test_validate_driver_license_success():
    url = "https://www.dof.ms.gov.br/wp-content/uploads/2019/08/28-CNH-falsa-em-Amambai.jpg"  # noqa E501
    validator = KYCValidate()
    response = validator.validate_driver_license(url)

    assert response is True


def test_validate_driver_license_failed():
    url = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    validator = KYCValidate()
    response = validator.validate_driver_license(url)

    assert response is False
