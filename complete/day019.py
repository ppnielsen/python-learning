'''
Day 19 Cup of Code
'''

def prompts():
    '''
    Learning argument vector and prompts. Using input within code
    '''

    from sys import argv

    script, username = argv
    prompt = '>>> '

    # f before a string means format
    # the curly brackets are replacement strings
    print(f"Hi {username}, I'm the {script} script.")
    print("I'd like to ask a few questions.")
    print(f"What kind of computer are you learning to code on {username}?")
    learning = input(prompt)

    print(f"What is your favorite cpu {username}?")
    cpu = input(prompt)

    print("Do you have a GPU?")
    gpu = input(prompt)

    print(f"""
Alright, so you are learning to code on a {learning}.
Your favorite CPU is {cpu}, and I bet that will change soon.
Regarding GPU, you said {gpu}.""")

prompts()
