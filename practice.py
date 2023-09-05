print("Good morning")

print("Good afternoon")

print("Good evening")

num1 = 1
print(num1)

num2 = 2.0
print(num2)

print(num1 < num2)

hello = "hello"
print(type(hello))

list = [1, 2, 3]
print(list)
print(list[0])

list2 = [[1, 2], [3]]
print(list2[0][1])

age = 20
if age >= 18:
  print("You are old enough to vote!")
elif age >= 16:
  print("You are old enough to drive")
else:
  print("You are too young to vote or drive")


for i in range(5):
  if i == 2:
    break
  print(i)

for i in range(5):
  if i == 2:
    continue
  print(i)

for i in range(3):
  for j in range(3):
    print(i, j, sep="-")

arr = ["a", "b", "c"]
for i in arr:
  print(i)

arr2 = [["a", "b"], ["c", "d"]]
for i in arr2:
  for j in i:
    print(j)

def say_hello():
  print("Hello")

say_hello()

def say_hi(name):
  print(f"Hello {name}")

say_hi("John")

# クラス内の関数 = メソッド, クラス内の変数 = アトリビュート
class Student:
  def avg(self, math = 0, english = 0): # メソッドの引数にはselfを書くが省略可能
    print((math + english) / 2)

  def judge(self, score):
    if score >= 60:
      print("合格")
    else:
      print("不合格")

student1 = Student()
student1.avg(math = 80, english = 70)

student1.name = "Ken" # アトリビュートはクラス内に宣言してなくてもOK（今回の場合はname）
print(student1.name)

class Teacher:
  def __init__(self, name):
    self.name = name

teacher1 = Teacher("Kathy")
print(teacher1.name)

class Student2:
  def __init__(self, name):
    self.name = name

  def calc_avg(self, data):
    sum = 0
    for i in data:
      sum += i
    avg = sum / len(data)
    return avg

  def judge(self, avg):
    if avg >= 60:
      print("passed")
    else:
      print("failed")

student2 = Student2("Sam")
student2.calc_avg([80, 70])
student2.judge(student2.calc_avg([80, 70]))