#!/usr/bin/env python
import sys
import warnings

from fionica_baby_chatbot.src.fionica_baby_chatbot.crew import FionicaBabyChatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def main():
    chatbot = FionicaBabyChatbot().crew()

    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("Enter a topic or query: ")
        if user_input.lower() == 'exit':
            print("Ending conversation. Goodbye!")
            break

        inputs = {'topic': user_input}
        response = chatbot.kickoff(inputs=inputs)
        print(f"AI Response: {response}")
main()



# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs',
#         'current_year': str(datetime.now().year)
#     }
#
#     try:
#         FionicaBabyChatbot().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")
#
#
# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         FionicaBabyChatbot().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")
#
# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         FionicaBabyChatbot().crew().replay(task_id=sys.argv[1])
#
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
#
# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#     try:
#         FionicaBabyChatbot().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
