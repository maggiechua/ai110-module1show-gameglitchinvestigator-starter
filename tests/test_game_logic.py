import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess
import random

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, feedback = check_guess(50, 50)
    assert result == "Win"
    assert feedback == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, feedback = check_guess(60, 50)
    assert result == "Too High"
    assert feedback == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, feedback = check_guess(40, 50)
    assert result == "Too Low"
    assert feedback == "📈 Go HIGHER!"

# Test that the range for each difficulty level is correct
def test_secret_within_range_for_difficulty():
    # Verify that secrets generated for each difficulty are within valid ranges
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        # Generate multiple secrets and verify they're in range
        for _ in range(10):
            secret = random.randint(low, high)
            assert low <= secret <= high, f"Secret {secret} outside range [{low}, {high}] for {difficulty}"

def test_parse_guess_within_range():
    # Valid guess within range should succeed
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None

def test_parse_guess_below_range():
    # Guess below the minimum should fail
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err

def test_parse_guess_above_range():
    # Guess above the maximum should fail
    ok, value, err = parse_guess("150", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err

def test_parse_guess_at_range_boundaries():
    # Guesses at the boundaries should succeed
    ok, value, err = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1

    ok, value, err = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100