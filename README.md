# 売上データ自動処理プロジェクト
SAS/SQLのデータ処理をPythonで自動化


## プロジェクトの目的
SAS/SQL で行っていたデータ処理・レポート生成を Python で自動化し、  
業務効率を向上させることを目的としています。


## 使用技術・ツール
- Python（pandas）
- Git / GitHub
- VS Code
- MacBook環境


## 機能概要
- 生データの前処理(欠損値処理・列名変更など)
- 支払い方法ごとの売上金額を自動で集計
- 集計結果をCSVファイルとして出力


## 実行方法
以下の順に実行します。(Python環境が必要です)：

```bash
python scripts/data_cleaning.py
python scripts/generate_report.py
```

## 今後の展望-あれば

- 集計結果をグラフ化（matplotlibやseaborn）して、視覚的に理解しやすくする
- Flaskを使って、ブラウザから操作できる簡単なWebアプリ化に挑戦したい

