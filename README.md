qdssdkr
=========
A python and R wrapper code for launching HiveQueries using qds-sdk-py

Requires
--------
[qds-python-sdk] ( https://github.com/qubole/qds-sdk-py)


Installation:
-------------
In R
  
    install.packages("devtools")
    devtools::install_github("KarandeepJohar/qdssdkr")

Usage:
------
    library(qdssdkr)
    results<-quboleHiveCommand(query="sample query")


