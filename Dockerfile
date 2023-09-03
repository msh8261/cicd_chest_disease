FROM public.ecr.aws/lambda/python:3.9

RUN pip install -U pip
RUN pip install poetry

COPY [ "pyproject.toml", "poetry.lock", "./" ]

RUN poetry install --system --deploy

COPY [ "lambda_function.py", "model.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]
