def word_count(word):
    return len(word.split())


def create_dict(arr):
    my_dict={}
    for char in arr:
        if(char not in my_dict):
            my_dict[char]=1
        else: my_dict[char]+=1
    return my_dict

def print_report(dict,count):
    print(f"{count} words found in the document ")
    for key, value in dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents=f.read()
        count=word_count(file_contents)
        char_list=list(file_contents.lower())
        char_dict=create_dict(char_list)
        sorted_dict=dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
        print_report(sorted_dict, count)
main()