# test/01-env和系统环境变量的优先级.py

import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv(override=True)

print(os.getenv("OPENAI_API_KEY"))

# 实际默认逻辑：override=False
# - 如果系统环境变量不存在 → 用.env里的值
# - 如果系统环境变量已存在 → 系统变量优先级更高
# 想让.env覆盖系统变量，需显式传 override=True
# load_dotenv(override=True)

# 示例：假设系统有环境变量 MY_KEY=system_val，.env里 MY_KEY=dotenv_val
print(os.getenv("MY_KEY"))
# load_dotenv() → 输出 system_val（系统优先级高）
# load_dotenv(override=True) → 输出 dotenv_val（.env覆盖系统）