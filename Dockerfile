FROM python:3.9 AS builder
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./dvc.yaml ./dvc.yaml
COPY ./data/seeds.csv ./data/
#COPY ./data/test_data.csv ./data/
#COPY ./data/train_data.csv ./data/
#COPY ./data/validation_data.csv ./data/
#COPY ./experiments/svc/model.pkl ./experiments/svc/
COPY ./src ./src
COPY ./tests ./tests

#RUN pwd
#RUN ls -alh
#CMD ["dvc", "repro"]
#RUN python -m unittest ./tests/tests.py
#RUN python -m dvc repro
