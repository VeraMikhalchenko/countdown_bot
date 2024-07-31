import os
import telebot
from datetime import datetime, timedelta

# Получаем токен бота и ID чата из переменных окружения
BOT_TOKEN = os.environ['7294943213:AAGJGOXFPRzloQACxAjCTfLf4NBa3nmPEkM']
CHAT_ID = int(os.environ['-250785345'])

bot = telebot.TeleBot(BOT_TOKEN)

# Устанавливаем дату окончания отсчета
END_DATE = datetime(2024, 12, 31)  # Пример: до конца 2024 года

def send_daily_update():
    now = datetime.now()
    remaining_time = END_DATE - now
    
    if remaining_time.total_seconds() > 0:
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        message = f"Осталось:\n{days} дней\n{hours:02d} часов\n{minutes:02d} минут\n{seconds:02d} секунд"
    else:
        message = "Время вышло!"
    
    bot.send_message(CHAT_ID, message)
    print(f"Сообщение отправлено: {message}")

if __name__ == "__main__":
    try:
        send_daily_update()
        print("Обновление успешно отправлено")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
