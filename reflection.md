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
| clicking on show hint checkbox when it is currently unchecked | displays a hint modal | no modal appears | none |
| pressing enter to submit guess | submits guess and user receives timely feedback | no feedback | None |
| guess of 2 | displays hint telling user to 'go higher' | displays hint telling user to 'go lower' when secret number is 7 | None |
| guess of 9 | displays hint telling user to 'go lower' | displays hint telling user to 'go higher' when secret number is 7 | None |
| clicking on new game button | removes the modal telling the user they won the game and need to start a new game | does not remove the modal | None |
| submitting a guess for a new game | allows a user to submit a guess and provides feedback | page refreshes, but no feedback is provided | None |
| user selects a different difficulty level | if the secret number is outside the defined range, its value is reassigned to one within the range | the secret number remains unchanged even if its outside the defined range | None |
| user submits the n-1 guess attempt  | user can use up to the pre-defined number of attempts based on difficulty level | attempts made vs. attempts remaining are not the same and ends the game early for the user | None 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
