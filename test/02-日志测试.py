# test/02-日志测试.py

from app.core.logger import logger

# --- 1. TRACE (最详细) ---
# 场景：极其详细的内部流程追踪，通常用于调试复杂的算法或状态机
# 颜色：通常是深青色/蓝色 (取决于终端主题)
logger.trace("进入函数 calculate_complex_logic，参数 x=10, y=20")
logger.trace("中间变量 state={'step': 1, 'val': 30}")

# --- 2. DEBUG (调试) ---
# 场景：开发阶段的调试信息，变量值，函数入口出口
# 颜色：蓝色
logger.debug("数据库连接池当前大小：5")
logger.debug("正在尝试重试第 2 次请求...")

# --- 3. INFO (信息) ---
# 场景：正常的业务流程关键节点，用户操作，系统启动/停止
# 颜色：白色/绿色 (通常较亮)
logger.info("用户 ID: 1001 登录成功")
logger.info("订单 #9527 已创建，金额：¥299.00")
logger.info("系统健康检查通过")

# --- 4. SUCCESS (成功 - Loguru 特有) ---
# 场景：明确标记某个耗时操作或关键任务圆满完成
# 颜色：绿色 (带勾选标记 ✅)
logger.success("数据备份完成！文件已保存至 /backup/2026-03-15.zip")
logger.success("模型训练结束，准确率达到 98.5%")

# --- 5. WARNING (警告) ---
# 场景：非致命错误，使用了废弃 API，配置项缺失使用默认值，重试前的提示
# 颜色：黄色/橙色
logger.warning("配置文件缺少 'TIMEOUT' 字段，使用默认值 30s")
logger.warning("检测到 API 响应时间超过 2s，性能可能下降")
logger.warning("用户密码强度较弱，建议修改")

# --- 6. ERROR (错误) ---
# 场景：操作失败，但程序仍可继续运行（如单个请求失败，文件写入失败）
# 颜色：红色
logger.error("无法连接到 Redis 服务器：Connection refused")
logger.error("用户 ID: 1002 的数据解析失败，跳过该记录")

# --- 7. CRITICAL (严重) ---
# 场景：致命错误，程序无法继续运行，即将崩溃或退出
# 颜色：深红色/背景红色
logger.critical("磁盘空间已满！无法写入任何新数据，系统即将停止服务")
logger.critical("核心加密密钥丢失，安全模块初始化失败")

# --- 演示异常捕获 (自动记录为 ERROR 级别) ---
@logger.catch
def divide(a, b):
    return a / b

# try:
#     divide(10, 0)
# except ZeroDivisionError:
#     # 手动记录异常堆栈
#     logger.exception("发生除零错误，计算终止")
    # 等同于: logger.opt(exception=True).error("发生除零错误，计算终止")


divide(10, 0)
