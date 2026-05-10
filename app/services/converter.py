from ..models.document import ConversionRequest, ParsedDocument, DocumentFormat
from ..parsers.xml_cleaner import MarkupParser

class DocumentConversionService:
    @staticmethod
    def process_conversion(request: ConversionRequest) -> ParsedDocument:
        parsed = MarkupParser.parse_markup(request.raw_content, request.source_format)
        return parsed

    @staticmethod
    def export_as_markdown(doc: ParsedDocument) -> str:
        md_lines = [f"# {doc.title}\n"]
        for sec in doc.sections:
            if sec.block_type == "heading":
                prefix = "#" * (sec.level or 2)
                md_lines.append(f"{prefix} {sec.text_content}\n")
            elif sec.block_type == "paragraph":
                md_lines.append(f"{sec.text_content}\n")
            elif sec.block_type == "list_item":
                md_lines.append(f"- {sec.text_content}")
            elif sec.block_type == "code_block":
                md_lines.append(f"```\n{sec.text_content}\n```\n")
        return "\n".join(md_lines)
