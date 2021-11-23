#У вас есть список блюд, которые заказал пользователь, 
# распределите их по категориям и выведите на страничке заказа. 
# Чтобы вы смогли это сделать, в словаре cats указано, что куда относится.

from flask import Flask, render_template, request
app = Flask(__name__)

order = ["Суп с лосем", "Чизбургер",  "Тирамису"]

cats = {
  "soup" : ["Суп с грибами", "Суп с тыквой", "Суп с лосем", "Суп с вермишелью"], 
  "main" : ["Лазанья", "Паста Карбонара", "Чизбургер"], 
  "salads" : ["Греческий салат", "Салат Цезарь", "Салат из свежих овощей"],
  "desserts": ["Чизкейк", "Тирамису", "Вишневый пирог"]
}


@app.route("/cats/")
def page_cats():
    # TODO допишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()