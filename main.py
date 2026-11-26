#!/usr/bin/env python3
"""Entry for make.fun bounty: Funniest Forecast for a City That Isn't

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "Tomorrow in Nowhere: sunny with a chance of confusion. Bring an umbrella, just in case reality shows up."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
