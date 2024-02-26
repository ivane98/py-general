import json

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
 
def most_spoken_languages(fname, value):
    f = open(fname, encoding="UTF8")
    to_analyse = json.load(f)

    total_languages_initial = []
    counts = {}
    output_list = []

    for i in to_analyse:
        total_languages_initial.extend(i["languages"])

    for i in total_languages_initial:
        counts[i] = counts.get(i, 0) + 1

    counts = sort_dict_by_value(counts, True)

    for i in list(counts.items())[:value]:
        output_list.append(i)

    f.close()

    return [(sub[1], sub[0]) for sub in output_list]




print(most_spoken_languages('countries_data.json', 10))



