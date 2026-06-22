from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_string_secret_compared_numerically():
    # Regression test for the high/low glitch: when the secret arrives as a
    # string (as app.py passes it on even attempts), the comparison must still
    # be numeric. As strings, "9" > "10" is True, which used to flip the hint.
    # guess 9 vs secret "10" must report "Too Low", not "Too High".
    outcome, _message = check_guess(9, "10")
    assert outcome == "Too Low"

    # And the reverse: guess 10 vs secret "9" must report "Too High".
    outcome, _message = check_guess(10, "9")
    assert outcome == "Too High"
