from pydantic import BaseModel
from typing import List, Optional

class AgentResponse(BaseModel):
    success: bool
    data: str
    error: Optional[str] = None

class CodeSpec(BaseModel):
    function_name: str
    arguments: List[str]
    return_type: str
    logic_description: str
