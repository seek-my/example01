import math

class Calculator:
    """计算器类"""

    def __init__(self):
        self.history = []  # 历史记录
        self.last_result = 0  # 上次结果

    def add(self, a, b):
        """加法"""
        return a + b

    def subtract(self, a, b):
        """减法"""
        return a - b

    def multiply(self, a, b):
        """乘法"""
        return a * b

    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为0！")
        return a / b

    def power(self, a, b):
        """幂运算"""
        return a ** b

    def square_root(self, a):
        """平方根"""
        if a < 0:
            raise ValueError("不能对负数开平方根！")
        return math.sqrt(a)

    def calculate(self, operator, a, b=None):
        """执行计算"""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '**': self.power,
            'sqrt': self.square_root
        }

        try:
            if operator == 'sqrt':
                result = operations[operator](a)
            else:
                result = operations[operator](a, b)

            # 保存到历史记录
            if b is None:
                expression = f"{operator}({a})"
            else:
                expression = f"{a} {operator} {b}"

            self.history.append(f"{expression} = {result}")
            self.last_result = result
            return result

        except KeyError:
            raise ValueError(f"不支持的运算符: {operator}")

    def show_history(self):
        """显示历史记录"""
        if not self.history:
            print("暂无历史记录")
        else:
            print("\n=== 计算历史 ===")
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")

    def clear_history(self):
        """清空历史"""
        self.history = []
        print("历史记录已清空")

def main():
    """主程序"""
    calc = Calculator()

    print("=" * 50)
    print("简单计算器")
    print("=" * 50)
    print("支持运算: +, -, *, /, ** (幂), sqrt (平方根)")
    print("命令: history (历史), clear (清空), quit (退出)")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n请输入表达式 (如: 5 + 3) 或命令: ").strip()

            # 处理命令
            if user_input.lower() == 'quit':
                print("再见！")
                break
            elif user_input.lower() == 'history':
                calc.show_history()
                continue
            elif user_input.lower() == 'clear':
                calc.clear_history()
                continue

            # 解析表达式
            if 'sqrt' in user_input:
                # 处理平方根
                num = float(user_input.replace('sqrt', '').strip())
                result = calc.calculate('sqrt', num)
            else:
                # 处理二元运算
                parts = user_input.split()
                if len(parts) != 3:
                    print("格式错误！请使用格式: 数字 运算符 数字")
                    continue

                a = float(parts[0])
                operator = parts[1]
                b = float(parts[2])
                result = calc.calculate(operator, a, b)

            print(f"结果: {result}")

        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"未知错误: {e}")

if __name__ == "__main__":
    main()
