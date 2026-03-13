# stock101

这是一个基于 `yfinance` 的简易股票查询网站。
演示一下 用github Copilot 功能vibe coding 完成。

## 快速开始

1. 安装依赖

```bash
python -m pip install -r requirements.txt
```

2. 启动服务

```bash
python app.py
```

3. 打开浏览器访问：

- http://localhost:5000/

## 使用说明

- 在输入框填写股票代码，例如：`AAPL`、`000001.SZ`（深市）、`600000.SS`（沪市）。
- 点击查询后将展示最新的行情信息。

---

如果你希望使用更完整的行情、历史数据或图表，可以参考 `yfinance` 文档： https://pypi.org/project/yfinance/
