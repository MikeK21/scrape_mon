# scrape_mon web
scrape_mon project

### Web Server rendition is still in work

# The Script

The python script "simple_serverv2.py" uses environment variables from dockerfile to run against the hardcoded stock and timeline, which currently is "MSFT" and for 3 days. The script that does the actual lookup is "scrape_mon.py" and simple_serverv2.py simply provides a web interface.

The script allows for user input on stock and timeline to review, however, it is not currently being utilized.

# The Docker Image

For this part, you will need to install docker on your local machine. A directory with the "dockerfile" and the script in the same directory must exist for docker to build. THe dockerfile is included in this repo. At it's simplest, it looks like this:

FROM python:3

ENV STOCKSYMBOL "MSFT"
ENV NDAYS "3"
EXPOSE 8080

WORKDIR /
ADD scrape_mon.py /
ADD simple_serverv2.py /

CMD [ "python3", "./simple_serverv2.py" ]

The docker image can be built with the following once the dockerfile file is created as mentioned above and the script is in the same directory:

 	docker build -t scrape_mon .

Ater the build completes, you can run the container and the script therein with:

	docker run -p 8080:8080 scrape_mon
