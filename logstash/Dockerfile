FROM docker.elastic.co/logstash/logstash:7.6.2
ARG ELASTIC_PASSWORD
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD logstash.conf /usr/share/logstash/pipeline/
ADD logstash.conf /usr/share/logstash/config/
RUN sed -i "s|ELASTIC_PASSWORD|${ELASTIC_PASSWORD}|g" /usr/share/logstash/config/logstash.conf
RUN sed -i "s|ELASTIC_PASSWORD|${ELASTIC_PASSWORD}|g" /usr/share/logstash/pipeline/logstash.conf