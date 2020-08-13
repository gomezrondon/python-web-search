import webbrowser
import pyperclip


if __name__ == '__main__':
    paste_test = pyperclip.paste()
    paste_test = ' '.join([w for w in paste_test.split() if len(w) > 3])
    paste_test = paste_test.replace(" ", "+")
    url_wiki = 'https://en.wikipedia.org/w/index.php?search='
    # search_term = 'cloud+computing'
    search_term = paste_test
    print(url_wiki + search_term)
    webbrowser.open(url_wiki + search_term)
