# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the project code into the container at /code/
COPY . /code/

# Add the project directory to PYTHONPATH
ENV PYTHONPATH=/code/ecothaili_api:$PYTHONPATH

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["gunicorn", "ecothaili_api.wsgi:application", "--bind", "127.0.0.1:8000"]
