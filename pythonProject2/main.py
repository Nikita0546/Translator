import googletrans


source_lang = 'ru'
destination_lang = 'en'

translator = googletrans.Translator()

while True:
    try:
        user_input = input("Русское слово -> ")
        translation = translator.translate(user_input, src=source_lang, dest=destination_lang)
        print(f"[!] Перевод: {translation.text}")
        print("\n")
    except KeyboardInterrupt:
        print("Пока ;)")
        break

    except (BaseException, Exception) as e:
        print(f"[!] Ошибка: {e}")
