import openai

openai.api_key = "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"
f = 'file-LXusegCxGmDfrqOfON1XB3qw'
response = openai.Classification.create(
    file=f,
    query="My baby is a dog",
    search_model="ada",
    model="curie",
    max_examples=3
)
print(response)