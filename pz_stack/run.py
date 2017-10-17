#!/usr/bin/env python3

"""


"""

# Make sure this file is executable.
import descpipe


class Stage(descpipe.Stage):
    name = "pz_stack"
    config = {}

    inputs = {
        "photoz-catalog": "fits",
        "tomographic-catalog": "fits",
    }

    outputs = {
        "n_of_z" : "fits",
    }


    def run(self):
        import pz_stack

        pdf_file = self.get_input_path("photoz-catalog")
        tomo_file = self.get_input_path("tomographic-catalog")
        n_of_z_file = self.get_output_path("n_of_z")
        
        # Run the code
        pz_stack.main(pdf_file, tomo_file, n_of_z_file)






# Always end with this
if __name__ == '__main__':
    Stage.main()
