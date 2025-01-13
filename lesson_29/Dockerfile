FROM python:3.11-slim

WORKDIR /graph_dir

#ADD graph.py
COPY . /graph_dir

RUN pip install -r requirements.txt & echo "Hello"

ENV USER_NAME=VLAD

CMD ["python", "graph_algorithms/example_3.py"]



