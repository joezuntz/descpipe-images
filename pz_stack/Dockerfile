# The first of these variables must be set when building.
# The second can be, but takes the default value 1.0
ARG user
ARG base=1.0
# This is the base image that we start from for this case.
FROM ${user}/desc-pipe-base:${base}

# Install python dependencies
RUN pip3 install fitsio

# This is not good practice in general - we should mainly put these things in independent repos.
COPY pz_stack.py /opt/desc/

# Always end with this!
USER vagrant
