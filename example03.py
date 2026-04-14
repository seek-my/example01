import json
import os

class Student:
    """学生类"""

    def __init__(self, student_id, name, scores):
        """
        初始化学生对象
        :param student_id: 学号
        :param name: 姓名
        :param scores: 成绩字典 {'语文': 90, '数学': 85, ...}
        """
        self.student_id = student_id
        self.name = name
        self.scores = scores

    def get_average(self):
        """计算平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def to_dict(self):
        """转换为字典"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'scores': self.scores
        }

    def __str__(self):
        """字符串表示"""
        avg = self.get_average()
        scores_str = ', '.join([f"{subject}: {score}" for subject, score in self.scores.items()])
        return f"学号: {self.student_id} | 姓名: {self.name} | 成绩: [{scores_str}] | 平均分: {avg:.2f}"

class StudentManager:
    """学生管理系统"""

    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = {}  # {student_id: Student对象}
        self.load_data()

    def add_student(self, student):
        """添加学生"""
        if student.student_id in self.students:
            print(f"学号 {student.student_id} 已存在！")
            return False

        self.students[student.student_id] = student
        print(f"成功添加学生: {student.name}")
        self.save_data()
        return True

    def delete_student(self, student_id):
        """删除学生"""
        if student_id not in self.students:
            print(f"学号 {student_id} 不存在！")
            return False

        student = self.students.pop(student_id)
        print(f"已删除学生: {student.name}")
        self.save_data()
        return True

    def update_score(self, student_id, subject, score):
        """更新成绩"""
        if student_id not in self.students:
            print(f"学号 {student_id} 不存在！")
            return False

        self.students[student_id].scores[subject] = score
        print(f"已更新 {self.students[student_id].name} 的 {subject} 成绩为 {score}")
        self.save_data()
        return True

    def find_student(self, student_id):
        """查找学生"""
        return self.students.get(student_id)

    def list_all_students(self):
        """列出所有学生"""
        if not self.students:
            print("暂无学生数据")
            return

        print("\n" + "=" * 80)
        print("所有学生信息")
        print("=" * 80)
        for student in self.students.values():
            print(student)
        print("=" * 80)

    def get_statistics(self):
        """统计信息"""
        if not self.students:
            print("暂无数据")
            return

        all_averages = [s.get_average() for s in self.students.values()]

        print("\n=== 统计信息 ===")
        print(f"学生总数: {len(self.students)}")
        print(f"班级平均分: {sum(all_averages) / len(all_averages):.2f}")
        print(f"最高平均分: {max(all_averages):.2f}")
        print(f"最低平均分: {min(all_averages):.2f}")

    def save_data(self):
        """保存到文件"""
        data = {sid: student.to_dict() for sid, student in self.students.items()}
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        """从文件加载"""
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for sid, student_data in data.items():
                    student = Student(
                        student_data['student_id'],
                        student_data['name'],
                        student_data['scores']
                    )
                    self.students[sid] = student
            print(f"已加载 {len(self.students)} 条学生数据")
        except Exception as e:
            print(f"加载数据失败: {e}")

def main():
    """主程序"""
    manager = StudentManager()

    menu = """
    ========== 学生成绩管理系统 ==========
    1. 添加学生
    2. 删除学生
    3. 修改成绩
    4. 查询学生
    5. 显示所有学生
    6. 统计信息
    0. 退出系统
    =====================================
    """

    while True:
        print(menu)
        choice = input("请选择操作 (0-6): ").strip()

        if choice == '1':
            student_id = input("请输入学号: ").strip()
            name = input("请输入姓名: ").strip()
            scores = {}
            subjects = ['语文', '数学', '英语']
            for subject in subjects:
                score = float(input(f"请输入{subject}成绩: "))
                scores[subject] = score

            student = Student(student_id, name, scores)
            manager.add_student(student)

        elif choice == '2':
            student_id = input("请输入要删除的学号: ").strip()
            manager.delete_student(student_id)

        elif choice == '3':
            student_id = input("请输入学号: ").strip()
            subject = input("请输入科目: ").strip()
            score = float(input("请输入新成绩: "))
            manager.update_score(student_id, subject, score)

        elif choice == '4':
            student_id = input("请输入学号: ").strip()
            student = manager.find_student(student_id)
            if student:
                print(f"\n{student}")
            else:
                print("未找到该学生")

        elif choice == '5':
            manager.list_all_students()

        elif choice == '6':
            manager.get_statistics()

        elif choice == '0':
            print("感谢使用！再见！")
            break

        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()
