import logging
import sys

logger = logging.getLogger('bark-client-logger')

logger.setLevel(logging.INFO)
fh = logging.StreamHandler(stream=sys.stderr)

fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
fh.setLevel(logging.INFO)
logger.addHandler(fh)