FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install flask flask-HTTPAuth gunicorn
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "PuckDBViewer:app"]