try:
    from qds_sdk.qubole import Qubole
    from qds_sdk.commands import *
    import qds_sdk.exception
except ImportError:
    print """You need to install qds-sdk-py from http://github.com/qubole/qds-sdk-py"""
import tempfile
import sys
import traceback
import logging
import shlex
import os
log = logging.getLogger("hivecommand")



def usage(code=1):
    sys.stderr.write(usage_str + "\n")
    sys.exit(code)

def hivecommand( queryString):
    #logging.basicConfig(level=logging.WARN)
    
    #Qubole.configure(api_token = api_token)  
    args = HiveCommand.parse(shlex.split(queryString ))
    
    print str(args)
    
    cmd = HiveCommand.run(**args)
    
    print(("Streaming Job run via command id: %s, finished with status %s"% (cmd.id, cmd.status)))
        
    tempfp = tempfile.TemporaryFile()
    
    cmd.get_results(fp = tempfp)
    
    tempfp.seek(0)
    
    results = tempfp.read()
    
    tempfp.close()
    
    return results 

def hivecommand_from_r(query=None, poll_interval = os.getenv('QDS_POLL_INTERVAL'), sample_size=None, macros=None , tags=None, cluster_label=None, notify=None, name=None, api_token = os.getenv('QDS_API_TOKEN') ):
    #get value of api_url,
    api_url = os.getenv('QDS_API_URL')
    api_version = os.getenv('QDS_API_VERSION')
     
    
    chatty = False
    verbose = False
    
    skip_ssl_cert_check = None
    api_url = None
    api_version = None

    queryString = ""
    #reconstruct the queryString for to be parsed by hivecommand.parse function
    if query is not None:
        queryString += " --query '%s' "%str(query)
    #if script_location is not None:
    #    queryString += " -f '%s' "%str(script_location)
    if macros is not None:
        queryString += " --macros '%s' "%str(macros)
    if tags is not None:
        queryString += " --tags '%s' "%str(tags)
    if sample_size is not None:
        queryString += " --sample_size '%s' "%str(sample_size)
    if cluster_label is not None:
        queryString += " --cluster-label '%s' "%str(cluster_label)
    if notify is not None:
        queryString += " --notify '%s' "%str(notify)
    if name is not None:
        queryString += " --name '%s' "%str(name)

    #print "query is: "+query+"\n"
    #query = str(query) #because r passes string as unicode
    #arguments = str("")
    #api_token = str(api_token)
    
    
    if chatty:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARN)
    if api_token is None:
        sys.stderr.write("No API Token provided\n")
        #usage(optparser)
    if api_url is None:
        api_url = "https://api.qubole.com/api/"
    if api_version is None:
        api_version = "v1.2"
    if poll_interval is None:
        poll_interval = 5
    if skip_ssl_cert_check is None:
        skip_ssl_cert_check = False
    elif skip_ssl_cert_check:
        log.warn("Insecure mode enabled: skipping SSL cert verification\n")
    Qubole.configure(api_token=api_token,
            api_url=api_url,
            version=api_version,
            poll_interval=poll_interval,
            skip_ssl_cert_check=skip_ssl_cert_check)


    try:
        return(hivecommand(queryString))
    except qds_sdk.exception.Error as e:
        sys.stderr.write("Error: Status code %s (%s) from url %s\n" %
                         (e.request.status_code, e.__class__.__name__,
                          e.request.url))
        
    except qds_sdk.exception.ConfigError as e:
        sys.stderr.write("Configuration error: %s\n" % str(e))
        
    except qds_sdk.exception.ParseError as e:
        sys.stderr.write("Error: %s\n" % str(e))
        #sys.stderr.write("Usage: %s\n" % e.usage)
        
    except Exception:
        traceback.print_exc(file=sys.stderr)
        
if __name__ =='main':
    print hivecommand_from_r()

#Qubole.configure(api_token='7qpdaKMjWH4RzvsqGyG1ygcafqgBzsxr2d2ykz7SsBgTtY7cSs4uG9YdaBHHZWsU')



