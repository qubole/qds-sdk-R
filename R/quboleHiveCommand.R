
library(rPython)
#setwd("~/Downloads/qds-sdk-py")
# Load/run the main Python script
#'  calls hivecommand_from_r and return the result
#'  
#'  \url{http://qubole.com}
#'  \email{karandeepj@@qubole.com}
#'  @param query A String
#'  @param script_location A String
#'  @param macros A String
#'  @param tags A String
#'  @param sample_size A Number
#'  @param cluster_label A String
#'  @param notify A Boolean
#'  @param name A String
#'  @param poll_interval A Number
#'  @param api_token A String
#'  @param api_url A String
#'  @param api_version A Number
#'  @param skip_ssl_cert_check A Boolean
#'  @param verbose A Boolean
#'  @param chatty A Boolean
#'  @return the results of the query
#'  @examples
#'  quboleHiveCommand("show tables")
#'  @export
#quboleHiveCommand<-function(query=NULL, script_location=NULL, macros=NULL , tags=NULL, sample_size=NULL, cluster_label=NULL, notify=NULL, name=NULL, poll_interval=15,api_token=NULL, )
quboleHiveCommand<-function(...){ 
    
    rPython::python.load(file.path(find.package("qdssdkr"),"exec","r-python.py" ))
    
    #results<-python.call("hivecommand_from_r", query, script_location, macros , tags, sample_size, cluster_label, notify, name, poll_interval, api_token)
    
    results<-rPython::python.call("hivecommand_from_r",...)
  
    cat(results)
}

