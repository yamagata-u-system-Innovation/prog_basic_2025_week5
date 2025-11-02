# Week5 Autograde Starter (Number Guessing Game)

## 使い方（学生）

1. このリポジトリを Clone  
2. `assignment3_number_game.py` を編集（TODO を埋める）  
3. 保存して Commit → Push  
4. 数十秒後、GitHub の Actions（Auto-grading）が実行され、テスト結果が反映されます  

---

### テストファイルについて

- `test/` フォルダ：授業中に使う確認用スクリプトです（学生が編集可）  
- `autograde_tests/` フォルダ：自動採点（pytest）用です。内容を変更する必要はありません。  

---

## 採点（可視テスト）

- 採点対象：`autograde_tests/test_number_game_autograde.py`
- 判定条件：
  - 1〜100 の乱数を生成
  - 最大 7 回まで挑戦可
  - 「もっと大きい」「もっと小さい」のヒントを表示
  - 「正解！」および「残念！正解は X でした。」のメッセージ
  - 整数以外を入力した場合、再入力を促すメッセージ（例：「整数を入力してください」）

---

## ローカル確認

```bash
pip install -r requirements.txt
pytest -q autograde_tests
```

---

## 注意

- テストをパスするため、出力メッセージに **以下のキーワードを含めてください：**  
  「正解」「もっと大きい」「もっと小さい」「残念」「整数」など  
- メッセージ末尾の句読点や全角／半角は厳密に一致しなくても合格します（ゆるいマッチングです）

---

## 課題#3（数当てゲーム）と自動採点について

- **編集するファイル**：`assignment3_number_game.py`  
- **要件**：
  - 1〜100 の乱数を生成
  - 最大 7 回まで挑戦
  - 「もっと大きい」「もっと小さい」のヒント表示
  - 「正解！」で終了、失敗時は正答を表示
  - 整数以外は再入力を促す  
- **自動採点テスト**：`autograde_tests/test_number_game_autograde.py`（pytest）

---

### 重要: solution ファイルの扱い

- 以前公開していた `number_game.py` は **模範解答（`solutions/number_game_solution.py`）** に移動しました。  
- `solutions/` は `.gitignore` により **Push対象外** です。  
- 課題は **`assignment3_number_game.py`** を編集して提出してください。

---

### ローカル実行・テスト

```bash
python assignment3_number_game.py
pip install -r requirements.txt
pytest -q autograde_tests
```

---

### Classroom の自動採点（参考）

**Setup command**
```bash
python -m pip install -r requirements.txt
```

**Test command**
```bash
pytest -q autograde_tests
```
