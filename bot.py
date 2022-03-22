import openai

openai.api_key = "API-KEY"

conversation = "Human: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?"
print(conversation)

i = 1
while (i != 0):
    question = input("Human: ")
    conversation += "\nHuman:" + question + "\nAI:"
    response = openai.Completion.create(
        engine = "davinci",
        prompt = conversation,
        temperature = 0.9,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = ["\n", " Human:", " AI:"]
    )
    answer = response.choices[0].text.strip()
    conversation += answer
    print("AI: " + answer)
