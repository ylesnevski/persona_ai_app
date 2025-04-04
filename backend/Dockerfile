FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for building and installing packages
RUN apt-get update && apt-get install -y build-essential curl

# Install Poetry
ENV POETRY_VERSION=2.1.2
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Disable Poetry virtualenvs — install globally in the container
RUN poetry config virtualenvs.create false

# Copy only Poetry files to install dependencies (faster caching)
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of your app
COPY . /app

# Expose the port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
