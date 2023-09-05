import sys

if not sys.argv[1]:
    print("No parameter!")
else:
    split_strings = sys.argv[1].split(" ")
    print("model: "+split_strings[0])
    if split_strings[0] == 'RandomForestClassifier':
        n_estimators = split_strings[1]
        criterion = split_strings[2]
        print("n_estimators: "+split_strings[1])
        print("criterion: "+split_strings[2])
    elif split_strings[0] == 'DecisionTreeClassifier':
        max_depth = split_strings[1]
        print("max_depth: "+split_strings[1])
        
    
model = split_strings[0]
# n_estimators = split_strings[1]
# criterion = split_strings[2]

def modify_python_file(file_path, new_code):
    with open(file_path, 'r') as file:
        content = file.read()

    start_tag = "        # START_MODEL_CODE"
    end_tag = "        # END_MODEL_CODE"

    start_index = content.find(start_tag)
    end_index = content.find(end_tag)

    if start_index != -1 and end_index != -1:
        old_code = content[start_index:end_index + len(end_tag)]
        replacement = start_tag + '\n' + new_code + '\n' + end_tag
        content = content.replace(old_code, replacement)
        with open(file_path, 'w') as file:
            file.write(content)
        print("File modified successfully.")
    else:
        print("Custom code tags not found.")
        
new_code = ""
if model == 'RandomForestClassifier':
    new_code = "        from sklearn.ensemble import RandomForestClassifier\n        return RandomForestClassifier(n_estimators="+n_estimators+", criterion = '"+criterion+"')"
elif model == 'DecisionTreeClassifier':
    new_code = "        from sklearn.tree import DecisionTreeClassifier\n        return DecisionTreeClassifier(max_depth="+max_depth+")"

file_path = "./target_sklearn.py"

modify_python_file(file_path, new_code)
