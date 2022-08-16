import pytest
from unittest.mock import patch

from pyrekognition.helper import HelperBotoClient, KYCValidate


@pytest.mark.vcr
def test_helper_convert_url_to_bytes():
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    assert HelperBotoClient()._convert_url_to_bytes(url_) is not None


@pytest.mark.vcr
@patch("pyrekognition.helper.rekognition_client.detect_labels")
def test_detect_labels(mock_detect_labels, aws_detect_labels):
    mock_detect_labels.return_value = mock_detect_labels
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    assert HelperBotoClient().detect_labels(url_) is not None


@pytest.mark.vcr
def test_detect_text():
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    response = HelperBotoClient().detect_text(url_)
    assert response is not None


@pytest.mark.vcr
def test_compare_faces():
    url_origin = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    url_targer = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    response = HelperBotoClient().compare_faces(url_origin, url_targer)
    assert response is not None


@pytest.mark.vcr
def test_validate_id_cards_success():
    url = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    validator = KYCValidate()
    response = validator.validate_id_cards(url)

    assert response is True


@pytest.mark.vcr
def test_validate_id_cards_failed():
    url = "https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f984.png"
    validator = KYCValidate()
    response = validator.validate_id_cards(url)

    assert response is False


@pytest.mark.vcr
def test_validate_driver_license_success():
    url = "https://www.dof.ms.gov.br/wp-content/uploads/2019/08/28-CNH-falsa-em-Amambai.jpg"  # noqa E501
    validator = KYCValidate()
    response = validator.validate_driver_license(url)

    assert response is True


@pytest.mark.vcr
def test_validate_driver_license_failed():
    url = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    validator = KYCValidate()
    response = validator.validate_driver_license(url)

    assert response is False


@pytest.mark.vcr
def test_validade_faces():
    url_origin = "https://pbs.twimg.com/profile_images/1226626761611456513/MMyVfrYT_400x400.jpg"  # noqa E501
    url_targer = "https://img.a.transfermarkt.technology/portrait/big/3366-1489607001.jpg"

    validator = KYCValidate()
    assert validator.validade_faces(url_origin, url_targer) is True


@pytest.mark.vcr
def test_validade_faces_not_matched():
    url_origin = "https://pbs.twimg.com/profile_images/1226626761611456513/MMyVfrYT_400x400.jpg"  # noqa E501
    url_targer = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"

    validator = KYCValidate()
    assert validator.validade_faces(url_origin, url_targer) is False


@pytest.mark.vcr
def test_extract_driver_license_data():
    url = "https://gringo.com.vc/wp-content/uploads/2021/05/geral-CNH-867x1024.png"
    validator = KYCValidate()
    print(validator.validate_driver_license(url))
    data = validator.extract_driver_license_data(url)
    print(data)


@pytest.mark.vcr
def test_extract_driver_license_data_fake():
    url = 'https://support-candidates.gupy.io/hc/article_attachments/4419319664283/cnh_fisica.png'
    validator = KYCValidate()
    print(validator.validate_driver_license(url))
    data = validator.extract_driver_license_data(url)
    print(data)
