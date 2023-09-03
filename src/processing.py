import os 
import sys
sys.path.insert(0, '..')
#import mlflow 
import hydra
from omegaconf import DictConfig, OmegaConf
from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner, ConcurrentTaskRunner


@task
def load_data():
    print()

@task
def transform_data():
    print()


@flow(task_runner=ConcurrentTaskRunner())
def main(config):
    # MLFLOW_EXPERIMENT_NAME = config.MLFLOW_EXPERIMENT_NAME
    # MLFLOW_TRACKING_URI = config.MLFLOW_TRACKING_URI

    load_data()
    transform_data()
