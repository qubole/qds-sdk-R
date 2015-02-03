# Load/run the main Python script
#'  calls hivecommand_from_r  in /exec/r-python.py and return the result
#'  
#'  \url{http://qubole.com}
#'  \email{karandeepj@@qubole.com}
#'  @import rPython
#'  @param query A String
#'  @param poll_interval A Number
#'  @param sample_size A Number
#'  @param macros A String
#'  @param tags A String
#'  @param cluster_label A String
#'  @param notify A Boolean
#'  @param name A String
#'  @param api_token A String
#'  @return the results of the query
#'  @examples
#'  \dontrun{results = quboleHiveCommand("show tables", poll_interval = 5)}
#'  @export
quboleHiveCommand<-function(query = NULL, poll_interval = NULL, sample_size = NULL, macros = NULL, tags =NULL, cluster_label = NULL, notify = NULL, name = NULL, api_token = NULL){ 
    
    rPython::python.load(file.path(find.package("qds"),"exec","r-python.py" ))
    
    
    
    results<-rPython::python.call("hivecommand_from_r", query, poll_interval, sample_size, macros, tags, cluster_label, notify, name, api_token)
  
    cat(results)
}

