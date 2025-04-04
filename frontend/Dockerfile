FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for building Python packages)
RUN apt-get update && apt-get install -y build-essential curl

# Install Poetry
ENV POETRY_VERSION=2.1.2
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Disable virtualenvs so packages install globally
RUN poetry config virtualenvs.create false

# Copy only pyproject.toml and poetry.lock first (for better layer caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the app
COPY . /app

# Expose the port Streamlit runs on
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
