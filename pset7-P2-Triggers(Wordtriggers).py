# PART 2: TRIGGERS (WORDTRIGGERS)  

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


class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())
