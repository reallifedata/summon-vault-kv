#!/bin/python

import os
import os.path
import re
import subprocess
import sys

def print_stderr(val):
    os.write(2, val)

def fetch_secret_from_vault_kv(secretpath):
    """ given a secretpath (vault kv-engine path) read/print the secret """
    command = 'vault read {}'.format(secretpath)
    process_output = ''
    print_stderr('executing shell command: [\n\t{}\n]'.format(command))
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process_output, _ = process.communicate()  # ignore stderr output from process
    print_stderr(process_output)
    try:
        if process.returncode != 0:
            raise StandardError('shell command failed due to non-zero return code({}): {}'.format(process.returncode, process_output))
    except (OSError, subprocess.CalledProcessError) as exception:
        print_stderr('shell command failed: ' + str(exception) + '  ' + process_output)
        raise exception
    except KeyboardInterrupt as exception:
        print_stderr('shell command cancelled by keyboard interrupt...')
        raise exception
    result = re.search(r'^data\s*map\[.*:(.*)\]', process_output, re.MULTILINE).group(1)
    print result
    


if __name__ == "__main__":
    # require profile to be explicitly supplied as a command-line argument
    if len(sys.argv) != 2:
        raise StandardError('USAGE: -v --version or secretpath')
    elif sys.argv[1] == '-v' or  sys.argv[1] == '--version':
        print('1.0.0')
    else:
        fetch_secret_from_vault_kv(sys.argv[1])

