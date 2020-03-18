# Diabetic retinopathy screening & classification

![Diabetic retinopathy screening & classification output example](sample_data/level-0 %28f4df3d86688d%29.png?raw=true)

[The Diabetic retinopathy screening & classification](https://aws.amazon.com/marketplace/pp/prodview-b53upp27dnmzq) - is an image analysis and anomaly detection model that identifies and classifies diabetic anomalies in eye screens. It scales eye screening and helps doctors detect signs of diabetic retinopathy. As all screens are ranked by severity, doctors can address urgent cases first, to diagnose faster and prevent sight loss. The model is trained on images from multiple clinics, including Aravind Eye Hospital (Kaggle dataset), using a variety of vision screening devices over an extended period of time. NB: The model is not FDA-compliant; for auxiliary/support use only.

## Usage Information

Using our model for real time prediction is as simple as this:

```python
predictor = sagemaker.predictor.RealTimePredictor(
    ' your endpoint name ',
    sagemaker_session=sagemaker.Session(),
    content_type="image/jpeg"
)

with open('data/sample_image.jpg', 'rb') as img:
    img_bytes = bytearray(img.read())
    result = predictor.predict(img_bytes).decode("utf-8")
```

Also we've published two notebooks showing how to use our model:
* [Using-Diabetic-Retinopathy-Detector-Single-Image-Inference.ipynb](Using-Diabetic-Retinopathy-Detector-Single-Image-Inference.ipynb) notebook shows how you can use Python API to perform inference on endpoint created from the model on a single image
* [Using-Diabetic-Retinopathy-Detector-model.ipynb](Using-Diabetic-Retinopathy-Detector-model.ipynb) notebook shows how you can use Python API to run the full scenario:
    * deploy our model to create an endpoint
    * run Real Time inference on endpoint using local image
    * visualize  and save the prediction on original image

## Input data examples

* You can find sample input data in [sample_data](sample_data/) folder

