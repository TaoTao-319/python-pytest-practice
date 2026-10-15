# Python 与 pytest 测试实践

对手机号校验、密码校验和购物车金额计算进行单元测试，覆盖参数化、fixture、边界、异常、舍入和数据隔离。默认测试集 45 个场景。

## 安装与运行

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m pytest -q
python demo.py
```

上述安装和执行命令应在已激活的虚拟环境中运行；Windows 可使用 `.venv\Scripts\python.exe` 替换 `python`，Linux 使用 `.venv/bin/python`。

## 规则

| 模块 | 约定 |
|---|---|
| 手机号 | 以 1 开头的 11 位 ASCII 数字字符串；不校验实际号段 |
| 密码 | 长度 8–20，包含英文字母和 ASCII 数字 |
| 购物车 | 非负有限单价、非负整数数量，拒绝布尔数量；返回两位 Decimal，使用 HALF_EVEN 舍入 |

`src/qa_utils` 保存业务函数，`tests` 保存默认测试。`examples/policies` 保存早期不同规则的独立实现，不混入主规则；其中密码要求大小写、数字、特殊字符并拒绝空格。

完整证据生成：`python scripts/verify_project.py`。输出位于 `artifacts`，包括正常测试、演示程序和隔离的预期失败示例。单独执行 `python -m pytest examples/failure_example.py` 应返回失败，其错误预期为 16.00，实际总价为 16.50。

## 验证记录

45 个默认场景通过，预期失败示例与演示程序验证通过。[执行摘要](docs/verification.json) · [逐场景结果](examples/results/test_cases.csv)
