# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
name_prompt = "What is your name? "
prompt = "\nIf you could visit one place in the world, where would you go? "
prompt += "\ntype 'quit' to exit the poll: "
poll_results = {}
polling = True

while polling:
    name = input(name_prompt)
    poll = input(prompt)
    if poll == 'quit':
        polling = False
    else:
        poll_results[name] = poll

print("\n--- Poll Results ---")
for name, poll in poll_results.items():
    print(name + ": " + poll)
