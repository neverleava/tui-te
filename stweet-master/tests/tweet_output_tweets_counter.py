from typing import List

import stweet as st


class TweetOutputTweetsCounter(st.TweetOutput):
    counter: int

    def __init__(self):
        self.counter = 0

    def export_tweets(self, tweets: List[st.UserTweetRaw]):
        self.counter += len(tweets)
        return

    def get_output_call_count(self) -> int:
        return self.counter
