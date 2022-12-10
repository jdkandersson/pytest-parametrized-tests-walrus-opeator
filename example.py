def get_second_word(text: str) -> str | None:
    """Get the second word from text."""
    words = text.split()
    return words[1] if len(words) >= 2 else None
