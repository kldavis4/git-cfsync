#!/usr/bin/env python3

import argparse
import os
import shlex
import subprocess
import sys

class CfGitRepository(object):
    '''A Git repository used for storing configuration files

    This class represents a git respository that is used to control
    configuration files and provides a set of actions useful for automating
    common tasks.

    Note: This object will run system commands, alter the environment and
    change directories.  Beware.
    '''
    def __init__(self, repopath):
        'Initialize the environment for running git commands'
        os.chdir(repopath)
        self._gather_sync_config()

    def _gather_sync_config(self):
        '''Read cfsync configuration for this repository

        cfsync configuration is stored via 'git-config', which makes it easy
        link configuration to particular repositories.  This procedure reads
        all known configuration values into self.config.
        '''
        config = {}
        for key in ('fetch',):
            config[key] = self._git('config --get-all cfsync.' + key).split()
        self.config = config

    def _git(self, cmdstr):
        return subprocess.check_output(['git',] + shlex.split(cmdstr))

    def run_periodic_tasks(self):
        'Perform tasks that should run periodically'
        pass

def parse_arguments():
    'Parse arguments from command line invocation'
    parser = argparse.ArgumentParser(prog='git-cfsync')
    parser.add_argument('repopath', metavar='PATH',
                        help="path to git repository")
    parser.add_argument('-V', action='version', version='0.1')
    return parser.parse_args()

def main():
    args = parse_arguments()
    cfgit = CfGitRepository(args.repopath)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error:', e, file=sys.stderr)
