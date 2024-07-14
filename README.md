# PDF Q&A Agent

This application extracts answers from a PDF document based on given questions and posts the results to Slack using OpenAI's language models.

## Features

- Extracts text from PDF documents
- Answers questions using OpenAI's GPT model
- Posts results to Slack in a structured JSON format
- Handles large PDFs by chunking the text

## Installation

1. Clone the repository:

```
git clone https://github.com/rksainath/pdf-qa-agent.git
cd pdf-qa-agent
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:

```
OPENAI_API_KEY=your_openai_api_key
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_CHANNEL=your_slack_channel_id
```

## Usage

Run the application from the command line:

```
python -m src.main path/to/your/document.pdf "Question 1?" "Question 2?" "Question 3?"
```

The application will process the PDF, answer the questions, and post the results to the specified Slack channel.

## Testing

To run the tests, use the following command:

```
python -m unittest discover tests
```
