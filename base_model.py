import uuid
"""base model of the airbnb project"""
class BaseModel:
    """base model 
    """
    def __init__(self) -> None:
        self.id = uuid.uuid4()
        id = str(id)