# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 50 |"Too Low" |"Too High" |"none" | 
|Guess of 75 |"Too High |"Too Low" |"none"  |
|New Game Clicked, after winning|A new game begins |A new game does not begin |"You already won. Start a new game to play again." |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code was the only AI used

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
A suggestion that the AI gave which was correct, was swapping the logic behind check_guess and ensuring the correct output was given to the user based on their guess.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Originally, the AI suggested merely swapping the two outputs with each other. However, this still resulted in a misleading output for the user so I had to tell the Ai to rewrite the tex contained within the string. The result was verified within running the program on localhost.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I ran pytest alongside running the program from streamlit, to make sure the user was getting the correct output.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I ran pytest and did it manually within streamlit. It helped me to identify where certain functions were located within my code, and how they interacted with each other.

- Did AI help you design or understand any tests? How?

Yes, Ai helped me design my test. I gave it a list of requirements, and the AI was fed this list to create tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
