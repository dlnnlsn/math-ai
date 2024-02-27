from random import choice


def main():
    input("Hello! I am your AI mathematics assistant. How can I help you today?\n")
    print(choice([
        "This is a straightforward application of known results in the literature.",
        "This is left as an exercise to the reader.",
        "The result is trivial.",
        "The proof is beyond the scope for the current discussion, but can be found in any good textbook on the topic.",
        "The problem can be reduced to one famously solved by Gauss.",
        "The problem can be reduced to one famously solved by Euler.",
        "The problem can be reduced to one famously solved by Ramanujan.",
        "The problem can be reduced to one famously solved by Erdos.",
        "The problem can be reduced to one famously solved by Hilbert.",
        "The problem can be reduced to one famously solved by Poincare.",
        "The problem can be reduced to one famously solved by Riemann.",
        "I have a remarkable proof of this theorem, but this terminal is too small to contain it.",
    ]))


if __name__ == "__main__":
    main()
