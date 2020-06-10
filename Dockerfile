FROM python:3.7.5

WORKDIR /usr/src/discord-bot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./src/Main.py" ]