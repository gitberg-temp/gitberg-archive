#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
"""
import os

import appdirs
from six.moves import input
import yaml

from .dialog import ConfigGenerator


class ConfigFile(object):
    """ A wrapper for managing creating and reading a config file
    takes (optional) appname str kwarg,
    for testing creation/destruction """
    # TODO emit warning if config doesn't exist
    # TODO make subcommand for creating config file
    appname = 'gitberg'
    file_name = 'config.yaml'

    def __init__(self, appname=None):
        if appname:
            self.appname = appname
        self.dir = appdirs.user_config_dir(self.appname)
        self.exists_or_make()

    @property
    def file_path(self):
        return os.path.join(self.dir, self.file_name)

    def exists_or_make(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        if not os.path.exists(self.file_path):
            # FIXME: copy or template sample config file
            with open(self.file_path, 'a'):
                os.utime(self.file_path, None)

    def write(self):
        # FIXME: VVV
        # self.check_self()
        with open(self.file_path, 'wb') as self.file:
            self.file.write(self.yaml)
        return True

    @property
    def yaml(self):
        return yaml.dump(self.data,
                         default_flow_style=False)

    def __repr__(self):
        return self.read()

    def read(self):
        with open(self.file_path) as _fp:
            return _fp.read()

    def parse(self):
        self.data = yaml.load(self.read())

    def check_self(self):
        # TODO: do a basic check of internal data values
        # TODO: check if file already exists
        pass

def check_config():
    """ Report if there is an existing config file
    """
    config = ConfigFile()
    config.parse()

    if config.data.keys() > 0:
        # FIXME: run a better check of this file
        print("Gitberg config looks ok")
    else:
        print("No config found")
        print("\twould you like to create a gitberg config file?")
        answer = input("-->  [Y/n]")
        # By default, the answer is yes, as denoted by the capital Y
        if not answer:
            answer = 'Y'

        # If yes, generate a new configuration
        # to be written out as yaml

        if answer in 'Yy':
            print("Running gitberg config generator ...")
            # config.exists_or_make()
            config_gen = ConfigGenerator()
            config_gen.ask()
            # print(config_gen.answers)
            config.data = config_gen.answers
            config.write()
            print("Config written to {}".format(config.file_path))
