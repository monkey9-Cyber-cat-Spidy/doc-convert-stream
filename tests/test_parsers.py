import pytest
from app.models.document import DocumentFormat
from app.parsers.xml_cleaner import MarkupParser

def test_xml_parsing_structure():
    sample_xml = """
    <document>
        <title>Engineering Specifications</title>
        <h1>System Overview</h1>
        <p>This is a paragraph describing the core cloud architecture.</p>
        <h2>Requirements</h2>
        <li>Low latency streaming</li>
        <li>Automated validation</li>
    </document>
    """
    parsed = MarkupParser.parse_markup(sample_xml, DocumentFormat.XML)
    assert parsed.title == "Engineering Specifications"
    assert len(parsed.sections) == 5
    assert parsed.sections[0].block_type == "heading"
    assert parsed.sections[0].level == 1
    assert parsed.sections[1].block_type == "paragraph"
    assert parsed.word_count > 5
