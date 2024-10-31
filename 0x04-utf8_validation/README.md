UTF-8 is a variable-length encoding system for Unicode characters, encoding each character into one to four bytes based on its Unicode code point. Here's a breakdown of how UTF-8 encoding works, along with the byte patterns for each possible character length.

### UTF-8 Encoding Rules

1. **One-byte (ASCII):**
   - **Pattern:** `0xxxxxxx`
   - **Range:** 0x00 - 0x7F (0 - 127 in decimal)
   - **Description:** UTF-8 preserves ASCII characters, which use only 7 bits, with a leading `0` bit. Any character in this range is encoded directly in a single byte (e.g., "A" = `0x41`).

2. **Two-byte Characters:**
   - **Pattern:** `110xxxxx 10xxxxxx`
   - **Range:** 0x80 - 0x7FF
   - **Description:** Characters in this range are encoded in two bytes. The first byte starts with `110`, and the second byte begins with `10`. Together, they can represent characters in the range 128 to 2047 (e.g., "é" = `0xC3A9`).

3. **Three-byte Characters:**
   - **Pattern:** `1110xxxx 10xxxxxx 10xxxxxx`
   - **Range:** 0x800 - 0xFFFF
   - **Description:** Characters in this range require three bytes, covering many common characters from languages beyond Latin (e.g., "汉" = `0xE6B18E`).

4. **Four-byte Characters:**
   - **Pattern:** `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
   - **Range:** 0x10000 - 0x10FFFF
   - **Description:** Characters in this range are encoded in four bytes, accommodating more rare characters, such as some emoji and less common script characters (e.g., "𠜎" = `0xF0A09C8E`).

### Valid UTF-8 Byte Patterns

For a sequence to be a valid UTF-8 encoding:
- Each multi-byte sequence starts with a specific prefix (e.g., `110`, `1110`, `11110`).
- Following bytes in a multi-byte character must start with `10`.
- The length of each sequence matches the initial prefix (e.g., `110` prefix indicates a two-byte character).

### Examples
- **Single-byte character (ASCII):** `"A"` (U+0041) → `0x41`
- **Two-byte character:** `"é"` (U+00E9) → `0xC3A9`
- **Three-byte character:** `"汉"` (U+6C49) → `0xE6B18E`
- **Four-byte character:** `"𠜎"` (U+2070E) → `0xF0A09C8E`

UTF-8's structure allows backward compatibility with ASCII while supporting a wide range of characters in Unicode.