FROM ubuntu
EXPOSE 5000
RUN ["/bin/bash", "-c", "apt-get update > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3 > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-pip > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-venv > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y python3-dev > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "apt-get install -y libpq-dev > /dev/null 2>&1"]
RUN mkdir /app
RUN mkdir /app/app
RUN mkdir /app/appVenv
WORKDIR /app/appVenv
RUN ["/bin/bash", "-c", "python3 -m venv venv > /dev/null 2>&1"]
CMD ["/bin/bash", "-c", "cp /app/app/requirements.txt requirements.txt; source venv/bin/activate; pip install --no-cache-dir -r requirements.txt; cd /app/app; python run.py"]
