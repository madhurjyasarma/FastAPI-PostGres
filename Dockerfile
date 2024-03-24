FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL "postgresql://turnoverdb_owner:1FL8RPuzgkwo@ep-gentle-field-a1seqjg1.ap-southeast-1.aws.neon.tech/NatureDots?sslmode=require"

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port on which your FastAPI application runs
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
