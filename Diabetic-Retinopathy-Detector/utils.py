import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display

REGION_ACCOUNT_MAP = {
    "us-east-1": "865070037744",
    "us-east-2": "057799348421",
    "us-west-2": "594846645681",
    "eu-west-1": "985815980388",
    "eu-central-1": "446921602837",
    "ap-northeast-1": "977537786026",
    "ap-northeast-2": "745090734665",
    "ap-southeast-2": "666831318237",
    "ap-southeast-1": "192199979996",
    "ap-south-1": "077584701553",
    "ca-central-1": "470592106596",
    "eu-west-2": "856760150666",
    "us-west-1": "382657785993",
    "eu-west-3": "843114510376",
    "eu-north-1": "136758871317",
    "sa-east-1": "270155090741",
    "ap-east-1": "822005858737",
}

MODEL_PACKAGE_ARN = (
    "arn:aws:sagemaker:%s:%s:model-package/vitechlab-ppe-bbb-model-v1-1-398bfa174f00cfad7e4af4bf76862eb6"
)

def get_model_package_arn(region):
    account = REGION_ACCOUNT_MAP[region]
    
    return MODEL_PACKAGE_ARN % (region, account)

