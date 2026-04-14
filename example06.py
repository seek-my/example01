from datetime import datetime, timedelta

class Countdown:
    """倒计时程序"""

    def __init__(self):
        self.events = {}

    def add_event(self, name, target_date):
        """添加事件"""
        self.events[name] = target_date
        print(f"已添加事件: {name} - {target_date}")

    def calculate_days(self, target_date):
        """计算剩余天数"""
        now = datetime.now()
        target = datetime.strptime(target_date, '%Y-%m-%d')
        delta = target - now
        return delta.days

    def show_all_events(self):
        """显示所有事件"""
        if not self.events:
            print("暂无事件")
            return

        print("\n=== 倒计时事件 ===")
        for name, date in sorted(self.events.items(), key=lambda x: x[1]):
            days = self.calculate_days(date)
            if days > 0:
                print(f"{name}: 还有 {days} 天 ({date})")
            elif days == 0:
                print(f"{name}: 就是今天！({date})")
            else:
                print(f"{name}: 已过去 {abs(days)} 天 ({date})")

    def timer(self, seconds):
        """简单计时器"""
        import time

        print(f"倒计时 {seconds} 秒开始...")
        for i in range(seconds, 0, -1):
            print(f"\r剩余: {i} 秒", end='')
            time.sleep(1)
        print("\n时间到！")

# 使用
countdown = Countdown()
countdown.add_event("春节", "2025-01-29")
countdown.add_event("生日", "2025-06-15")
countdown.show_all_events()
