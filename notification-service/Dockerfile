FROM python:3.9-slim
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app/src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "src/controllers/notification_controller.py"]
