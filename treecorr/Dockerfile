# This is the base we are building off, and is described in 
# the "base" directory.
FROM joezuntz/desc-pipe-base:1.0
MAINTAINER joezuntz@googlemail.com

# Enable root mode, so we can install things more easily
USER root

# Install dependencies
RUN apt-get install -y libffi-dev && apt-get clean

# Commands that need the DM stack set up first require bash -lc "command"
# The python we use comes from the DM stack so we require that.
RUN pip3 install TreeCorr
RUN pip3 install twopoint

COPY treecorr_wrapper.py /opt/desc/treecorr_wrapper.py

# Must always end with these.
# In the base image we told docker that the default command to run 
# should always be "/opt/desc/run.py".  We replace what that
# particular file is here.
USER vagrant
