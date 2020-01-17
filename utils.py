import subprocess
import logger

DRY_RUN = True

def exec_cmd(cmd: str, get_output=False, default=None, shell=True):
    logger.info("executing command: [%s]" % cmd)
    logger.info("DRY_RUN: {}".format(DRY_RUN))
    if not DRY_RUN:
        if get_output:
            return subprocess.check_output(cmd, shell=shell)
        else:
            subprocess.call(cmd, shell=shell)
    else:
        if get_output:
            return default

def get_host_ip():
    cmd = ["hostname", "-I"]
    result = exec_cmd(cmd, get_output=True, default = b"a b c", shell=False).split(b" ")[0].decode("utf-8")
    return result

def unset_dry_run():
    global DRY_RUN
    DRY_RUN = False

def set_dry_run():
    global DRY_RUN
    DRY_RUN = True