FROM python:2.7

COPY docker/newrelic_agent /usr/local/bin/agent

RUN pip install newrelic-plugin-agent \
    && pip install Jinja2 \
    && pip install psycopg2 \
    && pip install newrelic-plugin-agent[postgresql] \
    && chmod +x /usr/local/bin/agent/run.sh

WORKDIR /usr/local/bin/agent

CMD ["/usr/local/bin/agent/run.sh"]