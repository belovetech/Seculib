FROM python:3.8-slim


# Set environment variables to prevent Python from writing pyc files to disc
# and to prevent Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the environment variable for Flask
ENV FLASK_APP=api.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Set environment for Redis
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt file to the working directory
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /usr/src/app
COPY . .


# Expose the port the app runs on
EXPOSE 3000

# Run the flask command
CMD ["flask", "run", "-p", "3000"]


