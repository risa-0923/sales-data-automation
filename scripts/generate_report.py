
import pandas as pd
import os

#プロジェクトのルートディレクトリを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#クリーンデータのパス
clean_data_path = os.path.join(BASE_DIR, "data", "clean_data.csv")
report_path = os.path.join(BASE_DIR, "data", "selase_report.csv")

#データの読み込み
df = pd.read_csv(clean_data_path)

#データの集計処理
total_sales = df["Amount"].sum() #売上合計
sales_by_payment = df.groupby("PaymentMethod")["Amount"].sum() #支払いごとの売上
sales_by_customer = df.groupby("CustomerID")["Amount"].sum() #顧客ごとの売上

#レポートをDataFrameにまとめる
report_df = pd.DataFrame ({
    "Total Sales": [total_sales],
    "CreditCard Sales": [sales_by_payment.get("CreditCard", 0)],
    "Cash Sales": [sales_by_payment.get("Cash", 0)],
    "DebitCard Sales": [sales_by_payment.get("DebitCard", 0)]
})

#レポートをCSVに保存
report_df.to_csv(report_path, index=False)

print(f"売上レポートを {report_path} に保存しました！")