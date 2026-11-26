"""One Line to Your Younger Self - make.fun entry.

Writes a single line, in English, that the writer would send back to
their younger self if one line were all they got. Gate: /output/entry.txt
must be UTF-8 text of 1 to 200 characters, not only white space.
"""

LINE = "You'll spend ten years chasing the money, then spend the money chasing the ten years back."


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only white space"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    verify_output(text)


def verify_output(expected):
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == expected, "output does not match the line"
    assert 1 <= len(data.decode("utf-8")) <= 200, "output outside the 1-200 char gate"
    print(f"verified {len(data)} bytes, byte-identical")


if __name__ == "__main__":
    main()
