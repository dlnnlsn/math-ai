from lingua import LanguageDetectorBuilder
import os
from random import choice


def main():
    detector = LanguageDetectorBuilder.from_all_languages().build()

    prompt = input("Hello! I am your AI mathematics assistant."
                   "How can I help you today?\n")

    language = detector.detect_language_of(prompt)
    language_code = language.iso_code_639_1.name

    languages_directory = os.path.join(os.path.dirname(__file__), "languages")

    try:
        with open(
            os.path.join(languages_directory, f"{language_code}.txt"), "r"
        ) as f:
            responses = f.readlines()
    except FileNotFoundError:
        try:
            with open(os.path.join(languages_directory, "en.txt"), "r") as f:
                responses = f.readlines()
            print(f"Sorry, I don't know how to speak {language.name.title()},"
                  "so I will loudly and agressively speak English instead")
        except FileNotFoundError:
            print("Sorry, I don't know how to speak any language at all")
            return

    print(choice(responses), end="")


if __name__ == "__main__":
    main()
