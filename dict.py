studentdata = {
    'id1': {'name': 'John', 'class': 'XAAAA', 'subject_integration': 'engish, maf, sience'},
    'id2': {'name': 'Daquavius', 'class': 'XBBBB', 'subject_integration': 'engish, maf, sience'},
    'id3': {'name': 'John', 'class': 'XAAAA', 'subject_integration': 'engish, maf, sience'},
    'id4': {'name': 'Pork', 'class': 'XHABH', 'subject_integration': 'engish, maf, sience'},
}

result = {}
seen_keys = []

for student_id, details in studentdata.items():
    unique_key = (details['name'], details['class'], details['subject_integration'])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ':', v)