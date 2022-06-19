#  Telegram-бот для анализа сайта Hotels.com и поиска подходящих пользователю отелей

Для работы бота используется открытый API Hotels, который расположен на сайте rapidapi.com.

Telegram-бот воспринимаtn следующие команды:
>/start - запуск бота
> 
>/help — помощь по командам бота,
> 
>/lowprice — вывод самых дешёвых отелей в городе,
> 
>/highprice — вывод самых дорогих отелей в городе,
> 
>/bestdeal — вывод отелей, наиболее подходящих по цене и расположению от центра.
> 
>/history — вывод истории поиска отелей



## Описание работы команд
### Команды /lowprice и /highprice.
После ввода команды у пользователя запрашивается:
>1. Город, где будет проводиться поиск.
>2. Даты въезда и выезда из отеля
>3. Количество отелей, которые необходимо вывести в результате (не больше 25).
>4. Подтверждение введенных данных
>5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”) При положительном ответе пользователь также 
>вводит количество необходимых фотографий (не больше 10)


### Команда /bestdeal
После ввода команды у пользователя запрашивается:
>1. Город, где будет проводиться поиск.
>2. Диапазон цен.
>3. Диапазон расстояния, на котором находится отель от центра.
>4. Даты въезда и выезда из отеля
>5. Количество отелей, которые необходимо вывести в результате (не больше 25).
>6. Подтверждение введенных данных
>7. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”) При положительном ответе пользователь также 
>вводит количество необходимых фотографий (не больше 10)


### Команда /history
После ввода команды пользователю выводится история поиска отелей. 
Сама история
содержит:
>1. Команду, которую вводил пользователь.
>2. Дату и время ввода команды.
>3. Отели, которые были найдены.



При выполнении команд lowprice, highprice и bestdeal выводятся сообщения с результатом команды, содержащие следующую 
информацию по каждому отелю:
>1. фотографии отеля (если пользователь счёл необходимым их вывод)
>2. название отеля,
>3. рейтинг,
>4. адрес,
>5. расстояние до центра города,
>6. стоимость за ночь,
>7. общая стоимость
>8. ссылка на сайт отеля 
