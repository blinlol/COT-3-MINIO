FROM python:3-slim
WORKDIR /
COPY manul.jpg requirements.txt ./
RUN pip install -r requirements.txt
COPY spamer.py .
CMD [ "python3", "spamer.py" ]
