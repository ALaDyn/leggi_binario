from .Simulation import Simulation
from .utilities.Utility import lampy_version

__version__ = lampy_version
__doc__ = """
Light and fast Aladyn's data Manipulation in PYton (LAMPY)

This package is developed by the ALaDyn Collaboration

You can read, plot and elaborate ALaDyn's output files.
To import the simulation folder, type

>>> sim=lampy.Simulation(path)

where 'path' is the relative or absolute path of interest.
"""