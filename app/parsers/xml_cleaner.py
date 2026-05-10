from bs4 import BeautifulSoup
import re
from typing import List
from ..models.document import ContentBlock, DocumentFormat, ParsedDocument

class MarkupParser:
    """
    Parses messy raw XML and HTML content into normalized structured sections
    suitable for automated ePublishing, indexing, and headless CMS distribution.
    """

    @staticmethod
    def parse_markup(raw_content: str, doc_format: DocumentFormat) -> ParsedDocument:
        parser_type = "lxml-xml" if doc_format == DocumentFormat.XML else "html.parser"
        soup = BeautifulSoup(raw_content, parser_type)

        # Extract title
        title_tag = soup.find(["title", "h1", "book-title", "doc-title"])
        title = title_tag.get_text().strip() if title_tag else "Untitled Document"

        sections: List[ContentBlock] = []

        # Find all textual and structural elements
        for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "blockquote"]):
            tag_name = element.name.lower()
            text = element.get_text().strip()

            if not text:
                continue

            # Clean multiple spaces and linebreaks
            cleaned_text = re.sub(r'\s+', ' ', text)

            if tag_name.startswith("h") and len(tag_name) == 2 and tag_name[1].isdigit():
                level = int(tag_name[1])
                sections.append(ContentBlock(
                    block_type="heading",
                    level=level,
                    text_content=cleaned_text,
                    attributes={"tag": tag_name}
                ))
            elif tag_name == "p":
                sections.append(ContentBlock(
                    block_type="paragraph",
                    text_content=cleaned_text
                ))
            elif tag_name == "li":
                sections.append(ContentBlock(
                    block_type="list_item",
                    text_content=cleaned_text
                ))
            elif tag_name == "pre":
                sections.append(ContentBlock(
                    block_type="code_block",
                    text_content=text  # Preserve indentation
                ))

        all_text = " ".join(s.text_content for s in sections)
        words = all_text.split()

        return ParsedDocument(
            title=title,
            detected_format=doc_format,
            character_count=len(all_text),
            word_count=len(words),
            sections=sections,
            metadata={
                "extracted_blocks_count": len(sections),
                "has_code_blocks": any(s.block_type == "code_block" for s in sections)
            }
        )
