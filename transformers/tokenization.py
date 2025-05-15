import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

print("Vocab Size:", encoder.n_vocab)

text = "The cat sat on the mat"

tokens = encoder.encode(text)
print("generated tokens:", tokens)

decoded = encoder.decode(tokens)
print("decoded tokens:", decoded)