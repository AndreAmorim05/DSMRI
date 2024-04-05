FROM python:3.10-slim

# Configure files and directories
WORKDIR /app

RUN apt-get update --yes && \
    apt-get install --yes \
    build-essential \
    curl

ENV POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false && \
    poetry install

COPY . .

# Run supervisord
CMD ["python3", "dsmri/dsmri.py"]
