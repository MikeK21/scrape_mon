FROM python:3

ENV STOCKSYMBOL "MSFT"
ENV NDAYS "3"

ADD scrape_mon.py /
ADD simple_server.py /

CMD [ "python", "./scrape_mon.py" ]
