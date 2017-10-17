#!/usr/bin/env python3

"""
This pipeline step is trivial enough that we just code it up 
in this run program rather than calling another script.

"""

# Make sure this file is executable.
import descpipe

# Get input and output names etc.


class Stage(descpipe.Stage):
    name = "photoz"
    config = {
        "config":"config.yaml"
    }

    inputs = {
        "photoz-catalog": "fits",
    }

    outputs = {
        "tomographic-catalog": "fits",
    }


    def run(self):
        # Imports must be in here
        import yaml
        import tomography

        config_file = self.get_config_path("config")
        input_file = self.get_input_path("photoz-catalog")
        output_file = self.get_output_path("tomographic-catalog")

        #Configuration options
        config = yaml.load(open(config_file))
        bin_col = config['bin_column']
        nbin = config['nbin']
        zmin = config['zmin']
        zmax = config['zmax']
        weight_col = config.get('weight_col', None)
        hdu = config.get('hdu', 1)

        tomography.main(input_file, output_file, bin_col, nbin, zmin, zmax, weight_col, hdu)






# Always end with this
if __name__ == '__main__':
    Stage.main()
