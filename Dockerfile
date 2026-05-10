FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY convert-dbf-to-csv.py .

CMD ["python", "convert-dbf-to-csv.py"]
