import os 
import sys
sys.path.insert(0, '..')
import warnings
warnings.filterwarnings('ignore')

from prefect import flow
from omegaconf import DictConfig, OmegaConf
import hydra
from prefect.task_runners import SequentialTaskRunner, ConcurrentTaskRunner
from prefect_ray.task_runners import RayTaskRunner

import src.processing as prc
import src.train as tr
import src.validate as val


@hydra.main(version_base=None, config_path="../config", config_name="main.yaml")
@flow(name="chest_disease_classification",
    description="A flow to run the pipeline",
    task_runner=RayTaskRunner()
) ## multi cpus
# @flow(name="chest_disease_classification",
#     description="A flow to run the pipeline",
#     task_runner=SequentialTaskRunner()
# ) ## multi threads
def main(cfg) -> None:
    prc.main(cfg)
    tr.main(cfg)
    val.main(cfg)


if __name__ == '__main__':    
    main()














