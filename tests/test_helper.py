from unittest.mock import patch

import pytest

from pyrekognition.helper import HelperBotoClient, KYCValidate


@pytest.mark.vcr
def test_helper_convert_url_to_bytes():
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    assert KYCValidate().convert_url_to_image(url_) is not None


@pytest.mark.vcr
@patch("pyrekognition.helper.rekognition_client.detect_labels")
def test_detect_labels(mock_detect_labels, aws_detect_labels):
    mock_detect_labels.return_value = mock_detect_labels
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    image = KYCValidate().convert_url_to_image(url_)
    assert HelperBotoClient().detect_labels(image) is not None


@pytest.mark.vcr
def test_detect_text():
    url_ = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    image = KYCValidate().convert_url_to_image(url_)
    response = HelperBotoClient().detect_text(image)
    assert response is not None


@pytest.mark.vcr
def test_compare_faces():
    url_origin = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501
    url_targer = "https://guiadocumentos.com.br/wp-content/uploads/2013/10/RIC-2010-F-310x165.jpg"  # noqa E501

    image_origin = KYCValidate().convert_url_to_image(url_origin)
    image_targer = KYCValidate().convert_url_to_image(url_targer)

    response = HelperBotoClient().compare_faces(image_origin, image_targer)
    assert response is not None


@pytest.mark.vcr
def test_validate_id_cards_success():
    url = "https://classic.exame.com/wp-content/uploads/2022/07/CIN-carteira-identificacao-nacional.jpg"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)
    response = validator.validate_id_cards(image)
    assert response is False


@pytest.mark.vcr
def test_validate_id_cards_failed():
    url = "https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f984.png"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)
    response = validator.validate_id_cards(image)
    assert response is False


@pytest.mark.vcr
def test_validate_driver_license_success():
    url = "https://www.dof.ms.gov.br/wp-content/uploads/2019/08/28-CNH-falsa-em-Amambai.jpg"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)
    response = validator.validate_driver_license(image)
    assert response is True


@pytest.mark.vcr
def test_validate_driver_license_failed():
    url = "https://www.dof.ms.gov.br/wp-content/uploads/2019/08/28-CNH-falsa-em-Amambai.jpg"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)
    response = validator.validate_driver_license(image)
    assert response is True


@pytest.mark.vcr
def test_validade_faces():
    url_origin = "https://pbs.twimg.com/profile_images/1226626761611456513/MMyVfrYT_400x400.jpg"  # noqa E501
    url_targer = "https://img.a.transfermarkt.technology/portrait/big/3366-1489607001.jpg"  # noqa E501

    validator = KYCValidate()
    image_origin = validator.convert_url_to_image(url_origin)
    image_targer = validator.convert_url_to_image(url_targer)
    assert validator.validade_faces(image_origin, image_targer) is True


@pytest.mark.vcr
def test_validade_faces_not_matched():
    url_origin = "https://pbs.twimg.com/profile_images/1226626761611456513/MMyVfrYT_400x400.jpg"  # noqa E501
    url_targer = "https://support-candidates.gupy.io/hc/article_attachments/4419319664283/cnh_fisica.png"  # noqa E501

    validator = KYCValidate()
    image_origin = validator.convert_url_to_image(url_origin)
    image_targer = validator.convert_url_to_image(url_targer)
    assert validator.validade_faces(image_origin, image_targer) is False


@pytest.mark.vcr
def test_extract_driver_license_data():
    url = "https://support-candidates.gupy.io/hc/article_attachments/4419319664283/cnh_fisica.png"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)
    assert validator.validate_driver_license(image) is False
    data = validator.extract_driver_license_data(image)
    assert isinstance(data, list)


@pytest.mark.vcr
def test_extract_driver_license_data_fake():
    url = "https://support-candidates.gupy.io/hc/article_attachments/4419319664283/cnh_fisica.png"  # noqa E501
    validator = KYCValidate()
    image = validator.convert_url_to_image(url)

    assert validator.validate_driver_license(image) is False
    data = validator.extract_driver_license_data(image)
    assert isinstance(data, list)
