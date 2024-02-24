from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://pavlenkooksanaod:K6Blo1wve6JNREgL@cluster0.c8dy3qp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book


# функція створює новий документ коллекції
def create_doc(name, age, features):
    cat_data = {
        "name": name,
        "age": age,
        "features": features if isinstance(features, list) else [features]
    }
    result = db.mine_cats.insert_one(cat_data)
    print(f"Додано нового кота з ID: {result.inserted_id}")


# функція для виведення всіх записів із колекції
def print_bd():
    result = db.mine_cats.find({})
    count = db.mine_cats.count_documents({})
    if count == 0:
        print("В нашій базі коти відсутні")
    else:
        print("База котів виглядає наступним чином:")
        for el in result:
            print(el)
    print("\n")    


# функція, що дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота
def print_cat():
    cat_name = input ("Введіть ім'я кота для пошуку: ")
    result = db.mine_cats.find({"name":cat_name})
    count = db.mine_cats.count_documents({"name": cat_name})
    if count >= 1:
        for cat in result:
            print(f"Інформація про кота:\nІм'я: {cat['name']}\nВік: {cat['age']}\nХарактеристики: {cat['features']}\n")
    else:
        print(f"Кіт з ім'ям {cat_name} в базі відсутній")


# функція, що дозволяє оновити вік кота за ім'ям
def update_age_cat(cat_name, new_age):
    result = db.mine_cats.update_one({"name": cat_name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Вік кота з ім'ям {cat_name} оновлено успішно\n")
    else:
        print(f"Кота з ім'ям {cat_name} не знайдено\n")


# функція, що дозволяє додати нову характеристику до списку features кота за ім'ям
def add_feature_to_cat(cat_name, new_feature):
    result = db.mine_cats.update_one(
        {"name": cat_name},
        {"$addToSet": {"features": new_feature}}
    )
    
    if result.modified_count > 0:
        print(f"Нова характеристика додана до кота з ім'ям {cat_name}")
    else:
        print(f"Кота з ім'ям {cat_name} не знайдено")


# функція для видалення запису з колекції за ім'ям тварини
def delete_cat(cat_name):
    result = db.mine_cats.find({"name":cat_name})
    count = db.mine_cats.count_documents({"name": cat_name})
    if count >= 1:
        for cat in result:
            db.mine_cats.delete_one({"name": cat_name})
            print(f"Інформація про кота {cat['name']} із бази видалена")
    else:
        print(f"Кіт з ім'ям {cat_name} в базі відсутній")


# функція для видалення всіх записів із колекції    
def delete_all_cat():
    count = db.mine_cats.count_documents({})
    if count >= 1:
        result = db.mine_cats.find({})
        for cat in result:
            db.mine_cats.delete_one({"_id": cat["_id"]})
            print(f"Інформація про кота {cat['name']} із бази видалена")
    else:
        print("В нашій базі коти відсутні")


# create_doc("Барсік", 3, "прожерливий")
# create_doc("Мяв", 22, "ошатна бабуся")
# create_doc("Агата", 7, "сфінкс, мерзне")
# create_doc("Патрон", 9, "дуже цілеспрямований")
# create_doc("Москаль", 13, "полюбляє пакети, переважно чорного кольору")
# create_doc("Пуйло", 666, "сдох")        

# print_bd()

print_cat() 
# update_age_cat("Barsik2",3)
# update_age_cat("Барсік",1)
# add_feature_to_cat("Мяв", "полюбляє сало")
# delete_cat("May222")
# delete_cat("Пуйло")
# delete_cat("Москаль")
# delete_all_cat()

print_bd()




