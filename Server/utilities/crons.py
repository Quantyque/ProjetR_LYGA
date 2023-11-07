from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from logs import log_info, log_error
from constants import INTERNAL_ERROR

#************************************************************************************************
# Utilities : CRONS
#************************************************************************************************

class Crons:

    def __init__(self) -> None:
        self.__task_functions = {}

    def start_cron_task(self, function_name: str, function: callable):
        try:
            if function_name in self.__task_functions:
                return f"Task '{function_name}' is already running"

            scheduler = BackgroundScheduler()
            scheduler.add_job(function, 'cron', hour=0, minute=0)  # 00:00 AM
            scheduler.start()
            
            self.__task_functions[function_name] = scheduler

            return f"Task '{function_name}' started"
            
        except Exception as e:
            log_error(str(e))
            return INTERNAL_ERROR, 500

    def stop_cron_task(self, function_name: str) -> str:
        try:
            message = ""

            if function_name in self.__task_functions:
                scheduler = self.__task_functions[function_name]
                scheduler.shutdown()
                del self.__task_functions[function_name]
                message = f"Task '{function_name}' stopped"
            else:
                message = f"Task '{function_name}' not found"

            return message
            
        except Exception as e:
            log_error(str(e))
            return INTERNAL_ERROR, 500

    def get_cron_tasks(self) -> dict:
        return list(self.__task_functions.keys())