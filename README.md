# scrape_mon
scrape_mon project

# The Script

The python script "scrape_mon.py" uses environment variables set in the code itself to run against the hardcoded stock and timeline, which currently is "MSFT" and for 3 days.

The script allows for user input on stock and timeline to review, however, it is not currently being utilized.

# The Docker Image

For this part, you will need to install docker on your local machine. A directory with the "dockerfile" and the script in the same directory must exist for docker to build. THe dockerfile is included in this repo. At it's simplest, it looks like this:
	FROM python:3

	ADD scrape_mon.py /

	CMD [ "python", "./scrape_mon.py" ]

The docker image can be built with the following once the dockerfile file is created as mentioned above and the script is in the same directory:

 	docker build -t scrape_mon .

Ater the build completes, you can run the container and the script therein with:

	docker run scrape_mon
