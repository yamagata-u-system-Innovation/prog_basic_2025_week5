import importlib
import pytest
from types import SimpleNamespace
import sys
import os

# ★ リポジトリのルートを import path に確実に入れる
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

PREFERRED_MODULES = ["assignment3_number_game", "number_game"]


def _import_student_module():
    last_exc = None
    for name in PREFERRED_MODULES:
        try:
            return importlib.import_module(name)
        except Exception as e:
            last_exc = e
    raise RuntimeError(
        f"Could not import any student module: {PREFERRED_MODULES}"
    ) from last_exc


def _run_with_inputs(capsys, monkeypatch, inputs, target):
    """inputs による入力を順に返す input を用意し、module.main() を呼び出す"""

    # テスト対象モジュールの import
    module = _import_student_module()

    # ★ module.random を差し替えて target を返すようにする
    fake_random = SimpleNamespace(randint=lambda a, b: target)
    monkeypatch.setattr(module, "random", fake_random)

    # 入力列 input を準備
    input_iter = iter(inputs)

    def fake_input(_prompt=""):
        try:
            return next(input_iter)
        except StopIteration:
            return ""  # 念のため空を返す

    # ★ 組み込みの input 関数を差し替える
    monkeypatch.setattr("builtins.input", fake_input)

    # ★ main() だけを呼ぶ（play() は使わない）
    if hasattr(module, "main"):
        module.main()
    else:
        raise RuntimeError("main() 関数が存在しません。")

    out = capsys.readouterr().out
    return out


# ここから各テスト ------------------------------------------


def test_correct_in_one_try(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["50"], target=50)
    assert "正解" in out, (
        "Expected a win message containing '正解' when guessing the target in one try."
    )


def test_hint_smaller_then_correct(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["20", "50"], target=50)
    assert "もっと大きい" in out, (
        "Expected hint 'もっと大きいです。' when the guess is smaller than target."
    )
    assert "正解" in out, "Expected a win message after the correct second guess."


def test_hint_bigger_then_correct(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["80", "50"], target=50)
    assert "もっと小さい" in out, (
        "Expected hint 'もっと小さいです。' when the guess is larger than target."
    )
    assert "正解" in out, "Expected a win message after the correct second guess."


def test_max_tries_limit_and_lose_message(capsys, monkeypatch):
    wrongs = ["1"] * 7
    out = _run_with_inputs(capsys, monkeypatch, inputs=wrongs, target=50)
    assert "残念" in out, (
        "Expected a lose message containing '残念' after 7 wrong attempts."
    )
    assert "50" in out, "Expected the lose message to include the correct answer."


def test_non_integer_reprompt(capsys, monkeypatch):
    out = _run_with_inputs(capsys, monkeypatch, inputs=["abc", "50"], target=50)
    assert "正解" in out, (
        "Program should continue after non-integer input and eventually accept a valid guess."
    )
    assert ("整数を入力してください" in out) or ("整数" in out), (
        "Expected a guidance message prompting for an integer input."
    )
