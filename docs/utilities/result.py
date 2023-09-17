def get_category(output):
    confidences_list = output["confidences"]
    category = confidences_list[0]["label"]
    return str(category).capitalize()


def get_titles(output):
    confidences_list = output["confidences"]
    titles = [elem["label"] for elem in confidences_list]
    return titles


def get_genres(output):
    confidences_list = output["confidences"]
    genres = [elem["label"] for elem in confidences_list]
    return genres
