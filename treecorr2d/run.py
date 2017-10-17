#!/usr/bin/env python3

# Make sure this file is executable.
import descpipe

# Get input and output names etc.


class Stage(descpipe.Stage):
    name = "photoz"
    config = {
        "config": "config.yaml"
    }

    #Tags and types?
    #Tags and schemas?
    inputs = {
        "shear-catalog": "fits",
    }

    outputs = {
        "correlation-functions": "txt",
        #"some-catalog": "hdf",
        #"some-metadata": float,
        #other stuff like this?
    }



    def run(self):
        # Imports must be in here
        import treecorr

        config_file = self.get_config_path("config")
        input_file = self.get_input_path("shear-catalog")
        output_file = self.get_output_path("correlation-functions")
        print(config_file)
        print(input_file)

        config = treecorr.read_config(config_file)
        config['file_name'] = input_file
        config['gg_file_name'] = output_file
        treecorr.corr2(config)



# Always end with this
if __name__ == '__main__':
    Stage.main()
