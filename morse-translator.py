class MorseCodeTranslator:
    def __init__(self):
        # Dictionary mapping characters to Morse code
        self.char_to_morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ' ': ' ', '.': '.-.-.-', ',': '--..--', '?': '..--..',
            '!': '-.-.--', '@': '.--.-.', '&': '.-...'
        }
        # Create reverse dictionary for decoding
        self.morse_to_char = {value: key for key, value in self.char_to_morse.items()}
    
    def to_morse(self, message):
        """Convert text to Morse code"""
        try:
            morse = []
            for char in message.upper():
                if char in self.char_to_morse:
                    morse.append(self.char_to_morse[char])
            return ' '.join(morse)
        except Exception as e:
            return f"Error encoding message: {str(e)}"
    
    def from_morse(self, morse):
        """Convert Morse code to text"""
        try:
            # Split morse code into individual symbols
            symbols = morse.split(' ')
            text = []
            for symbol in symbols:
                if symbol in self.morse_to_char:
                    text.append(self.morse_to_char[symbol])
                elif symbol == '':
                    text.append(' ')
            return ''.join(text)
        except Exception as e:
            return f"Error decoding message: {str(e)}"

# Example usage
if __name__ == "__main__":
    translator = MorseCodeTranslator()
    
    # Test encoding
    message = "Hello World"
    morse = translator.to_morse(message)
    print(f"Original message: {message}")
    print(f"Morse code: {morse}")
    
    # Test decoding
    decoded = translator.from_morse(morse)
    print(f"Decoded message: {decoded}")
