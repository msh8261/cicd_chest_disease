import os 
import sys
sys.path.insert(0, '..')
import mlflow 
import hydra
from omegaconf import DictConfig, OmegaConf
from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner, ConcurrentTaskRunner


@task
def create_pipeline():
    print()


@task 
def train():
    print()



@flow(task_runner=ConcurrentTaskRunner())
def main(config):
    MLFLOW_EXPERIMENT_NAME = config.MLFLOW_EXPERIMENT_NAME
    MLFLOW_TRACKING_URI = config.MLFLOW_TRACKING_URI
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    create_pipeline()
    train()
