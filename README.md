qds.sdk.R
=========
A python and R wrapper code for launching HiveQueries using qds-sdk-py

Requires
--------
[qds-python-sdk] ( https://github.com/qubole/qds-sdk-py)

    cd /path/to/qds-python-sdk/directory 
    sudo python setup.py install

[rPython] (http://cran.r-project.org/web/packages/rPython/)

    install.packages("rPython")

Installation:
-------------
In R
  
    install.packages("devtools")
    devtools::install_github("KarandeepJohar/qds.sdk.R")

Usage:
------
In R

    library(qds.sdk.R)
    results<-qds.sdk.R::quboleHiveCommand(query="sample query")

Optional:
---------
To change default qds env variables
In shell

    $ export QDS_API_TOKEN = xxyyzz
    $ export QDS_API_URL = xyz/xyz
    $ export QDS_API_VERSION = 1.2

Additionally you can also use sampling in Hive. For further details read this [page] (https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Sampling).
