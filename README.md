﻿1\. Открыть PyCharm.

2\. В верхнем меню навести курсором на “File”.

3\.  В выпадающем списке нажать на “New Project..”.

4\. Поставить чек-бокс на “Create a main.py welcome script”.

5\. Нажать кнопку “Create”.

6\. Нажать кнопку “This Window”.

7\. Вернуться в GitHub и скопировать код из файла “test.py”.

8\. Вернуться в PyCharm и вставить скопированный код в созданный файл main.py.

9\. Открыть терминал(В нижнем левом углу нажать на значок  квадрата внутри символы >_) . Откроется терминал.

10\. Написать в терминале команду pip install pytest-playwright. Подождать, когда закончится загрузка.

11\. Написать в терминале команду playwright install. Подождать, когда закончится загрузка.

12\. Для получения скриншотов для счетчика воды нажать на зеленый треугольник находящийся рядом с функцией def test\_water(page: Page): . Нажать на Run. 

13\. Подождать, когда функция завершит работу. 

14\. Если возникли ошибки при запуске, то зайти в терминал и вставить команду pytest -k test\_water

15\. Для получения скриншотов для счетчика CO2 нажать на зеленый треугольник находящийся рядом с функцией def test\_co2(page: Page): . Нажать на Run. 

16\. Подождать, когда функция завершит работу. 

17\. Если возникли ошибки при запуске, то зайти в терминал и вставить команду pytest -k test\_co2

18\. Для получения скриншотов для счетчика энергии нажать на зеленый треугольник находящийся рядом с функцией def test\_energy(page: Page): . Нажать на Run. 

19\. Подождать, когда функция завершит работу. 

20\. Если возникли ошибки при запуске, то зайти в терминал и вставить команду pytest -k test\_ energy

21\. Слева появится папка с названием “output”. В ней расположены полученные скриншоты. 

