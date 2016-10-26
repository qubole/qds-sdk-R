try:
    from qds_sdk.qubole import Qubole
    from qds_sdk.commands import *
    import qds_sdk.exception
except ImportError:
    print """You need to install qds-sdk-py from http://github.com/qubole/qds-sdk-py"""
import tempfile
import os
import sys
import traceback
import logging
import shlex

log = logging.getLogger("command")

def connect(api_token=None, poll_interval=None):
    # Try setting from environment variables
    if api_token is None:
        api_token = os.getenv('QDS_API_TOKEN')
    if poll_interval is None:
        poll_interval = os.getenv('QDS_POLL_INTERVAL')
    api_url = os.getenv('QDS_API_URL')
    api_version = os.getenv('QDS_API_VERSION')
    # If they aren't set, resort to default values
    if api_url is None:
        api_url = "https://api.qubole.com/api/"
    if api_token is None:
        sys.stderr.write("No API Token provided\n")
    if api_version is None:
        api_version = "v1.2"
    if poll_interval is None:
        poll_interval = 5
    Qubole.configure(api_token=api_token,
                     api_url=api_url,
                     version=api_version,
                     poll_interval=poll_interval,
                     skip_ssl_cert_check=False)

def getcommandresults(cmd):
    print(("Streaming Job run via command id: %s, finished with status %s" % (cmd.id, cmd.status)))
    tempfp = tempfile.TemporaryFile()
    cmd.get_results(fp=tempfp)
    tempfp.seek(0)
    results = tempfp.read()
    tempfp.close()
    return results

# Check
def check(commandId):
    print Command.find(commandId)

# Cancel
def cancel(commandId):
    return Command.cancel_id(commandId)

# Get
def getresult(commandId):
    cmdobj = Command.find(commandId)
    return getcommandresults(cmdobj)

def getlog(commandId):
    return Command.get_log_id(commandId)

#Hive
def hivecommand(query=None, macros=None, tags=None, sample_size=None, cluster_label=None,
                notify=None, name=None, script_location=None, print_logs=None, command_type="submit"):
    
    command = ""
    try:
        command = HiveCommand.create(query=query, macros=macros, tags=tags, sample_size=sample_size,
                                     label=cluster_label,can_notify=notify, name=name, script_location=script_location,
                                     print_logs=print_logs)
    except qds_sdk.exception.Error as e:
        sys.stderr.write("Error: Status code %s (%s) from url %s\n" %
                         (e.request.status_code, e.__class__.__name__,
                          e.request.url))
    except qds_sdk.exception.ConfigError as e:
        sys.stderr.write("Configuration error: %s\n" % str(e))
    except qds_sdk.exception.ParseError as e:
        sys.stderr.write("Error: %s\n" % str(e))
    except Exception:
        traceback.print_exc(file=sys.stderr)
    if command_type == "run":
        while not Command.is_done(command.status):
            time.sleep(Qubole.poll_interval)
            command = Command.find(command.id)
        return getcommandresults(command)
    else:
        return command.id

# Presto
def prestocommand(query=None, script_location=None, macros=None, tags=None, cluster_label=None,
                  notify=None, name=None, print_logs=None, command_type="submit"):
    command = ""
    try:
        command = PrestoCommand.create(query=query, script_location=script_location, macros=macros, tags=tags,
                                       label=cluster_label, can_notify=notify, name=name, print_logs=print_logs)
    except qds_sdk.exception.Error as e:
        sys.stderr.write("Error: Status code %s (%s) from url %s\n" %
                         (e.request.status_code, e.__class__.__name__,
                          e.request.url))
    except qds_sdk.exception.ConfigError as e:
        sys.stderr.write("Configuration error: %s\n" % str(e))
    except qds_sdk.exception.ParseError as e:
        sys.stderr.write("Error: %s\n" % str(e))
    except Exception:
        traceback.print_exc(file=sys.stderr)
    if command_type == "run":
        while not Command.is_done(command.status):
            time.sleep(Qubole.poll_interval)
            command = Command.find(command.id)
        return getcommandresults(command)
    else:
        return command.id

# Spark
def sparkcommand(program=None, cmdline=None, sql=None, script_location=None, macros=None,
                 tags=None, cluster_label=None, language=None, app_id=None, notify=None, name=None,
                 arguments=None, user_program_arguments=None, print_logs=None, command_type="submit"):
    command = ""
    try:
        command = SparkCommand.create(program=program, cmdline=cmdline, sql=sql, script_location=script_location,
                                      macros=macros, tags=tags, label=cluster_label, language=language, app_id=app_id,
                                      can_notify=notify, name=name, arguments=arguments,
                                      user_program_arguments=user_program_arguments, print_logs=print_logs)
    except qds_sdk.exception.Error as e:
        sys.stderr.write("Error: Status code %s (%s) from url %s\n" %
                         (e.request.status_code, e.__class__.__name__,
                          e.request.url))
    except qds_sdk.exception.ConfigError as e:
        sys.stderr.write("Configuration error: %s\n" % str(e))
    except qds_sdk.exception.ParseError as e:
        sys.stderr.write("Error: %s\n" % str(e))
    except Exception:
        traceback.print_exc(file=sys.stderr)
    if command_type == "run":
        while not Command.is_done(command.status):
            time.sleep(Qubole.poll_interval)
            command = Command.find(command.id)
        return getcommandresults(command)
    else:
        return command.id
