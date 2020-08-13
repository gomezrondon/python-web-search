import webbrowser
import pyperclip


if __name__ == '__main__':
    paste_test = pyperclip.paste()
    paste_test = ' '.join([w for w in paste_test.split() if len(w) > 3])
    paste_test = paste_test.replace(" ", "+")
    google_url = 'https://www.google.com/search'
    # search_term = 'cloud+computing'
    search_term = '?q='+paste_test
    print(google_url + search_term)
    webbrowser.open(google_url + search_term)
