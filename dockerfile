FROM python:3

ENV STOCKSYMBOL "MSFT"
ENV NDAYS "3"

ADD scrape_mon.py /

CMD [ "python3", "./scrape_mon.py" ]
