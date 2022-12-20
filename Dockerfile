FROM python:3.8-slim-buster

RUN python3.8 -m venv /home/printer/venv

ENV PATH="/home/printer/venv/bin:$PATH"

WORKDIR .

COPY requirements.txt ./

RUN python3.8 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9998

CMD [ "python3", "index.py"]