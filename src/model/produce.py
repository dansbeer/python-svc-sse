from pydantic import BaseModel
from typing import Optional, List

class MessageProduce(BaseModel):
    full_name: Optional[str]
    progress: Optional[str]
    status: Optional[str]
    files_name: List[str]
    message: Optional[str]
    upload_at: Optional[int]