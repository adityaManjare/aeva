from pydantic import BaseModel , field_validator




class Chat(BaseModel):
    message: str
    n_results:int = 2 
    @field_validator('n_results')
    def max_relevant_chunks(cls,n_results):
        if n_results>3:
            raise ValueError("n_result cannot be greater than 3")
        
        return n_results
