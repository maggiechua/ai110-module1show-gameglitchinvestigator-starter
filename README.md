# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

### Game's Purpose
The purpose of this game is to guess the secret number. There are three difficulty levels (easy, medium, hard), where the number of attempts and the range of values the secret number is within are different. After each guess, the game provides hints that tell the user whether their guess is higher or lower than the secret value. The game ends when the secret number is guessed correctly or the user runs out of attempts. 

### Bugs Found
- **Feedback hints reversed**: When submitted guess was greater than the secret number, the game returned "Too Low" and vice versa when the guess was lower
- **User cannot start a new game**: When a user decides to click on the 'New Game' button, it does not change the state
- **Difficulty level and secret number discrepancy**: When a new difficulty level is selected, the current secret number is not updated, so that it falls within the specified range
- **Discrepancy between promised and usable attempts**: User is promised n attempts based on the difficulty level, but they are only able to submit n-1 attempts before the game ends  

### Fixes Applied
- **Feedback hints updated**: feedback messages were swapped to the correct output
- **Updated state management**: set session state status value to "playing" to enable remaining logic to work as expected
- **New Game Resets Values**: attempts, score, and history is reset
- **Secret number updated when difficulty level changes**: when the Session State notices that the difficulty level variable does not match the current state difficulty, it updates the secret number according to the specified range
- **Additional field error handling**: If a user enters a value outside the specified range for a difficulty level, the game returns an error message and does not count the submission as an attempt. 
- **Promised and Usable Attempts are the same**: attempt variable is set to 0 at start and increments up when a valid guess is submitted
- **Refactored code by moving functions to logic_utils.py** 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User chooses difficulty level (easy, medium, hard)
2. User enters a guess
3. Game returns "Go LOWER!" if the guess is greater than the secret number. Otherwise, it returns "Go HIGHER!"
4. Score and remaining attempts updates correctly after each valid guess
5. Game ends after the correct guess

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
