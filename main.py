import sys

def display_text(message: str) -> None:
    """
    Выводит текст на экран.
    
    Args:
        message (str): Текст для вывода.
    """
    print(message)

def main():
    # Если пользователь передал текст через командную строку, используем его.
    # Пример запуска: python main.py "Привет, это мой первый проект!"
    if len(sys.argv) > 1:
        text_to_show = " ".join(sys.argv[1:])
    else:
        # Текст по умолчанию для демонстрации
        text_to_show = (
            "Привет! Это мой первый проект на GitHub для изучения нейросетей. "
            "Я учусь работать с Python и ИИ. Alice AI помогает мне расти!"
        )
    
    try:
        display_text(text_to_show)
    except Exception as e:
        print(f"Произошла ошибка при выводе текста: {e}")

if __name__ == "__main__":
    main()
