from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models.document import ConversionRequest, ParsedDocument
from .services.converter import DocumentConversionService

app = FastAPI(
    title="doc-convert-stream",
    description="Learning project: Automated document conversion and structural normalization engine.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "HEALTHY", "service": "doc-convert-stream"}

@app.post("/api/v1/convert", response_model=ParsedDocument)
def convert_document(request: ConversionRequest):
    try:
        parsed = DocumentConversionService.process_conversion(request)
        return parsed
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/convert/markdown")
def convert_to_markdown(request: ConversionRequest):
    try:
        parsed = DocumentConversionService.process_conversion(request)
        md = DocumentConversionService.export_as_markdown(parsed)
        return {"title": parsed.title, "markdown": md}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
