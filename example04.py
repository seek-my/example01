class UnitConverter:
    """单位转换器"""

    # 长度转换（基准单位：米）
    LENGTH_UNITS = {
        '米': 1,
        '千米': 1000,
        '厘米': 0.01,
        '英尺': 0.3048,
        '英里': 1609.34
    }

    # 重量转换（基准单位：千克）
    WEIGHT_UNITS = {
        '千克': 1,
        '克': 0.001,
        '磅': 0.453592,
        '吨': 1000
    }

    def convert_length(self, value, from_unit, to_unit):
        """长度转换"""
        meters = value * self.LENGTH_UNITS[from_unit]
        result = meters / self.LENGTH_UNITS[to_unit]
        return result

    def convert_weight(self, value, from_unit, to_unit):
        """重量转换"""
        kg = value * self.WEIGHT_UNITS[from_unit]
        result = kg / self.WEIGHT_UNITS[to_unit]
        return result

    def celsius_to_fahrenheit(self, celsius):
        """摄氏度转华氏度"""
        return celsius * 9/5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """华氏度转摄氏度"""
        return (fahrenheit - 32) * 5/9

# 使用
converter = UnitConverter()
print(f"100厘米 = {converter.convert_length(100, '厘米', '米')}米")
print(f"1千克 = {converter.convert_weight(1, '千克', '磅')}磅")
