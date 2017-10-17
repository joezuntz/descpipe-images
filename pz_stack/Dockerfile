FROM joezuntz/desc-pipe-base:1.0
MAINTAINER joezuntz@googlemail.com

RUN bash -lc "pip install fitsio"

# This is not good practice in general - we should mainly put these things in independent repos.
COPY pz_stack.py /opt/desc/

USER vagrant
COPY run.py /opt/desc/run.py
