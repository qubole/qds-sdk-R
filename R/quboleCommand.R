library(R6)
QuboleCommand <- R6Class("QuboleCommand",public = list(
  api_token = NULL,
  poll_interval = 5,
  initialize = function(api_token,poll_interval)
    {
    if (!missing(api_token)) self$api_token <- api_token
    if (!missing(poll_interval)) self$poll_interval <- poll_interval
    rPython::python.load(file.path(find.package("qds"),"exec","r-quboleCommand.py" ))
    rPython::python.call("connect",self$api_token,self$poll_interval)
    },
  #' Prints command object for a given commandId
  #' @method 
  check = function(commandId)
  {
    rPython::python.call("check",commandId)
  },
  #' Cancels the command, for a given commandId
  #' @method 
  cancel = function(commandId)
  {
    return(rPython::python.call("cancel",commandId))
  },
  #' Returns result of submitted command to stdout for a given commandId
  #' @method
  getresult = function(commandId)
  {
    return(rPython::python.call("getresult", commandId))
  },
  #' Returns the logs of the command for a give commandId
  #' @method 
  getlog = function(commandId)
  {
    return(rPython::python.call("getlog", commandId))
  }
  )
)

#'  Uses given authtoken to authenticate against the given api_url
#'  and returns and instance of qubole HiveCommand
#'  \url{http://qubole.com}
#'  \email{sdk-dev@@qubole.com}
#'  @param api_token A String
#'  @param poll_interval A Number
#'  @return the qubole HiveCommand instance
#'  @examples
#'  \dontrun{qubolehivecommand = HiveCommand("apitoken","pollinterval")}
#'  @export
HiveCommand <- R6Class("HiveCommand",inherit = QuboleCommand,public = list(
  #' Submits hive command and returns command id
  #' @method 
  submit = function(query=NULL, macros = NULL, tags = NULL, sample_size = NULL,
                    cluster_label = NULL, notify = NULL, name = NULL, 
                    script_location = NULL, print_logs = NULL)
    {
    commandId <- rPython::python.call("hivecommand",query = query,macros = macros,tags = tags,sample_size = sample_size,
                                      cluster_label = cluster_label,notify = notify,name = name,
                                      script_location = script_location,print_logs = print_logs)
    return(commandId)
    },
  #' Runs hive command and returns the results
  #' @method 
  run = function(query=NULL, macros = NULL, tags = NULL, sample_size = NULL,
                 cluster_label = NULL, notify = NULL, name = NULL,
                 script_location = NULL, print_logs = NULL)
    {
    results <- rPython::python.call("hivecommand",query = query,macros = macros,tags = tags,sample_size = sample_size,
                                    cluster_label = cluster_label,notify = notify,name = name,
                                    script_location = script_location,print_logs = print_logs,command_type = "run")
    return(results)
    }
  )
)

#'  Uses given authtoken to authenticate against the given api_url
#'  and returns and instance of qubole PrestoCommand
#'  \url{http://qubole.com}
#'  \email{sdk-dev@@qubole.com}
#'  @param api_token A String
#'  @param poll_interval A Number
#'  @return the qubole PrestoCommand instance
#'  @examples
#'  \dontrun{quboleprestocommand = PrestoCommand("apitoken")}
#'  @export
PrestoCommand <- R6Class("PrestoCommand",inherit = QuboleCommand,public = list(
  #' Submits presto command and returns command id
  #' @method 
  submit = function(query = NULL, script_location = NULL, macros = NULL , tags = NULL,
                    cluster_label = NULL, notify = NULL, name = NULL, print_logs = NULL)
    {
    commandId <- rPython::python.call("prestocommand",query = query,script_location = script_location,macros = macros,
                                      tags = tags,cluster_label = cluster_label,notify = notify,name = name,
                                      print_logs = print_logs)
    return(commandId)
    },
  #' Runs presto command and returns the results
  #' @method 
  run = function(query = NULL, script_location = NULL, macros = NULL , tags = NULL,
                 cluster_label = NULL, notify = NULL, name = NULL, print_logs = NULL)
    {
    result <- rPython::python.call("prestocommand",query = query,script_location = script_location,macros = macros,
                                   tags = tags,cluster_label = cluster_label,notify = notify,name = name,
                                   print_logs = print_logs,command_type = "run")
    return(result)
    }
  )
)

#'  Uses given authtoken to authenticate against the given api_url
#'  and returns and instance of qubole SparkCommand
#'  \url{http://qubole.com}
#'  \email{sdk-dev@@qubole.com}
#'  @param api_token A String
#'  @param poll_interval A Number
#'  @return the qubole SparkCommand instance
#'  @examples
#'  \dontrun{qubolesparkcommand = SparkCommand("apitoken")}
#'  @export
SparkCommand <- R6Class("SparkCommand",inherit = QuboleCommand,public = list(
  #' Submits presto command and returns command id
  #' @method
  submit = function(program = NULL, cmdline = NULL, sql = NULL, script_location = NULL,
                    macros = NULL , tags = NULL, cluster_label = NULL, language = NULL,
                    app_id = NULL, notify = NULL, name = NULL, arguments = NULL,
                    user_program_arguments = NULL, print_logs = NULL)
    {
    commandId <- rPython::python.call("sparkcommand",program = program,cmdline = cmdline,sql = sql,
                                      script_location = script_location,macros = macros,tags = tags,
                                      cluster_label = cluster_label,language = language,app_id = app_id,
                                      notify = notify,name = name,arguments = arguments,
                                      user_program_arguments = user_program_arguments,print_logs = print_logs)
    return(commandId)
    },
  #' Runs presto command and returns the results
  #' @method 
  run = function(program = NULL, cmdline = NULL, sql = NULL, script_location = NULL,
                 macros = NULL , tags = NULL, cluster_label = NULL, language = NULL,
                 app_id = NULL, notify = NULL, name = NULL, arguments = NULL,
                 user_program_arguments = NULL, print_logs = NULL)
    {
    result <- rPython::python.call("sparkcommand",program = program,cmdline = cmdline,sql = sql,
                                   script_location = script_location,macros = macros,tags = tags,
                                   cluster_label = cluster_label,language = language,app_id = app_id,
                                   notify = notify,name = name,arguments = arguments,
                                   user_program_arguments = user_program_arguments,print_logs = print_logs,
                                   command_type = "run")
    return(result)
    }
  )
)

