def transform(legacy_data):
    data = {}

    for score in legacy_data.keys():
        for letter in legacy_data[score]:
            data[letter.lower()] = data.get(letter.lower(), score)

    return data
