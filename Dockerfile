FROM python:3.6.15
RUN useradd -ms /bin/bash act
WORKDIR /tmp
COPY ./oc /usr/local/bin
RUN pip install -r requirements.txt && apt update -y && apt install jq sqlite3 vim -y 
COPY --chmod=0644 *.py .env requirements.txt app_list_to_check.txt /tmp/
USER act
CMD ["python","-u","main.py"]
