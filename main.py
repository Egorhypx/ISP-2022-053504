import re


def textInput():
    string = input("Input string: ")
    string = re.sub('[,.!?\n]', '', string)
    return string


def numbersInput():
    k = int(input("Input k: "))
    n = int(input("Input n: "))
    if k == "":
        k = 10

    if n == "":
        n = 4

    return [k, n]


def getList(string: str):
    words = string.split()
    return words


def amountOfWords(words: list):
    words_count = {}
    for item in words:
        if words_count.__contains__(item):
            continue
        words_count[item] = words.count(item)
    return words_count


def averegeAmountOfWords(words: list, words_count: dict):
    return len(words) / len(words_count)


def medianWordNumber(words_amount: dict):
    words = words_amount.values()
    words = list(words)
    if len(words) % 2 == 0:
        med = (words[int(len(words) / 2 - 1)] + words[int(len(words) / 2)]) / 2
    else:
        med = words[len(words) // 2]
    return med


def getNgram(words: list, string: str, n: int):
    ngram = {}
    for item in words:
        for i in range(len(item)):
            if i + n > len(item):
                break
            if not ngram.__contains__(item[i:i + n]):
                ngram[item[i: i + n]] = string.count(item[i:i + n])
    return ngram


def showNgram(ngram: dict, k: int):
    ngram = sorted(ngram, key=ngram.get)
    ngram.reverse()
    for i in range(k if len(ngram) > k else len(ngram)):
        print(ngram[i])


def main():
    k, n = numbersInput()
    string = textInput()

    words = getList(string)
    words_amount = amountOfWords(words)

    print("Words amount: " + str(words_amount))
    average_words_amount = averegeAmountOfWords(words, words_amount)

    print("Average words amount: " + str(average_words_amount))
    median_words_amount = medianWordNumber(words_amount)

    print("Median words amount: " + str(median_words_amount))
    n_grams = getNgram(words, string, n)
    showNgram(n_grams, k)


if __name__ == '__main__':
    main()