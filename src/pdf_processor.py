import PyPDF2
from typing import List


class PDFProcessor:
    @staticmethod
    # chunking 5 pages at a time
    def extract_text(pdf_path: str, pages_per_chunk: int = 5) -> List[str]:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            chunks = []
            current_chunk = ""
            for i, page in enumerate(reader.pages):
                current_chunk += page.extract_text()
                if (i + 1) % pages_per_chunk == 0:
                    chunks.append(current_chunk)
                    current_chunk = ""
            if current_chunk:
                chunks.append(current_chunk)
        return chunks

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 2000) -> List[str]:
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
