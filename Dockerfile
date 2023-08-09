ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
ARG PYTHON_VERSION=3.9.8

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

COPY --from=py3 / /

ARG PYSPARK_VERSION=3.2.0
RUN pip --no-cache-dir install pyspark==${PYSPARK_VERSION}
RUN pip install pandas numpy

WORKDIR /flask_api
COPY ./requirements.txt /flask_api
RUN pip install -r requirements.txt
COPY . .
# EXPOSE 5000
# ENV FLASK_APP=app
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=production
# ENTRYPOINT ["python"]

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
# CMD ["flask", "run"]