# PPE Detector for Employee Safety

![PPE Detector for Employee Safety output example](sample_data/output_lab/image7.jpg?raw=true)

![PPE Detector for Employee Safety output example](sample_data/output_manuf/58_30.worker-work-build...jpg?raw=true)

[The PPE Detector for Employee Safety](https://aws.amazon.com/marketplace/pp/prodview-b53upp27dnmzq) - is a real-time computer vision model for identifying PPE non-compliance in working environments. The solution is a tool to ensure worker safety on building sites, fabrication lines, laboratories, steel, oil & gas enterprises, and other industrial environments where safety rules should be strictly followed. The solution is trained on the dataset manually selected and annotated by the VITechLab team. It detects if any of the following objects are missing: Coat, Glasses, Glove, Mask, Helmet. It works with live streams from CCTV cameras. This AI-based pre-packed solution is available for a subscription now.

### Are you looking to kick off an ML-driven worker safety initiative at your enterprise? [Contact us](https://vitechlab.com/) for details — we're now looking for pilot project teams to test the solution and will be happy to cooperate.

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
* [Using-Personal-Protection-Equipment-Detector-Single-Image-Inference.ipynb](Using-Personal-Protection-Equipment-Detector-Single-Image-Inference.ipynb) notebook shows how you can use Python API to perform inference on endpoint created from the model on a single image
* [Using-Personal-Protection-Equipment-Detection-model.ipynb](Using-Personal-Protection-Equipment-Detection-model.ipynb) notebook shows how you can use Python API to run the full scenario:
    * deploy our model to create an endpoint
    * run Real Time inference on endpoint using local image
    * visualize  and save the prediction on original image

## Input\output data examples

* You can find sample input data in [sample_data](sample_data/demo_input) folder
* [output_lab](sample_data/output_lab) and [output_manuf](sample_data/output_manuf) folders contains images with detections predicted by the model and visualized using `utils.visualize_detection` method


## Sample detection results:

![PPE Detector for Employee Safety output example](sample_data/output_lab/image2.jpg?raw=true)

![PPE Detector for Employee Safety output example](sample_data/output_lab/image4.jpg?raw=true)

![PPE Detector for Employee Safety output example](sample_data/output_manuf/79_32.site-1536859_960_...jpg?raw=true)

![PPE Detector for Employee Safety output example](sample_data/output_manuf/50_31.WomanFactory1940s...jpg?raw=true)

![PPE Detector for Employee Safety output example](sample_data/output_manuf/61_2.worker-on-construc...jpg?raw=true)
