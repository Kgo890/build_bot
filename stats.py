def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        file_contents = f.read()
    return file_contents


def counting_characters(text):
    character_count = {}
    for i in text:
        character_count[i.lower()] = character_count.get(i.lower(), 0) + 1
    return character_count


def sorted_count(text_dic):
    char_list = [{"character": char, "count": count} for char, count in text_dic.items()]
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list



def count_words(text):
    words = text.split()
    count = len(words)
    return count
