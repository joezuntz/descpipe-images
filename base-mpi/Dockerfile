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

RUN apt-get update && apt-get install -y gcc g++ gfortran python3 python3-pip wget autoconf automake && apt-get clean all
RUN pip3 install --upgrade pip
RUN pip3 install numpy py-dag==3.0.0 
RUN pip3 install fitsio
RUN pip3 install descpipe==1.3
ENV PYTHONPATH="/opt/desc:${PYTHONPATH}"


ENV DESC_CONFIG /opt/config
ENV DESC_INPUT /opt/input
ENV DESC_OUTPUT /opt/output


RUN chmod ugo+w /opt /opt/desc


RUN mkdir /opt/mpi \
    && cd /opt/mpi \
    && wget http://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz \
    && tar xvzf mpich-3.2.tar.gz && cd /opt/mpi/mpich-3.2 \
    && ./configure \
    && make \
    && make install \
    && rm -rf /opt/mpi

RUN mkdir /opt/mpi  \
    && cd /opt/mpi \
    && wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-2.0.0.tar.gz \
    && tar xvzf mpi4py-2.0.0.tar.gz \
    && cd mpi4py-2.0.0  \
    && python3 setup.py build  \
    && python3 setup.py install \
    && rm -rf /opt/mpi \
    && /sbin/ldconfig
