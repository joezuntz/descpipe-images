# We might have to change this base one, or have several different base versions for
# different systems.  e.g. OSG might require some specific parent image?
# This base does not include the DM stack.
# So it will need more dependencies installing.
FROM ubuntu:xenial

USER root
RUN mkdir /opt/desc
ONBUILD COPY run.py /opt/desc/run.py
CMD /opt/desc/run.py
RUN useradd -ms /bin/bash vagrant

RUN apt-get update && apt-get install -y gcc python3 python3-pip && apt-get clean
RUN pip3 install --upgrade pip
RUN pip3 install numpy py-dag==3.0.0 
RUN pip3 install fitsio
RUN pip3 install descpipe==1.3
ENV PYTHONPATH="/opt/desc:${PYTHONPATH}"


ENV DESC_CONFIG /opt/config
ENV DESC_INPUT /opt/input
ENV DESC_OUTPUT /opt/output

COPY cwl-run.sh /opt/desc/cwl-run.sh

RUN chmod ugo+w /opt /opt/desc
# This is needed to work on NERSC.
#ENV USER vagrant
#ENV HOME /home/vagrant
