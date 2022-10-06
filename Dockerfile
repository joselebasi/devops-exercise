FROM python:3.8.3-alpine

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED TRUE

RUN adduser -D devops
USER devops
WORKDIR /home/devops

COPY --chown=devops:devops requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-warn-script-location

COPY --chown=devops:devops . .

CMD [ "python3", "-u", "-m", "flask", "run", "--host=0.0.0.0"]