def theory_question():

    question = "Explain the process of photosynthesis."
    
    theory_results = {
        "photosynthesis": 2,
        "light energy": 1,
        "chemical energy": 1,
        "chloroplasts": 2,
        "chlorophyll": 1,
        "carbon dioxide": 1,
        "water": 1,
        "glucose": 1,
        "oxygen": 1,
        "ATP": 1
    }
    
    print()
    print("Question:", question)
    student_answer = input("Enter your answer here: ").strip().lower()
    total_score = 0
    max_score = sum(theory_results.values())
    
    for keyword, point in theory_results.items():
        if keyword in student_answer:
            total_score += point
    
    print()
    print(f"Your total score is {total_score} out of {max_score}.")

theory_question()
