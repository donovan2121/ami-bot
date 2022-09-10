FROM python:3.9

WORKDIR /ami

COPY *.py /ami/
COPY requirements.txt /ami/requirements.txt

RUN pip install --no-cache-dir -r /ami/requirements.txt

CMD [ "python" , "ami.py"]

