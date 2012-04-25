"""Pynsour Bootstrap"""

import sys
from src import *

def main(argv):
    if( len(sys.argv) > 1):
        conf = sys.argv[1]
    else:
        conf = 'bot.yaml'
    pynsour = Pynsour("./%s" % (conf))
    return pynsour.run()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
