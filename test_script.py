import requests
import pyfiglet

# Використовуємо requests
print(f"Поточна версія requests у цьому оточенні: {requests.__version__}")

# Використовуємо pyfiglet
ascii_art = pyfiglet.figlet_format("VS Code VENV!")
print(ascii_art)

# file_write = input("Введите название файла")
# with open(file_write, "a") as file:
#     file.write(file_write + "\n")
#     print(f"Вы успешно создали файл {file_write}")
