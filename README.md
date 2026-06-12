# ファイル結合ツール

複数のテキストファイルを1つに結合するシンプルなPythonスクリプトです。

## 使い方

```bash
python file_merger.py file1.txt file2.txt -o output.txt
```

## オプション

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `-o`, `--output` | 出力ファイルのパス（必須） | - |
| `-s`, `--separator` | ファイル間の区切り文字 | `\n---\n` |

## 例

```bash
# 3つのファイルを結合
python file_merger.py a.txt b.txt c.txt -o merged.txt

# カスタム区切り文字を使用
python file_merger.py a.txt b.txt -o merged.txt -s "\n===\n"
```

## 動作環境

- Python 3.6 以上
- 外部ライブラリ不要（標準ライブラリのみ使用）

## ライセンス

MIT
