# Python_Web_Review

Веб-сервис Шифратор:

В ячейке "About" пользователь может посмотреть описание шифратора

В верхнем поле - выбор режима ввода: файловый или набор текста в поле

P.S.: Выбор зависимый, если выбран файловый режим ввода - можно ввести только файл, если режим набора текста - можно ввести только текст.

Далее, также предоставляется зависимый выбор: шифрование и дешифрование с выбором шифра(Цезарь, Виженер) и вводом ключа; взлом Цезаря.

P.S.: При выборе режима взлома не работает ввод ключа и выбор шифра

P.S.: При некорректном вводе текста(не все символы лежат в алфавите или пустой текст),

или некорректном вводе ключа(не число при Цезаре, пустой ключ) сверху выводится сообщение об ошибке и указание к решению.

Как пользоваться?

Запуск сервиса: python solution.py

Запуск тестов: pytest tests.py 