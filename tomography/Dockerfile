FROM joezuntz/desc-pipe-base:1.0
MAINTAINER joezuntz@googlemail.com
RUN bash -lc "pip install fitsio"
USER vagrant
COPY tomography.py /opt/desc/
COPY run.py /opt/desc/run.py
