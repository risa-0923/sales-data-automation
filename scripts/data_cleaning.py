
import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv('data/raw_data.csv') # csvファイルの読み込み
    df['Date'] = pd.to_datetime(df['Date']) # 日付をdatetime形式に変換
    df = df.dropna(subset=['Amount']) # 欠損値を除去
    df = df.drop_duplicates() # 重複を削除
    df.to_csv(output_file, index=False) # クリーンデータの保存
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == '__main__':
    clean_data('data/raw_data.csv', 'data/clean_data.csv')