import warnings
warnings.filterwarnings('ignore')
from pathlib import Path
import os
import json
import base64
import boto3
import mlflow


def get_model_location(run_id):
    model_location = os.getenv('MODEL_LOCATION')

    if model_location is not None:
        return model_location

    model_bucket = os.getenv('MODEL_BUCKET', 'mlflow-models-alexey')
    experiment_id = os.getenv('MLFLOW_EXPERIMENT_ID', '1')
    model_location = f's3://{model_bucket}/{experiment_id}/{run_id}/artifacts/model'
    return model_location


# def test_model_predict():
#     run_id = os.getenv('MLFLOW_RUN_ID', '1')
#     model_path = get_model_location(run_id)
#     model = mlflow.pyfunc.load_model(model_path)
#     expected_result = model.predict('')
#     actual_result = ''
#     assert actual_result == expected_result


def test_data_location():
    bucket_name = 'bucket1-aws-2023'
    key1 = 'green_tripdata_1'
    key2 = 'green_tripdata_2'
    expected_data_location_1 = f's3://{bucket_name}/{key1}'
    expected_data_location_2 = f's3://{bucket_name}/{key2}'
    assert expected_data_location_1 == 's3://bucket1-aws-2023/green_tripdata_1'
    assert expected_data_location_2 == 's3://bucket1-aws-2023/green_tripdata_2'




