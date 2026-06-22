# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first glance, the game had a straightforward UI, but when I tried to play the game, several bugs were apparent. I found that the hints were backwards, pressing enter to submit a guess did not work, and that I was unable to start a new game. After encountering those bugs, I decided the second time around, I would test out trying to use up all of my attempts and experimenting with the settings.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The two concrete bugs I noticed at the start was that the hints were backwards. For instance, if the secret number is 55, when I submitted a guess greater than the number, it would display feedback telling me to guess higher and vice versa if the guess was lower than 55. The second bug occurred when a user correctly guesses the secret number and decides to start a new game. While the developer debug info updates to a new secret number, the modal telling the user they have won continues to persist and the user is unable to submit guesses for the new game. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| submitting a guess lower than the secret number/submitting a guess higher than the secret number | displays hint telling user to 'go higher'/displays hint telling user to 'go lower' | displays hint telling user to 'go lower'/displays hint telling user to 'go higher' | None |
| clicking on new game button | removes any feedback modals, new secret number chosen, and user can submit guesses | does not remove the modal, user cannot submit guesses | None |
| user selects a different difficulty level | if the secret number is outside the defined range, its value is reassigned to one within the range | the secret number remains unchanged even if its outside the defined range | None |
| user submits the n-1 guess attempt  | user can use up to the pre-defined number of attempts based on difficulty level | attempts made vs. attempts remaining are not the same and ends the game early for the user | None 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

I used Claude as my collaborative partner on this assignment. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

![alt text](image.png)

I told Claude that the user is unable to start a new game when the current game has ended. It correctly identified that the issue originated from the session state status not being reset to "playing," when the new game logic is run. I verified the result by playing two additional games, the first where I guessed the secret number and one where I was unable to guess it before my attempts ran out. Then I clicked on the 'New Game' button. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

While using Claude to address the new game bug, it correctly identified that the secret number provided did not follow the ranges prescribed by difficulty level. It tried to fix this by adding a line of code that retrieved the range values of the selected difficulty level, generating a secret number that was within the range, and updating the session state secret number value. However, unless the user selects the difficulty level before selecting a new game, the bug will persist as a new secret number is not chosen. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided that a bug was fixed only after checking that that the expected behavior occurred during manual testing and if applicable, through pytest. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

- Did AI help you design or understand any tests? How?

I used Claude to help me design tests. I would write a prompt concisely explaining the bug, the expected behavior, and the tests to check this behavior. Afterwards, I would review the code suggestions within the files, run pytest, and then do a manual check. If there were additional issues, I would go back to the code and walk through the logic. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is a framework that allows you to display interactive applications with minimal code. It handles state management using Session State, which allows you to retain variables across sessions/reruns. Session State can be changed using callbacks, which allow you to access/reassign values. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Whenever I was prompting AI to solve a bug, I made sure to identify what the issue is, where in the code files it was located, and what the fix would entail. It allowed me to receive outputs that were more likely to match what I was looking for, with minor embellishments on my end.  

- What is one thing you would do differently next time you work with AI on a coding task?

I think the next time I work with AI on a coding task, I want to preemptively determine my own answer to a bugfix. While I sometimes had something in mind before I submitted my prompt, I'm afraid of cognitive offloading that obstructs learning. It doesn't necessarily involve coding the entire solution in advance, but to consider the structure of the solution (i.e. what data structure am I using, is the main problem addressing state management, what edge cases do I need to account for). 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

Collaborating with AI on this project has provided me with mixed feelings. In some ways it requires a developer to think more critically about the outputs they're receiving, but the loss of manually solving a bug makes me worried about how to evaluate if one is truly learning. 