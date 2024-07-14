import argparse
from typing import List
from .pdf_processor import PDFProcessor
from .qa_engine import QAEngine
from .slack_poster import SlackPoster
from .progress_indicator import ProgressIndicator


def main(pdf_path: str, questions: List[str]):
    progress = ProgressIndicator()
    progress.start()

    try:
        # Extract text chunks from PDF
        progress.update_status("Extracting text from PDF...")
        pdf_chunks = PDFProcessor.extract_text(pdf_path)

        # Process PDF chunks and get final summary
        progress.update_status("Summarizing PDF content...")
        qa_engine = QAEngine()
        final_summary = qa_engine.process_pdf_chunks(pdf_chunks, progress)

        # Get answers based on the final summary
        progress.update_status("Answering questions...")
        answers = qa_engine.answer_questions(final_summary, questions)

        # Initialize Slack poster
        slack_poster = SlackPoster()

        # Post results to Slack
        progress.update_status("Posting results to Slack...")
        slack_poster.post_results(answers)

        progress.update_status("Done!")
    finally:
        progress.stop()
    print("\nProcess completed. Check Slack for results.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Q&A Agent")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("questions", nargs="+",
                        help="List of questions to answer")
    args = parser.parse_args()

    main(args.pdf_path, args.questions)
