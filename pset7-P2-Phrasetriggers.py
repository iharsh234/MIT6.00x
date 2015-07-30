# PART 2: TRIGGERS (PHRASETRIGGERS)


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



class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
    def evaluate(self,story):
     if story.getTitle():
        return self.phrase in story.getTitle()
     if story.getSubject():
        return self.phrase in story.getSubject()
     if story.getSummary():
        return self.phrase in story.getSummary()
       
