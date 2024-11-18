from scr.TeamMember import TeamMember


class Player(TeamMember):
    def __init__(self, name, skills, aim):
        super().__init__(name, "Гравець")
        self.skills = skills
        self.aim = aim  # Базова характеристика aim (точність)

    def calculate_performance(self, morale):
        """Обчислює продуктивність залежно від моралі команди."""
        performance_multiplier = 1 + (morale - 5) * 0.1  # Чим вище мораль, тим більший множник
        return round(self.aim * performance_multiplier, 2)

    def get_details(self):
        return f"{self.role}: {self.name}, Навички: {', '.join(self.skills)}, Aim: {self.aim}"

#Ціна залежть від абілки: якшо до 20 то по 1000 за штуку. Приклад "aim": 5 +500$ / "logic": 90 + 5000$ / "reaction": 16 + 500$ - гравець коштує 6000$  
#до 20 - 500$
#20 - 45- 1500$
#45+ 3000$ за опцію

players = {"nickname": "NiKo", "aim": 5, "logic": 12, "reaction": 16},#бомж
{"nickname": "device", "aim": 94, "logic": 90, "reaction": 91},#імба \\\
{"nickname": "blameF", "aim": 34, "logic": 12, "reaction": 39},#норм \\
{"nickname": "Twistzz", "aim": 87, "logic": 86, "reaction": 88},#імба \\\
{"nickname": "karrigan", "aim": 35, "logic": 43, "reaction": 34},#норм \\
{"nickname": "cadiaN", "aim": 14, "logic": 2, "reaction": 19},#бомж \
{"nickname": "jks", "aim": 83, "logic": 81, "reaction": 83},#імба \\\
{"nickname": "flameZ", "aim": 18, "logic": 8, "reaction": 8},#бомж \
{"nickname": "hunter-", "aim": 12, "logic": 8, "reaction": 9},#бомж \
{"nickname": "stavn", "aim": 19, "logic": 7, "reaction": 7},#бомж \
{"nickname": "magisk", "aim": 35, "logic": 22, "reaction": 43},#норм \\
{"nickname": "rain", "aim": 86, "logic": 40, "reaction": 35},#норм \\
{"nickname": "XANTARES", "aim": 93, "logic": 88, "reaction": 92},#імба \\\
{"nickname": "f0rest", "aim": 91, "logic": 87, "reaction": 90},#імба \\\
{"nickname": "GeT_RiGhT", "aim": 20, "logic": 45, "reaction": 18},#імба \\\
{"nickname": "shroud", "aim": 19, "logic": 44, "reaction": 37},#норм \\
{"nickname": "woxic", "aim": 34, "logic": 29, "reaction": 34},#норм \\
{"nickname": "KennyS", "aim": 9, "logic": 8, "reaction": 2},#бомж \
{"nickname": "s1mple", "aim": 98, "logic": 95, "reaction": 97},#імба \\\