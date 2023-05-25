FROM python:3.8.0
WORKDIR /marketplace_service
COPY /marketplace-service .
ENV PYTHONPATH /marketplace_service
RUN pip install --upgrade pip
RUN pip install "git+https://github.com/Alexzhukoff86/book-shared"

EXPOSE 5000
ENV FLASK_APP=marketplace_service/run.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]