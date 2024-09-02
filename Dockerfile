#FROM python:3.13-rc-alpine # for some reason it needs lscpu and a bash folder?
FROM python:3

# util-linux bash
#RUN apt install gcc python3-dev musl-dev linux-headers

#RUN adduser --disabled-password gramen

#USER gramen

ENV PATH="/home/gramen/.local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

COPY assets movie_streaming_site rxconfig.py ./

ENTRYPOINT ["python"]

CMD ["-m","reflex","run"]
