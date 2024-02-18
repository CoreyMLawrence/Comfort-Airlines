import inspect
from reference_wrapper import ReferenceWrapper

def processor_code_location(logger, log_method, event_dict):
    STRUCTLOG_STACK_FRAME_OFFSET = 4

    frame_info = inspect.getouterframes(inspect.currentframe())[4]
    event_dict["source_file"] = frame_info.filename
    event_dict["source_function"] = frame_info.function
    event_dict["source_line"] = frame_info.lineno
    
    return event_dict

class ProcessorID:
    def __init__(self, id_seed: int = 0):
        self.id = id_seed

    def __call__(self, _, __, event_dict):
        event_dict["id"] = self.id
        self.id += 1
        return event_dict
    
class ProcessorSimulationTime:
    def __init__(self, wrapper: ReferenceWrapper):
        self.wrapper = wrapper

    def __call__(self, _, __, event_dict): 
        event_dict["simulation_time"] = self.wrapper.value
        return event_dict