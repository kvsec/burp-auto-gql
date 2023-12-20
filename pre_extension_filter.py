import json

def find_matching_fields(introspection_data, word_list):
    matching_fields = set()

    for qparent in introspection_data['data']['__schema']['types']:
        fields = qparent.get('fields')

        if fields and isinstance(fields, list):
            for field in fields:
                field_name = field['name']

                if any(word.lower() == field_name.lower() for word in word_list):
                    matching_fields.add(field_name)

    return matching_fields

# Load introspection data from a file
with open('introspection.json', 'r') as file:
    introspection_data = json.load(file)

with open('raw_words.txt', 'r') as word_file:
    raw_words = word_file.read().strip()

word_list = raw_words.split()

result = find_matching_fields(introspection_data, word_list)

print("Matching Fields without Duplicates:")
for field in result:
    print(f"- {field}")

not_found_words = list(set(word.lower() for word in word_list) - set(match.lower() for match in result))

print("\nWords Not Found:")
print(', '.join(f"'{word}'" for word in not_found_words))

print("\nWords Found:")
print(', '.join(f"'{word}'" for word in result))

num_words_submitted = len(word_list)
num_words_found = len(result)
print(f"\nNumber of Words Submitted: {num_words_submitted}")
print(f"Number of Words Found: {num_words_found}")
