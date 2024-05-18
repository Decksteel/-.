#Задача 1-3, я решил одним кодом сразу выполнить 3 задания, так как суть у них одна



name_product = str(input("Введите названия продукта: "))
cost_of_product = float(input("Введите стоимость продукта руб/кг: "))
product_weight = float(input("Введите вес продутка = "))
final_cost = cost_of_product * product_weight
print("Стоимость продукта составляет =",final_cost)
deposited_funds = float(input("Введите внесенные средства = "))
def_cls = "\n"
if deposited_funds == final_cost:
    print(def_cls * 100)
    print("Товарный чек")
    print("Наименование продукта: ", name_product, product_weight,"кг",cost_of_product,"руб/кг")
    print("Итого:", final_cost)
    print("Внесенные средства: ", deposited_funds)
    change = deposited_funds - final_cost
    print("Ваша сдача =", change)
else:
     if deposited_funds < final_cost:
         print("Недостаточно средств")
     else:
         print(def_cls * 100)
         print("Товарный чек")
         print("Наименование продукта: ", name_product, product_weight, "кг", cost_of_product, "руб/кг")
         print("Итого:", final_cost)
         print("Внесенные средства: ", deposited_funds)
         change = deposited_funds - final_cost
         print("Ваша сдача =",change)


