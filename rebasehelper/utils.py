# -*- coding: utf-8 -*-

import os
import fnmatch
import subprocess

class ProcessHelper(object):

    @staticmethod
    def run_subprocess(cmd, output=None):
        return ProcessHelper.run_subprocess_cwd(cmd, output=output)

    @staticmethod
    def run_subprocess_cwd(cmd, cwd=None, output=None):
        if output is not None:
            out_file = open(output, "w")
        else:
            out_file = None
        sp = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              cwd=cwd,
                              shell=False)
        for line in sp.stdout:
            if out_file is not None:
                out_file.write(line)
            else:
                print line.rstrip("\n")
        if out_file is not None:
            out_file.close()
        sp.wait()
        return sp.returncode

class PathHelper(object):

    @staticmethod
    def find_file(top_path, patern):
        """ Finds a file that matches the given 'patern' recursively
        starting in the 'top_path' directory. If found, returns full path
        to the first occurance of the file, otherwise returns None. """
        for root, dirs, files in os.walk(top_path):
            for f in files:
                if fnmatch.fnmatch(f, patern):
                    return os.path.join(root, f)
        return None