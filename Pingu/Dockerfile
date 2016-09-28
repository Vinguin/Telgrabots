FROM buildpack-deps:trusty-scm


ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"

# Update Packages
RUN apt-get update

RUN apt-get install -y firefox python-pip \ 
    build-essential chrpath libssl-dev libxft-dev \
    libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \
    python-dev libxml2-dev libxslt1-dev zlib1g-dev

RUN wget "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2"
RUN  tar xvjf $PHANTOM_JS.tar.bz2

RUN rm $PHANTOM_JS.tar.bz2

RUN mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin 


ADD . /project
WORKDIR /project
RUN pip install -r requirements.txt 
 
CMD ["python", "wilson.py"]
