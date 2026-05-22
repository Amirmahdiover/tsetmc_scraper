# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -i https://pypi.devneeds.ir/simple/ --trusted-host pypi.devneeds.ir -r requirements.txt

# Copy all source code
COPY . .

# Run app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
