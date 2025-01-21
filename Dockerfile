
FROM python:3.9-slim


WORKDIR /app


COPY app/ /app/


EXPOSE 8080


RUN pip install --no-cache-dir -r /app/requirements.txt


CMD ["python", "service_a_app.py"]
