    # Use an official lightweight Python image.
# python:3.9-slim is a good choice for a balance of size and compatibility.
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's layer caching.
# This way, dependencies are only re-installed if requirements.txt changes.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# The --no-cache-dir option keeps the image size down
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Specify the command to run on container startup.
# This assumes ACEest_Fitness.py is the main executable script of your application.
CMD ["python", "ACEest_Fitness.py"]
