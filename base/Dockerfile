# We might have to change this base one, or have several different base versions for
# different systems.  e.g. OSG might require some specific parent image?
# This base does not include the DM stack.
# So it will need more dependencies installing.
FROM ubuntu:xenial
MAINTAINER joezuntz@googlemail.com

USER root
RUN mkdir /opt/desc
ONBUILD COPY run.py /opt/desc/run.py
CMD /opt/desc/run.py
RUN useradd -ms /bin/bash vagrant

RUN apt-get update && apt-get install -y gcc python3 python3-pip && apt-get clean
RUN pip3 install --upgrade pip
RUN pip3 install numpy py-dag==3.0.0 
RUN pip3 install fitsio
COPY descpipe-1.2.tar.gz /home/root/
RUN pip3 install /home/root/descpipe-1.2.tar.gz && rm /home/root/descpipe-1.2.tar.gz
ENV PYTHONPATH="/opt/desc:${PYTHONPATH}"

# This is needed to work on NERSC.
#ENV USER vagrant
#ENV HOME /home/vagrant
