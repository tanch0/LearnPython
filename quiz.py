questions = [
    {
        "prompt": "1. Which of the following is a valid variable name in Python?",
        "options": ["A. 2variable", "B. variable_name", "C. variable-name"],
        "answer": "B"
    },
    {
        "prompt": "2. What is the output of: print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9"],
        "answer": "B"
    },
    {
        "prompt": "3. Which data type is immutable in Python?",
        "options": ["A. List", "B. Tuple", "C. Dictionary"],
        "answer": "B"
    },
    {
        "prompt": "4. What is the correct way to create a function in Python?",
        "options": ["A. function myFunc():", "B. def myFunc():", "C. create myFunc():"],
        "answer": "B"
    },
    {
        "prompt": "5. Which method is used to add an element to the end of a list?",
        "options": ["A. append()", "B. add()", "C. insert()"],
        "answer": "A"
    },
    {
        "prompt": "6. What will be the output of: print(type([]))?",
        "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'dict'>"],
        "answer": "A"
    },
    {
        "prompt": "7. What is the result of: 'Hello' + 'World'?",
        "options": ["A. Hello World", "B. HelloWorld", "C. Error"],
        "answer": "B"
    },
    {
        "prompt": "8. Which of the following is used to handle exceptions in Python?",
        "options": ["A. try-except", "B. if-else", "C. for-while"],
        "answer": "A"
    },
    {
        "prompt": "9. What will be the output of: print(bool(0))?",
        "options": ["A. True", "B. False", "C. None"],
        "answer": "B"
    },
    {
        "prompt": "10. What keyword is used to define a class in Python?",
        "options": ["A. def", "B. class", "C. module"],
        "answer": "B"
    }
]


def quiz(questions):
    score = 0
    valid_inputs = ["A", "B", "C", "D", "a", "b", "c", "d"]
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer: ").upper()

        while user_answer not in valid_inputs:
            print("Invalid input. Please try again.")
            user_answer = input("Your answer: ").upper()

        if user_answer == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print(F"Incorrect! The correct answer is: {question['answer']}. You got {score} out of {len(questions)}d!")

    print(f"You scored {score} out of {len(questions)}")


quiz(questions)