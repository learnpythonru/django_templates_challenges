"""
У нас есть страница для администраторов. Любого пользователя сейчас мы приветствуем как администратора,
но хотелось бы запретить доступ к странице для не администраторов.

Задания:
    1. Найдите в проекте темплэйт admin_page.html и сделайте так, чтобы в зависимости от значения переменной is_admin
       пользователь видел либо приветствие, либо сообщение о том что ему сюда доступ запрещен.
    2. Откройте страницу http://127.0.0.1:8000/admin/ и посмотрите на результат.
    3. Поменяйте значение is_admin во вьюхе admin_page_view на True и снова посмотрите результат на странице http://127.0.0.1:8000/admin/
"""
from django.shortcuts import render
import random


def admin_page_view(request):
    is_admin = True
    list_name = ['Князь', 'Боярен', 'Дружинник', 'Холоп', 'Купец', 'Смерд']
    name_send = random.choice(list_name) 

    return render(request, 'admin_page.html', context={'is_admin': is_admin, 'name_send': name_send})
