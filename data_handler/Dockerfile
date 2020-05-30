FROM python:3
COPY requirements.txt entrypoint.sh /
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /data_handler
COPY rest_client.py config.json logging.conf data_handler.py /data_handler/
RUN sed -i "s|FREQ_API_PWD|${FREQ_API_PWD}|g" /data_handler/config.json
COPY /api_commands/ /data_handler/api_commands/ 
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.6.2-amd64.deb
RUN dpkg -i filebeat-7.6.2-amd64.deb
COPY filebeat.yml /etc/filebeat/filebeat.yml
WORKDIR /data_handler
RUN apt-get update && apt-get -y install jq
ENTRYPOINT ["/bin/bash","/entrypoint.sh"]
