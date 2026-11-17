FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY app.py banner.txt ./
USER 10001
EXPOSE 8000
CMD ["python", "app.py"]
