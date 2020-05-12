"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
   """Represents a student."""

   def __init__(self, name, number):
      """All scores are initially 0."""
      self._name = name
      self._scores = []
      for count in range(number):
         self._scores.append(0)

   def getName(self):
      """Returns the student's name."""
      return self._name

   def setScore(self, i, score):
      """Resets the ith score, counting from 1."""
      self._scores[i - 1] = score

   def getScore(self, i):
      """Returns the ith score, counting from 1."""
      return self._scores[i - 1]

   def getAverage(self):
      """Returns the average score."""
      return sum(self._scores) / len(self._scores)

   def getHighScore(self):
      """Returns the highest score."""
      return max(self._scores)

   def __str__(self):
      """Returns the string representation of the student."""
      return "Name: " + self._name  + "\nScores: " + \
             " ".join(map(str, self._scores))

   def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            print (type(self), type(other))
            return False
        else:
            return self.getHighScore() == other.getHighScore()

   def __lt__(self, others):
      return  self.getHighScore() < others.getHighScore()

def main():
    sList = []
    s1 = Student('Bob Day', 2)
    s1.setScore(1, 90)
    s1.setScore(2, 80)
    s2 = Student('Hunter Bertoson', 2)
    s2.setScore(1, 96)
    s2.setScore(2, 83)
    s3 = Student('Landon Morris', 2)
    s3.setScore(1, 23)
    s3.setScore(2, 34)
    s4 = Student('Curtis Bohannan', 2)
    s4.setScore(1, 99)
    s4.setScore(2, 89)
    sList.append(s1)
    sList.append(s2)
    sList.append(s3)
    sList.append(s4)
    for i in range(len(sList)):
        print (sList[i])
    sList.sort()
    print ("-----sorted-----")
    for i in range(len(sList)):
        print (sList[i])
main()

