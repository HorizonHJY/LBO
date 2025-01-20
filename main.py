import yfinance as yf
import pandas as pd

# 获取 Walgreens 财务数据
wba = yf.Ticker("WBA")

# 获取财务报表
income_statement = wba.financials
balance_sheet = wba.balance_sheet
cash_flow = wba.cashflow

# 创建 Excel 文件并存储数据
file_path = "Walgreens_Financials.xlsx"

with pd.ExcelWriter(file_path) as writer:
    income_statement.to_excel(writer, sheet_name="Income Statement")
    balance_sheet.to_excel(writer, sheet_name="Balance Sheet")
    cash_flow.to_excel(writer, sheet_name="Cash Flow Statement")

print(f"Excel 文件已保存: {file_path}")
