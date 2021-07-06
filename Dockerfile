FROM pytorch/pytorch:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
ENV FLASK_APP app.py
CMD ["python3", "-m", "flask", "run"]