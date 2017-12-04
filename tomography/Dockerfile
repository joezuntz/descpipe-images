# The first of these variables must be set when building.
# The second can be, but takes the default value 1.0
ARG user
ARG base=1.0
# This is the base image that we start from for this case.
FROM ${user}/desc-pipe-base:${base}

# Install the file implementing this module.
# Should really do this from github tagged version.
COPY tomography.py /opt/desc/

# Always end with this.
USER vagrant
