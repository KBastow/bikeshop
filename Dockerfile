# Use Python 3.6 or later as a base image
FROM python:3.7
# Copy contents into image
WORKDIR /app
# Copy the app file into the image working directory
COPY . .
# Execute a pip install command using the list 'requirements.txt'
RUN pip install -r requirements.txt
# Set YOUR_NAME environment variable
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT [ "python", "app.py" ]