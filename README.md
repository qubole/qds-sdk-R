qds.sdk.R
=========
A python and R wrapper code for launching HiveQueries using qds-sdk-py

Requires
--------
[qds-python-sdk] ( https://github.com/qubole/qds-sdk-py)


+ Install it from [pypi] (https://pypi.python.org/pypi/qds_sdk) - `pip install qds_sdk`

Or 

+ Download the package from [pypi] (https://pypi.python.org/pypi/qds_sdk) or [githib] ( https://github.com/qubole/qds-sdk-py)  
  
  then
  
    `cd /path/to/qds-python-sdk/directory`

    `sudo python setup.py install`

[rPython] (http://cran.r-project.org/web/packages/rPython/)

    install.packages("rPython")

Installation:
-------------
In R
  
    install.packages("devtools")
    devtools::install_github("qubole/qds-sdk-R")

Usage:
------
In Shell

    $ export QDS_API_TOKEN = xxyyzz
  
In R

    library(qds.sdk.R)
    results<-qds.sdk.R::quboleHiveCommand(query="show tables")

Optional:
---------
To change default qds env variables
In shell

    $ export QDS_API_TOKEN = xxyyzz
    $ export QDS_API_URL = https://api.qubole.com/api/
    $ export QDS_API_VERSION = v1.2

Notes:
------

default api_url is `https://api.qubole.com/api/`
default api_version is `v1.2`

Additionally you can also use sampling in Hive. For further details read this [page] (https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Sampling).
