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
    "arn:aws:sagemaker:%s:%s:model-package/vitechlab-ppe-lab-model-v1-1-480cb3fc5bd97e9bf1e213cca498bbc4"
)
    

box_color = '#e0e0e0'
txt_box_color = '#e0e0e0b3'
default_color = 'black'
breach_color = '#ff0000'

maxsize = (1028, 1028)


def get_model_package_arn(region):
    account = REGION_ACCOUNT_MAP[region]
    
    return MODEL_PACKAGE_ARN % (region, account)


def visualize_detection(img_file, detections, save_path=None):
    img = Image.open(img_file)
    width_old = img.size[0]

    img.thumbnail(maxsize, Image.ANTIALIAS)

    ratio = img.size[0] / width_old

    drawing = ImageDraw.Draw(img, 'RGBA')


    for info in detections:
        xmin, ymin, xmax, ymax = np.array(info['box_points']) * ratio
        drawing.rectangle([xmin, ymin, xmax, ymax], outline=box_color, width=2)

        text_bg_height = 80
        text_bg_width = 130
            
        if ymin - text_bg_height < 0:
            ymin = ymin + text_bg_height

        drawing.rectangle([xmin, ymin - text_bg_height, xmin + text_bg_width, ymin], fill=txt_box_color)

        text_offset = -18
        for lbl, conf in info['classes'].items():
            color = breach_color if conf > 50 else default_color

            drawing.text((xmin, ymin + text_offset),
                         f' • {lbl}: {conf:.0f}%',
                         font=ImageFont.truetype("arial.ttf", 12),
                         fill=color)
            text_offset -= 18

        if save_path is not None:
            img.save(save_path)
    
    display(img)


def predict_and_display(predictor, file_name, save_path=None):
    global prediction_result
    
    with open(file_name, 'rb') as image:
        f = image.read()
        image_bytes = bytearray(f)

    prediction_result = predictor.predict(image_bytes).decode("utf-8")
    
    result = json.loads(prediction_result)
    
    visualize_detection(file_name, result, save_path)
    
    return result
