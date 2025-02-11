def cbt_question():
    print(f"""
    Welcome to the Quiz!!!
    You are to answer all questtions correctly and each question gives you 5 point each 
    GOODLUCK!!!
""")
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
            "answer": "C"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A. 5", "B. 8", "C. 9", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
            "answer": "A"
        }
    ]

    score = 0
    print()
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        user_answer = input("Enter the correct answer from the given option A - D: ").upper()
        print()
        if user_answer == question["answer"]:
            score += 5

    print(f"You have completed the quiz! Your total score is: {score}")

    if score >= 15:
            print(f"You paseed the test successfully")
    else:
            print("You failed the test! your score is below average!")

cbt_question()
