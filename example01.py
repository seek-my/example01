# Step 1: 导入random模块
import random

# Step 2: 实现游戏核心逻辑
def guess_number_game():
    """猜数字游戏主函数"""
    # 生成1-100之间的随机数
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # 最多猜10次

    print("=" * 50)
    print("欢迎来到猜数字游戏！")
    print(f"我已经想好了一个1到100之间的数字，你有{max_attempts}次机会猜测。")
    print("=" * 50)

    # Step 3: 游戏循环
    while attempts < max_attempts:
        try:
            # 获取用户输入
            guess = int(input(f"\n第{attempts + 1}次猜测，请输入你的数字: "))
            attempts += 1

            # Step 4: 判断猜测结果
            if guess < secret_number:
                print(f"❌ 太小了！还剩{max_attempts - attempts}次机会")
            elif guess > secret_number:
                print(f"❌ 太大了！还剩{max_attempts - attempts}次机会")
            else:
                print(f"\n🎉 恭喜你！猜对了！")
                print(f"答案是 {secret_number}，你用了 {attempts} 次猜中！")
                return True

        except ValueError:
            print("⚠️  请输入有效的数字！")
            attempts -= 1  # 无效输入不计次数

    # 超过最大次数
    print(f"\n😢 游戏结束！你已用完所有机会。")
    print(f"正确答案是: {secret_number}")
    return False

# Step 5: 实现重复游戏功能
def main():
    """主程序"""
    while True:
        guess_number_game()

        # 询问是否继续
        play_again = input("\n是否继续游戏？(y/n): ").lower()
        if play_again != 'y':
            print("\n感谢游玩！再见！")
            break

# 程序入口
if __name__ == "__main__":
    main()
