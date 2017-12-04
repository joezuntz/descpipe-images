# The first of these variables must be set when building.
# The second can be, but takes the default value 1.0
ARG user
ARG base=1.0
# This is the base image that we start from for this case.
FROM ${user}/desc-pipe-base:${base}

# Before all these things happen the command "ONBUILD" that we ran in the 
# base image will trigger this build to add a file called "run.py to "/opt/desc/".


# Install dependencies
RUN apt-get install -y libffi-dev && apt-get clean

# Install python dependencies
RUN pip3 install TreeCorr
RUN pip3 install twopoint

# Install a file with code for this module.
COPY treecorr_wrapper.py /opt/desc/treecorr_wrapper.py

# Must always end with these.
USER vagrant


