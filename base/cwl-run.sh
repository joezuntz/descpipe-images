#!/usr/bin/env bash

# This script turns a CWL command line into a descpipe command line
# CWL demands that all inputs and outputs are specified on the command line and 
# accept arbitrary locations. It also can't currently do mounted directories.

# This script:
#  makes the mount directories
#  parses the command line to find out what inputs and outputs it should have
#  links the inputs and config files into the right directories
#  runs the main script
#  moves output files back into the working directory


# Any failed call is definitely an error
set -e

ls -ld /opt
ls -l /opt
#  make the three mount directories
mkdir /opt/input
mkdir /opt/output
mkdir /opt/config

# Record list of outputs for later
OUTPUTS=()

# Parse the command line.

# This command splits up a variable
IFS=' ' read -ra ARGS <<< "$@"
for ARG in "${ARGS[@]}"
do
    # We expect the form type:name=path
    # where type=config/input/output
    # name is the tag from the stage
    # path is the input path that the CWL runtime gives
    # This bit parses that
    IFS='=' read -ra TAGPATH_PARTS <<< "$ARG"
    IFS=':' read -ra TAG_PARTS <<< "$TAGPATH_PARTS"
    TAG_TYPE=${TAG_PARTS[0]}
    TAG=${TAG_PARTS[1]}
    FILEPATH=${TAGPATH_PARTS[1]}

    # Either link (for config/input) or just store for later moving (output)
    case $TAG_TYPE in 
        input)
            echo "TAG ${TAG} is an input file: ${FILEPATH}"
            ln -s $FILEPATH /opt/input/${TAG}
            ;;
        config)
            echo "TAG ${TAG} is a config file: ${FILEPATH}"
            ln -s $FILEPATH /opt/config/${TAG}
            ;;
        output)
            echo "TAG ${TAG} is an output file: ${FILEPATH}"
            OUTPUTS+=("${FILEPATH}")
    esac
done

# Run the main script
/opt/desc/run.py

# Copy script outputs back
for OUTPUT_PATH in $OUTPUTS
do
    echo mv /opt/output/$OUTPUT_PATH . 
    mv /opt/output/$OUTPUT_PATH . 
done
