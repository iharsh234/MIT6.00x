# PART 2: TRIGGERS (COMPOSITETRIGGERS)

# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word

    def isWordIn(self,text):
        word = self.word
        word = word.lower()
        text = text.lower()

        import string
        for x in string.punctuation:
              word = word.replace(x,"")
              text = text.replace(x,"")
        word = word.split()
        text = text.split()
        for word in word:
          if word not in text:
            return False
          else:return True


class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())


class NotTrigger(Trigger):
    def __init__(self,word):
        self.word = word
    def evaluate(self,story):
        return not self.word.isWordIn(story.getTitle())
            
class AndTrigger(Trigger):
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
    def evaluate(self,story):
        return self.word1.isWordIn(story.getTitle()) and self.word2.isWordIn(story.getTitle())

class OrTrigger(Trigger):
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
    def evaluate(self,story):
        return self.word1.isWordIn(story.getTitle()) or self.word2.isWordIn(story.getTitle())
