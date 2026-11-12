
name = input("What is your name? ")

questions = [
    {
        "question": "Why did Darth Vader redeem himself?",
        "options": [
            "A. The Emperor was a diva.",
            "B. His son was going to die.",
            "C. Luke had the high ground."
        ],
        "answer": "B"
    },
    {
        "question": "Who trained Obi-Wan Kenobi?",
        "options": [
            "A. Yoda.",
            "B. Qui-Gon Jinn.",
            "C. Mace Windu."
        ],
        "answer": "B"
    },
    {
        "question": "What does a Jedi need to build a lightsaber?",
        "options": [
            "A. A Kyber crystal.",
            "B. A Death Star stone.",
            "C. A spaceship engine."
        ],
        "answer": "A"
    },
    {
        "question": "Who built C-3PO?",
        "options": [
            "A. Luke Skywalker.",
            "B. Emperor Palpatine.",
            "C. Anakin Skywalker."
        ],
        "answer": "C"
    },
    {
        "question": "What is Chewbacca's home planet?",
        "options": [
            "A. Kashyyyk.",
            "B. Tatooine.",
            "C. Naboo."
        ],
        "answer": "A"
    },
    {
        "question": "What is Han Solo's ship called?",
        "options": [
            "A. Tantive IV.",
            "B. Millennium Falcon.",
            "C. Star Destroyer."
        ],
        "answer": "B"
    },
    {
        "question": "Who is Luke Skywalker's mother?",
        "options": [
            "A. Leia Organa.",
            "B. Padme Amidala.",
            "C. Shmi Skywalker."
        ],
        "answer": "B"
    }
]

score = 0

for q in questions:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Your answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz finished!")
print("Congratulations,", name)
print("You got", score, "out of", len(questions), "correct!")
