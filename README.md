# Telegram Bot

Этот проект реализует Telegram бота  для техподдержки, который будет использоваться для помощи новым ученикам нашей школы и их родителям. Бот будет предоставлять информацию о школе, ее услугах, процессах работы, а также отвечать на самые часто задаваемые вопросы.

## Установка и запуск

### Шаги по установке

1. Склонируйте репозиторий:

    ```bash
    git clone <URL репозитория>
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd <название папки репозитория>
    ```

3. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:

    - На Windows:

        ```bash
        venv\Scripts\activate
        ```

    - На MacOS/Linux:

        ```bash
        source venv/bin/activate
        ```


5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Конфигурация

1. Создайте файл `.env` в корневой директории проекта и добавьте в него следующие переменные:

    ```dotenv
    TELEGRAM_API_TOKEN=your_telegram_api_token
    ADMIN_CHANNEL_ID=your_admin_channel_id
    ```

2. Замените `your_telegram_api_token` на ваш токен API Telegram бота, а `your_admin_channel_id` на ID вашего закрытого канала для администраторов.

## Запуск

Для запуска бота используйте следующую команду:

```bash
python bot.py
```

## Описание файлов

- `bot.py`: Основной файл кода, содержащий логику бота.
- `text.py`: Файл, содержащий текстовые константы, используемые в боте.

## Описание переменных

- `ADMIN_CHANNEL_ID`: ID канала администратора для получения обратной связи.
- `user_states`: Словарь для отслеживания состояний пользователей.
- `user_question`: Переменная для хранения последнего вопроса пользователя.

## Описание функций

- `information_button()`: Создание кнопки "Узнать больше".
- `create_buttons_markup()`: Создание кнопок для основного меню.
- `create_info_markup()`, `create_summer_info_markup()`, `create_pay_info_markup()`: Создание кнопок для подменю.
- `main(message)`: Обработчик команды `/start`.
- `callback(call)`: Обработчик всех callback-запросов.
- `handle_feedback(message)`: Обработчик обратной связи от пользователей.

## Используемые библиотеки

- `pyTelegramBotAPI`: Библиотека для работы с API Telegram.

## Пример использования

После установки зависимостей и запуска бота, отправьте команду `/start` в чат с ботом. Бот ответит приветственным сообщением с кнопкой "Узнать больше". Нажатие на эту кнопку откроет меню с несколькими опциями, такими как информация о плате, обучении и расписании. Вы также можете отправить обратную связь, нажав на соответствующую кнопку.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле `LICENSE`.
