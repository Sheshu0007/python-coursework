quiz = {
    1: {
        "Question": "Question 1: What is the output of: print(type(lambda x: x))?",
        "a": "a) <class 'function'>",
        "b": "b) <class 'lambda'>",
        "c": "c) <class 'method'>",
        "d": "d) <class 'generator'>",
        "answer": "a"
    },
    2: {
        "Question": "Question 2: Which of these data types is immutable?",
        "a": "a) list",
        "b": "b) dict",
        "c": "c) tuple",
        "d": "d) set",
        "answer": "c"
    },
    3: {
        "Question": "Question 3: What does the '//' operator do in Python?",
        "a": "a) Floating point division",
        "b": "b) Integer (floor) division",
        "c": "c) Modulus operation",
        "d": "d) Bitwise AND",
        "answer": "b"
    },
    4: {
        "Question": "Question 4: How do you insert an element at the beginning of a list?",
        "a": "a) list.add(0, element)",
        "b": "b) list.insert(0, element)",
        "c": "c) list.append(element)",
        "d": "d) list[0] = element",
        "answer": "b"
    },
    5: {
        "Question": "Question 5: Which of these is a mutable data type?",
        "a": "a) string",
        "b": "b) tuple",
        "c": "c) list",
        "d": "d) frozenset",
        "answer": "c"
    },
    6: {
        "Question": "Question 6: What does the 'pass' statement do in Python?",
        "a": "a) Exits a function",
        "b": "b) Does nothing (placeholder)",
        "c": "c) Skips to next iteration",
        "d": "d) Raises an error",
        "answer": "b"
    },
    7: {
        "Question": "Question 7: How can you create a dictionary in Python?",
        "a": "a) {}",
        "b": "b) []",
        "c": "c) ()",
        "d": "d) <>",
        "answer": "a"
    },
    8: {
        "Question": "Question 8: What is the output of: print(0.1 + 0.2 == 0.3)?",
        "a": "a) True",
        "b": "b) False",
        "c": "c) Error",
        "d": "d) None",
        "answer": "b"
    },
    9: {
        "Question": "Question 9: What is the output of this code?\nprint('Python'[::-1])",
        "a": "a) Python",
        "b": "b) nohtyP",
        "c": "c) Pytho",
        "d": "d) nohtyp",
        "answer": "b"
    },
    10: {
        "Question": "Question 10: What is the default return value of a function in Python?",
        "a": "a) 0",
        "b": "b) None",
        "c": "c) False",
        "d": "d) '' (empty string)",
        "answer": "b"
    }
}
count=0
num=int(input("enter the question number"))
for i in range(1,len(quiz)+1):
    print(quiz[i]["Question"])
    print(quiz[i]["a"])
    print(quiz[i]["b"])
    print(quiz[i]["c"])
    print(quiz[i]["d"])

option=input("a,b,c,d").strip().lower()
if option==quiz[i]["answer"]:
    print("correct answer")
    count+=1
else:
    print("wrong answer")

print(f"the total score is {count}/{len(quiz)}")