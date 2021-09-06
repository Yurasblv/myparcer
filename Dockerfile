FROM python:3
RUN pip install --upgrade pip

WORKDIR .
ADD main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python","-u", "main.py" ]

