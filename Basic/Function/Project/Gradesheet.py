# Suppose you are a teaching assistant at a university and you need to assign grades to students based on their average scores.

# The scores obtained by a student in various subjects are stored in a list like this:

# scores = [55, 64, 75, 80, 65]
# Your job is to first compute the average score first.

# Then, based on the average score, you need to compute students' grades.

# The grading rule is as follows:

# Grade A if the average score is equal to or above 80
# Grade B if the average score is equal to or above 60 and less than 80
# Grade C if the average score is equal to or above 50 and less than 60
# Grade F if the average score is less than 50
def getAverage(scores):
  totalScore = sum(scores)
  averageMark =totalScore / len(scores)
  return averageMark

scores = [89,78,63,90,84]

average = getAverage(scores)
print(average)


def compute_grade(average):
  if average >= 80:
    grade = "A"
  elif average >=60:
    grade = "B"
  elif average >=50:
    grade = "C"
  else:
    grade = "F"
  return grade

result = compute_grade(average)
print(result)
