FROM python:3.9-slim
RUN useradd -m -s /bin/bash appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python init_db.py && chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
