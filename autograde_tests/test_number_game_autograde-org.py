# test_number_game_autograde.py
# Autograde tests for Number Guessing Game
# Requirements:
# - Random target in [1,100]
# - Up to 7 attempts
# - Hints: "もっと大きいです。"/"もっと小さいです。"
# - Win message includes "正解！"
# - Lose message includes the correct answer (e.g., "残念！正解は 50 でした。")
# - Non-integer input should prompt re-entry and show a guidance message (expected substring: "整数を入力してください")

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import importlib
import builtins
from types import SimpleNamespace
from typing import List
import pytest

PREFERRED_MODULES = ["assignment3_number_game", "number_game"]

def _import_student_module():
    last_exc = None
    for name in PREFERRED_MODULES:
        try:
            return importlib.import_module(name)
        except Exception as e:
            last_exc = e
    raise RuntimeError(f"Could not import any student module: {PREFERRED_MODULES}") from last_exc


def _run_with_inputs(capsys, monkeypatch, inputs: List[str], target: int = 50) -> str:
    """Run the student program with patched input/print/random, capture stdout text.

    Supports two styles:
    - Function-based: module.play() exists
    - Script-based: top-level script executes on import; we reload under patches
    """
    # Prepare fake input iterator
    it = iter(inputs)

    def fake_input(prompt=""):
        # input(prompt) normally prints the prompt; emulate to capture into stdout
        if prompt:
            print(prompt, end="")
        try:
            return next(it)
        except StopIteration:
            # If inputs run out, keep returning a safe guess
            return str(target)

    # Patch random.randint to deterministic target
    fake_random = SimpleNamespace(randint=lambda a, b: target)

    # Patch builtins.input
    monkeypatch.setattr(builtins, "input", fake_input)

    # Import student module and swap its random
    module = _import_student_module()
    setattr(module, "random", fake_random)

    # Execute
    if hasattr(module, "play") and callable(getattr(module, "play")):
        try:
            module.play()
        except TypeError:
            try:
                module.play(randint_func=fake_random.randint, input_func=fake_input, print_func=print)
            except TypeError:
                importlib.reload(module)
    else:
        importlib.reload(module)

    captured = capsys.readouterr().out
    return captured


def test_correct_in_one_try(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["50"], target=50)
    assert "正解" in out, "Expected a win message containing '正解' when guessing the target in one try."


def test_hint_smaller_then_correct(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["20", "50"], target=50)
    assert "もっと大きい" in out, "Expected hint 'もっと大きいです。' when the guess is smaller than target."
    assert "正解" in out, "Expected a win message after the correct second guess."


def test_hint_bigger_then_correct(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["80", "50"], target=50)
    assert "もっと小さい" in out, "Expected hint 'もっと小さいです。' when the guess is larger than target."
    assert "正解" in out, "Expected a win message after the correct second guess."


def test_max_tries_limit_and_lose_message(capsys, monkeypatch):
    wrongs = ["1"] * 7
    out = _run_with_inputs(capsys, monkeypatch, inputs=wrongs, target=50)
    assert "残念" in out, "Expected a lose message containing '残念' after 7 wrong attempts."
    assert "50" in out, "Expected the lose message to include the correct answer."


def test_non_integer_reprompt(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["abc", "50"], target=50)
    assert "正解" in out, "Program should continue after non-integer input and eventually accept a valid guess."
    assert ("整数を入力してください" in out) or ("整数" in out), "Expected a guidance message prompting for an integer input."
