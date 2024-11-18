class Sponsor:
    def __init__(self, name, price, benefits, moneyMultiply, fans, merchAbility):
        self.name = name
        self.price = price
        self.benefits = benefits
        self.moneyMultiply = moneyMultiply
        self.fans = fans
        self.merchAbility = merchAbility

    def __str__(self):
        merchtText = "Можливість створення мерчу" if self.merchAbility     else "Без можливості створення мерчу"
        return f"{self.name}. Ціна: {self.price}$: {', '.join(self.benefits)}. Множник виграшу: x{self.moneyMultiply}, Фанати: +{self.fans}. {merchtText}"

    def GETmerchAbility(self):
        return self.merchAbility

# список спонсорів
sponsors = [
    Sponsor("Tech Corp", 5000, ["Виграш в турнірі x1.1", "Без можливості створення мерчу"], 1.1, 0, False),
    Sponsor("GameX", 8000, ["Виграш в турнірі x1.5", "Можливість створення мерчу"], 1.5, 100, True),
    Sponsor("MegaGaming", 12000, ["Виграш в турнірі x3", "Підвищення популярності","Можливість створення мерчу" ], 2, 500, True),
]

