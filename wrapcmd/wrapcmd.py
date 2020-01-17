import subprocess
import logger

class CmdSession:
    def __init__(self):
        self._dry_run = False
        self._logger = logger

    @property
    def dry_run(self):
        return self._dry_run

    @dry_run.setter
    def dry_run(self):
        self._dry_run = True

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    def exec(self, cmd: str, get_output=False, default=None, shell=True):
        self._logger.info("executing command: [%s]" % cmd)
        self._logger.info("DRY_RUN: {}".format(self._dry_run))
        if not self._dry_run:
            if get_output:
                return subprocess.check_output(cmd, shell=shell)
            else:
                subprocess.call(cmd, shell=shell)
        else:
            if get_output:
                return default
