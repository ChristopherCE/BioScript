import logging
import sys

import colorlog

from storage.config.chemstor_cli import ChemStorCLI
from storage.solvers.z3_solver import Z3Solver
from tests.convert.z3_test import *


def test():

    array = test_z3solver()

    for test in array:
        print('TEST')
        for t in test:
            (color, volume) = t
            print('    [BIN] color: %s, volume: %s' % (color, volume))
        print('\n\n')


def main(args):
    # parse the args.
    cli = ChemStorCLI(args)
    z3 = Z3Solver(cli.config)
    solution = z3.solve_constraints(z3.validate)
    colorlog.error(solution)


if __name__ == '__main__':
    colorlog.basicConfig(level=logging.DEBUG,
                         format='%(log_color)s%(levelname)s:\t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')

    # We don't need the first argument.
    main(sys.argv[1:])


