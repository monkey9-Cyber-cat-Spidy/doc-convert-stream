from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from enum import Enum

class DocumentFormat(str, Enum):
    XML = "XML"
    HTML = "HTML"
    MARKDOWN = "MARKDOWN"
    JSON = "JSON"

class ContentBlock(BaseModel):
    block_type: str = Field(..., description="e.g., heading, paragraph, list, table, code")
    level: Optional[int] = Field(None, description="Heading level 1-6 if applicable")
    text_content: str
    attributes: Dict[str, Any] = Field(default_factory=dict)

class ParsedDocument(BaseModel):
    title: str
    detected_format: DocumentFormat
    character_count: int
    word_count: int
    sections: List[ContentBlock]
    metadata: Dict[str, Any] = Field(default_factory=dict)
    processed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ConversionRequest(BaseModel):
    raw_content: str
    source_format: DocumentFormat
    target_format: DocumentFormat = DocumentFormat.JSON
    clean_whitespace: bool = True
