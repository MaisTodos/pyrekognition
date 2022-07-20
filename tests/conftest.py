import pytest


@pytest.fixture
def aws_detect_labels():
    return {
        "Labels": [
            {
                "Name": "Text",
                "Confidence": 99.98565673828125,
                "Instances": [],
                "Parents": [],
            },
            {
                "Name": "Person",
                "Confidence": 98.85494232177734,
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.2604822516441345,
                            "Height": 0.26448744535446167,
                            "Left": 0.18291354179382324,
                            "Top": 0.19233660399913788,
                        },
                        "Confidence": 98.85494232177734,
                    }
                ],
                "Parents": [],
            },
            {
                "Name": "Human",
                "Confidence": 98.85494232177734,
                "Instances": [],
                "Parents": [],
            },
            {
                "Name": "Document",
                "Confidence": 96.8370132446289,
                "Instances": [],
                "Parents": [{"Name": "Text"}],
            },
            {
                "Name": "Id Cards",
                "Confidence": 96.36094665527344,
                "Instances": [],
                "Parents": [{"Name": "Document"}, {"Name": "Text"}],
            },
            {
                "Name": "Driving License",
                "Confidence": 94.43672943115234,
                "Instances": [],
                "Parents": [{"Name": "Document"}, {"Name": "Text"}],
            },
            {
                "Name": "License",
                "Confidence": 94.43672943115234,
                "Instances": [],
                "Parents": [{"Name": "Document"}, {"Name": "Text"}],
            },
            {
                "Name": "Passport",
                "Confidence": 85.43043518066406,
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.9281060695648193,
                            "Height": 0.8953736424446106,
                            "Left": 0.025386426597833633,
                            "Top": 0.05398087203502655,
                        },
                        "Confidence": 85.43043518066406,
                    }
                ],
                "Parents": [
                    {"Name": "Id Cards"},
                    {"Name": "Document"},
                    {"Name": "Text"},
                ],
            },
        ],
        "LabelModelVersion": "2.0",
        "ResponseMetadata": {
            "RequestId": "2c379332-57f8-46c0-8401-5208c4e36f50",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": "2c379332-57f8-46c0-8401-5208c4e36f50",
                "content-type": "application/x-amz-json-1.1",
                "content-length": "1155",
                "date": "Fri, 15 Jul 2022 18:29:25 GMT",
            },
            "RetryAttempts": 0,
        },
    }
