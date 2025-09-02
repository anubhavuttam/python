# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.


questions =[ "Which of the following countries is the world's largest producer of saffron?", "Spain", "Iran", "India", "Greece",

 "Which god is also known as ‘Gauri Nandan’?", "Agni", "Indra", "Hanuman", "Ganesha" ,

 "What does not grow on tree according to a popular Hindi saying?", "Money", "Flowers", "Leaves", "Fruits" ,

 "Which city is known as the Pink City of India?", "Jaipur", "Kanpur", "Mumbai", "Delhi",

 "Who wrote India's National Anthem?", "Gandhi", "Nehru", "Rabindranath Tagore","BR Ambedkar" ]

n = len(questions) 

answers = [2, 4, 1, 1, 3]  # Correct option numbers

levels = [1000,2000,3000,5000,10000]

i=0

# Variable to track if the user answers all correctly
correct_answers_count = 0

# Loop through questions in steps of 5 (1 question + 4 options)
for i in range(0,n,5) :
    print(f"\nQuestion for Rs. {levels[i//5]}:")
    print(questions[i]) # Print the question

    # Print options
    print(questions[i+1])
    print(questions[i+2])
    print(questions[i+3])
    print(questions[i+4])

    # Get user input
    user_answer = int(input("Please enter the correct option number: "))

    # Check answer

    if user_answer == answers[i // 5]:  # Correct answer index
        print(f"Correct! You won Rs. {levels[i//5]}")
        correct_answers_count += 1  # Increment counter for correct answers
    else:
        print("Wrong answer! Game over.")
        break  # Stop the game if the answer is wrong


if correct_answers_count == 5:
    print("\nCongratulations! You've answered all questions correctly and won Rs. 10000!")