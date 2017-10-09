# We might have to change this base one, or have several different base versions for
# different systems.  e.g. OSG might require some specific parent image?
FROM lsstsqre/centos:7-newinstall
MAINTAINER joezuntz@googlemail.com

USER root
RUN mkdir /opt/desc
COPY run.py /opt/desc/run.py
CMD bash -lc /opt/desc/run.py

ADD dot-bashprofile /root/.bash_profile
ADD dot-bashrc /root/.bashrc

# Two versions one with stack one without?
RUN bash -lc "cd /opt/desc/ && wget https://github.com/joezuntz/descpipe/archive/0.1.0.tar.gz && tar -zxvf 0.1.0.tar.gz && rm 0.1.0.tar.gz && cd descpipe-0.1.0/ && python3 setup.py install && rm -rf /opt/desc/descpipe"
RUN echo http_caching=packages >> /etc/yum.conf
RUN yum clean all

USER vagrant
ADD dot-bashprofile /home/vagrant/.bash_profile
ADD dot-bashrc /home/vagrant/.bashrc


ENV DESC_INPUT=/opt/input
ENV DESC_OUTPUT=/opt/output
ENV DESC_CONFIG=/opt/config
ENV PYTHONPATH="/opt/desc:${PYTHONPATH}"

