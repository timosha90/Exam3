# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

class IceCream:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def info_about_icecream(self):
        if self.ingredient:
            print(f'Мороженное и {self.ingredient}')
        else:
            print('Обычное мороженое')

ice1 = IceCream(1)
ice2 = IceCream('лимон')
print(ice2.info_about_icecream())
