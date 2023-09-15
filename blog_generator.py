import openai

openai.api_key = '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'

def generate_blog(paragraph_topic):
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog

print(generate_blog('Who is the best EDM artist of 2021'))