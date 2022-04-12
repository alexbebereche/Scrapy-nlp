import nltk
import json

def extract_json(file_name: str) -> set:
    # read file
    with open(file_name, "r") as jf:
        json_data = json.load(jf)

    # create a set, because there is an article that appears on every page
    title_set = set()

    # traverse json file
    for json_item in json_data:
        title_set.add(json_item["title"])  
    
    return title_set

if __name__ == "__main__":
    title_set =  extract_json("blog.json")
    title_str = str(title_set)   
    
    all_words = nltk.tokenize.word_tokenize(title_str)

    stopwords = nltk.corpus.stopwords.words('english')
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in all_words if (w.lower() not in stopwords) and (w.isalpha() == True)) # could add len condition to exclude words like 'a'

    print(allWordExceptStopDist.most_common(100))
