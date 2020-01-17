# Retail Store Product Demand Forecasting

![Retail Store Product Demand Forecasting output example](assets/forecast.png?raw=true)

[The Product Demand Forecasting Solution](https://aws.amazon.com/marketplace/pp/prodview-56fo5it4n5mqm) - is a cloud-native predictive analytics ML model that analyzes multiple data points, including historical sales data, inventory data, and growth projections to generate up to 50% more accurate product demand forecasts. The solution is scalable and customizable, allows for manual adjustments. It supports batch (schedule) and real-time forecasting, and it can be integrated through RESTful API. The ML model can be used by small- and midsize retailers to cut overstock/stockouts, optimize inventory, and increase supply chain efficiency.

## Usage Information

### Train the model based on historical sales data

```python
import sagemaker as sage

algorithm_arn = 'arn:aws:sagemaker:us-east-2:992377156234:algorithm/vitech-lab-forecaster-v1-0-3'

forecaster = sage.AlgorithmEstimator(algorithm_arn,
                       'AmazonSageMaker-ExecutionRole', 1, 'ml.c4.xlarge',
                       output_path=train_output_data_location,
                       sagemaker_session=sess)
# train_data_location points to S3 directory containing the training CSV file
forecaster.fit({'training': train_data_location})
```

### Deploying the trained model

```python
from sagemaker.predictor import json_serializer

endpoint_instance_type = 'ml.c5.xlarge'
predictor = forecaster.deploy(1, endpoint_instance_type, serializer=json_serializer)
```

### Generating the product demand forecasts
```python
import pandas as pd
from io import StringIO

result_str = predictor.predict({'new_points_count': drop_month_count, 'new_points_frequency': 'month'}).decode('utf-8')

forecast = pd.read_csv(StringIO(result_str))
```

## Complete Usage Workflow

We've published [this Jupyter Notebook](Using-Forecaster-Algorithm.ipynb) showing how you can use Python API to run the full scenario:
    * train the model using historical data
    * deploy the model to create an endpoint
    * run Real Time inference on endpoint
    * visualize and save the prediction
    * run Batch Transform job to perfom the inference on your data stored in Amazon S3 bucket
