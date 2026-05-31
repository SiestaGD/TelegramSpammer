import pyautogui
import time
import configparser
import os
import pyperclip
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.chdir(BASE_DIR)

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# Читаем конфиг
text = config.get('Settings', 'text')
delay = config.getfloat('Settings', 'delay')
start_delay = config.getfloat('Settings', 'start_delay')
max_messages = config.getint('Settings', 'max_messages')
save_logs = config.getboolean('Settings', 'save_logs')


print("=" * 40)
print("     TELEGRAM SPAMMER")
print("=" * 40)
print(f"Текст: {text}")
print(f"Задержка: {delay} сек")
if max_messages > 0:
    print(f"Отправить: {max_messages} раз")
else:
    print(f"Отправить: бесконечно")
print("=" * 40)

# Логи
if save_logs:
    os.makedirs('logs', exist_ok=True)
    log_file = f"logs/session_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    print(f"Логи: {log_file}")

print(f"\n🚀 Старт через {start_delay} секунд...")
print("📌 Переключись в Telegram и кликни в поле ввода!")
print("🛑 Нажми Ctrl+C для остановки\n")

time.sleep(start_delay)

# Основной цикл
sent = 0

try:
    while max_messages == 0 or sent < max_messages:
        # Копируем в буфер и вставляем
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        sent += 1
        
        
        print(f"[{sent}] {text}")
        
        # Логи
        if save_logs:
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {text}\n")
        
        time.sleep(delay)
        
except KeyboardInterrupt:
    print(f"\n\n⛔ Остановлено!")

print(f"\n📊 Отправлено: {sent}")
print("\nНажми Enter для выхода...")
input()
