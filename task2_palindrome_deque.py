"""Завдання2.Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи
до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи 
з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно
враховувати як рядки з парною, так і з непарною кількістю символів,
а також бути нечутливою до регістру та пробілів."""

from collections import deque

def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum()) 

    d = deque(cleaned) #двостороння черга

    #порівняння символів з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
#Перевірка
print(is_palindrome("1234567654321")) 
print(is_palindrome("А"))
print(is_palindrome("Мама втомилась!"))
print(is_palindrome("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"))