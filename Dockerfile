# Dockerfile

# 1. Base image
FROM python:3.10-alpine


# 2. Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set work directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Copy project
COPY . .

# 6. Run server
CMD ["gunicorn", "Eshop.wsgi:application", "--bind", "0.0.0.0:8000"]
