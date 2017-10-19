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
        "tomographic-catalog": "fits",
    }

    outputs = {
        "correlation-functions": "fits",
        #"some-catalog": "hdf",
        #"some-metadata": float,
        #other stuff like this?
    }



    def run(self):
        # Imports must be in here
        import treecorr_wrapper

        config_file = self.get_config_path("config")
        cat_file = self.get_input_path("shear-catalog")
        tomo_file = self.get_input_path("tomographic-catalog")
        output_file = self.get_output_path("correlation-functions")

        treecorr_wrapper.main(config_file, tomo_file, cat_file, output_file)


# Always end with this
if __name__ == '__main__':
    Stage.main()
