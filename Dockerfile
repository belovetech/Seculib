FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt file to the working directory
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Set the environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose the port the app runs on
EXPOSE 5000

# Run the flask command
CMD ["flask", "run"]


