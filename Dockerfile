# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY app.py .

# Set the environment variable for the Telegram token
ENV TELEGRAM_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>

# Command to run the bot
CMD ["python", "app.py"]
