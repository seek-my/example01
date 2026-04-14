import random

class LotteryGenerator:
    """彩票号码生成器"""

    def generate_double_ball(self):
        """双色球：6个红球(1-33) + 1个蓝球(1-16)"""
        red_balls = sorted(random.sample(range(1, 34), 6))
        blue_ball = random.randint(1, 16)
        return {
            'red': red_balls,
            'blue': blue_ball,
            'display': f"红球: {red_balls} | 蓝球: {blue_ball}"
        }

    def generate_super_lotto(self):
        """大乐透：5个前区(1-35) + 2个后区(1-12)"""
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        return {
            'front': front,
            'back': back,
            'display': f"前区: {front} | 后区: {back}"
        }

    def generate_3d(self):
        """福彩3D：3个数字(0-9)"""
        numbers = [random.randint(0, 9) for _ in range(3)]
        return ''.join(map(str, numbers))

    def batch_generate(self, lottery_type, count=5):
        """批量生成"""
        methods = {
            'double_ball': self.generate_double_ball,
            'super_lotto': self.generate_super_lotto,
            '3d': self.generate_3d
        }

        print(f"\n=== 生成 {count} 注 ===")
        for i in range(count):
            result = methods[lottery_type]()
            if isinstance(result, dict):
                print(f"{i+1}. {result['display']}")
            else:
                print(f"{i+1}. {result}")

# 使用
gen = LotteryGenerator()
gen.batch_generate('double_ball', 5)
