import random
questions = ["Why is the sky blue?: ", "Why is there a face on the moon?: ", "Where are all the dinosaurs?: "]
question = random.choice(questions)
answear = input(question.strip().lower())
while answear != 'just because':
    answear = input("why?: ").strip().lower()
