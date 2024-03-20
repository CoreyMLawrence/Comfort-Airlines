# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Will Wadsworth
# Date: 2/19/2024
#
# Description:
#   This module defines several "processors" for logging with the structlog library.
#   A processor is a function in a function pipeline that transforms a log event.
#   For example, the `processor_code_location` function adds information about the source
#   code to all log events.
import inspect
import os

from helpers.reference_wrapper import ReferenceWrapper

class CodeLocation:
    STRUCTLOG_STACK_FRAME_OFFSET = 4

    @staticmethod
    def __call__(logger, log_method, event_dict):
        frame_info = inspect.getouterframes(inspect.currentframe())[CodeLocation.STRUCTLOG_STACK_FRAME_OFFSET]
        
        event_dict["source_file"] = os.path.basename(frame_info.filename)
        event_dict["source_function"] = frame_info.function
        event_dict["source_line"] = frame_info.lineno
        
        return event_dict

class ProcessorID:
    def __init__(self):
        self.id = 0

    def __call__(self, _, __, event_dict):
        event_dict["Log_id"] = self.id
        self.id += 1
        return event_dict
    
class ProcessorSimulationTime:
    def __init__(self, wrapper: ReferenceWrapper):
        self.wrapper = wrapper

    def __call__(self, _, __, event_dict): 
        event_dict["simulation_time"] = self.wrapper.value
        return event_dict