FROM python
WORKDIR /g2h
COPY . /g2h
RUN pip install -r requirements.txt
EXPOSE 80
CMD flask run --host 0.0.0.0 --port 80