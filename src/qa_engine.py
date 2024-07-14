from openai import OpenAI
from typing import List, Dict
from .config import MODEL_NAME, MAX_TOKENS, TEMPERATURE


class QAEngine:
    @staticmethod
    def summarize_text(text: str) -> str:
        prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
        client = OpenAI()
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system",
                    "content": "You are a helpful assistant that summarizes text, and never miss out any key details."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=MAX_TOKENS,
            n=1,
            temperature=TEMPERATURE,
        )
        return response.choices[0].message.content.strip()

    @staticmethod
    def answer_questions(summary: str, questions: List[str]) -> Dict[str, str]:
        client = OpenAI()
        answers = {}
        for question in questions:
            prompt = f"Context: {summary}\n\nQuestion: {question}\n\nAnswer:"
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=MAX_TOKENS,
                n=1,
                temperature=TEMPERATURE,
            )
            answer = response.choices[0].message.content.strip()
            answers[question] = answer if answer else "Data Not Available"
        return answers

    @staticmethod
    def process_pdf_chunks(chunks: List[str], progress) -> str:
        current_summary = ""
        total_chunks = len(chunks)
        for i, chunk in enumerate(chunks, 1):
            progress.update_status(f"Processing chunk {i}/{total_chunks}")
            if current_summary:
                combined_text = f"Previous summary:\n{
                    current_summary}\n\nNew content:\n{chunk}"
                current_summary = QAEngine.summarize_text(combined_text)
            else:
                current_summary = QAEngine.summarize_text(chunk)
        return current_summary
