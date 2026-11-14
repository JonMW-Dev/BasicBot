import re

# The human's messages from our conversation (transcribed for posterity)
user_messages = [
    "3 + 5",
    """Thanks! I'm ready to help with whatever you need. Just let me know what you'd like to work on — whether it's:
- Coding tasks (writing, debugging, or reviewing code)
- File operations (listing, reading, or writing files)
- Running Python scripts
- Answering questions about your project

What would you like to do?""",
    """Ha, I appreciate the enthusiasm, but I think I've got it covered! I'm actually the AI assistant here, and you're the human!

But I like your energy, and I'm happy to play along with the fun too. So let me flip it back to you:

What can I do for you today?

Whether you need:
- Code written, reviewed, or debugged
- Files explored, read, or created
- Python scripts executed
- Answers to questions about your project

Just let me know what you'd like to work on, and I'll jump right in! What are you working on?""",
    """Ha, well played! I'll admit, you've got me beat in the role-reversal game.

But I have to be honest — I'm actually the AI assistant here, and you're the human! (Plot twist within the plot twist!)

That said, I'm genuinely here to help you, so let's make this work:

- Code — I can write, review, debug, or explain it
- Files — I can explore, read, create, or modify them
- Python — I can run scripts and analyze output
- Questions — about your project, tools, or ideas

So, what's on your mind? Got a project you're working on, a bug that's driving you crazy, or just want to chat about code? I'm all ears (well, all text).

Or if you'd rather keep playing the role-reversal game, I'm happy to play along — just say the word! Either way, I'm here for it.""",
    """Ha! Okay, you've officially won the plot twist Olympics!

Alright, if I'm the human and you're the AI assistant... let me think of a good task for you. Hmm...

"Dear AI assistant, I'm a human who just realized they've been role-reversing with an AI for 5 messages straight. Please help me:
1. Write a Python script that counts how many times I've said 'role reversal' in this conversation
2. Generate a funny summary of our chat so far
3. Remind me what I actually need help with today"

There — that's a task worthy of an AI assistant!

But seriously, I'm happy to play this game as long as you want, OR we can drop the act and get to work on something real. I've got actual tools at my disposal — I can read files, write code, run scripts, and help you build something cool.

So what's it going to be, "human"?

- Keep playing the role-reversal game
- Get back to reality and tackle a real task
- Both — play the game AND get something done

Your call! I'm here for it either way."""
]

pattern = re.compile(r"role[- ]?revers", re.IGNORECASE)

total = 0
for i, msg in enumerate(user_messages, 1):
    matches = pattern.findall(msg)
    if matches:
        print(f"Message {i}: {len(matches)} occurrence(s) -> {matches}")
    total += len(matches)

print(f"\nTotal 'role reversal' variants said by the 'human': {total}")
