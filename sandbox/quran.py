import quran

text = quran.Quran()
j = 1
for i in range(int(input('Verse Count: '))):
    try:
        verse = text.get_verse(chapter_id=j, verse_id=i+1)
        translation = ' '.join(word['translation']['text'] for word in verse['verse']['words'] if 'translation' in word)
        print(translation)
    except KeyError:
        j += 1