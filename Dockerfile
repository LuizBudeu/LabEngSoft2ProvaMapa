
FROM python:3

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
WORKDIR /prova

COPY . .

EXPOSE 7000

# runs the production server
CMD ["python",  "manage.py",  "runserver", "0.0.0.0:7000"]