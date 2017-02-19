import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # store
        self.poswords = set()
        self.negwords = set()

        pos_file = open(positives, "r")
        for line in pos_file:
            if not line.startswith(";"):
                self.poswords.add(line.rstrip("\n"))
        pos_file.close()

        pos_file = open(negatives, "r")
        for line in pos_file:
            if not line.startswith(";"):
                self.negwords.add(line.rstrip("\n"))
        pos_file.close()


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        score = 0.0
        word_list = text.split()

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        for word in tokens:
            if word.lower() in self.poswords:
                score += 1
            if word.lower() in self.negwords:
                score -= 1

        return score
