import time 
  
  
def timed(func): 
    def wrapper(*args, **kwargs): 
        time_start = time.time() 
        result = func(*args, **kwargs) 
        time_end = time.time() 
          
        print(f"\n{func.__name__}: {time_end - time_start} seconds") 
        return result 
    return wrapper