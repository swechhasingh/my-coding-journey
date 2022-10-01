import imp
from typing import List
import re
import unittest
import random
from collections import Counter

def generate_n_grams(text:str, n=1)->List[str]:
    # return empty list or raise value error??
    if not text:
        # raise ValueError(f"Empty string input: {text}")
        return []

    # pre-processing
    # lower case
    text = text.lower()
    
    # Replace all none alphanumeric characters with spaces, replace by bcoz of words like this Natural-language
    text = re.sub(r'[^a-zA-Z\d\s]', ' ', text)
    
    # Tokenization, remove empty tokens
    tokens = [token for token in text.split(" ") if token != ""]
    
    # print(f"Tokenized sentence: {tokens}")

    n_grams = []
    n_words = len(tokens)

    # time-complexity: O(n_words*n)
    for i in range(n_words-n+1):
        n_grams.append(" ".join(tokens[i:i+n]))
        
    return n_grams

class Test(unittest.TestCase):
    def test_n_gram(self,):
        test_cases = []
        test_cases.append(("one two three (four)", 2, ['one two', 'two three', 'three four']))
        test_cases.append(("", 2, []))
        test_cases.append(("    ", 2, []))

        for input_text, n, n_grams in test_cases:
            output = generate_n_grams(input_text, n)
            # print(output)
            self.assertEqual(n_grams, output, f"Test Failed for {n}-gram for input:{input_text}")
        print("-----------All test cases passed!-----------")


if __name__ == "__main__":
    with open("./input.txt","r") as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())

    text = " ".join(lines)
    print(f"Input text: {text}\n")
    N = 3
    all_n_grams = []
    # weight = length of a gram, for eg: k-gram will have a weight of 'k'
    n_gram_weigths = []
    for n in range(1,N+1):
        n_grams = set(generate_n_grams(text, n))
        all_n_grams += n_grams
        n_gram_weigths += [n]*len(n_grams)

    print(f"All-{N}-grams: {all_n_grams}\n")
    print(f"All-{N}-grams weight: {n_gram_weigths}\n")
    
    # generate 100 grams from all_n_grams list with corresponding n_gram_weigths weigths
    generated_n_grams = random.choices(all_n_grams, n_gram_weigths, k=10)
    print(f"Generated n-grams: {generated_n_grams}")
    
    unittest.main()


