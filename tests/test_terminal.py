from unittest.mock import patch
from terminal_app import main

def test_terminal_exit():
    with patch("builtins.input", side_effect=["exit"]):
        main()  # Should exit cleanly
