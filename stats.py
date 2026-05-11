def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_string = text.lower()
    chars = {}
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    """Hilfsfunktion für die Sortierung nach der Anzahl."""
    return dict["num"]

def get_sorted_list(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        # Aufgabe: Nur alphabetische Zeichen berücksichtigen
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    # Absteigend sortieren (groß nach klein)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
 
