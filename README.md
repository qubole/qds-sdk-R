qds-sdk-R
=========
R wrapper code for launching Hive, Spark, Presto queries using qds-sdk-py.


Requires
--------
1. [QDS Python SDK](https://github.com/qubole/qds-sdk-py). To install it, you can either:

   + Install it from [PyPI](https://pypi.python.org/pypi/qds_sdk) - `pip install qds-sdk`.

   + Download the package from [GitHub](https://github.com/qubole/qds-sdk-py) and then
     ```
     cd /path/to/qds-sdk-py/
     sudo python setup.py install
     ```

2. [rPython](http://cran.r-project.org/web/packages/rPython/). In R,
    ```
    install.packages("rPython")
    ```


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

    library(qds)
    results<-qds::quboleHiveCommand(query="show tables")
    
Or
    
    library(qds)
    
    hive<-HiveCommand$new() 
    Or 
    hive<-HiveCommand$new(<apitoken>) 
    Or
    hive<-HiveCommand$new(<apitoken>,<pollinterval>)
    
    For Spark:
    spark<-SparkCommand$new()
    sparkCmdId<-spark$submit(sql="select * from default_qubole_memetracker limit 10")
    

Asynchronous 

    commandId<-hive$submit(query = "show tables")
    result<-hive$getresult(commandId)

Cancel

    hive$cancel(<commandId>)

Synchronous

    result<-hive$run(query = "show tables")

For results

    hive$getresult(<commandId>)
    
For logs

    hive$getlog(<commandId>)
    
To display command object

    hive$check(<commandId>)

Optional:
---------
To change the default QDS environment variables,

    $ export QDS_API_TOKEN = xxyyzz
    $ export QDS_API_URL = https://api.qubole.com/api/
    $ export QDS_API_VERSION = v1.2

Notes:
------

The default api_url is `https://api.qubole.com/api/`.

The default api_version is `v1.2`.

Additionally you can also use sampling in Hive. For further details read this [page](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Sampling).
