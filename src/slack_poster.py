from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from typing import Dict
from .config import SLACK_BOT_TOKEN, SLACK_CHANNEL


class SlackPoster:
    def __init__(self):
        self.client = WebClient(token=SLACK_BOT_TOKEN)

    def post_results(self, results: Dict[str, str]):
        formatted_results = self._format_results(results)
        try:
            response = self.client.chat_postMessage(
                channel=SLACK_CHANNEL,
                text="Here are the answers to your questions:",
                blocks=[
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "Here are the answers to your questions:"}
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": formatted_results}
                    }
                ]
            )
            print(f"Message posted: {response['ts']}")
        except SlackApiError as e:
            print(f"Error posting message: {e}")

    def _format_results(self, results: Dict[str, str]) -> str:
        formatted = ""
        for question, answer in results.items():
            formatted += f"*Q: {question}*\n"
            formatted += f"A: {answer}\n\n"
        return formatted
