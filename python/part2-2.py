# DEBBUGING SECOND CODE
import webbrowser
import re
def search_google(query):
 """Search for the given query on Google and open the first result in a web
browser."""
 url = f'https://www.google.com/search?q={query}'
 response = webbrowser.open(url)
 if not response:
    return 'Unable to open web browser' ### added space
 html = webbrowser.get().open(url).read().decode('utf-8')
 pattern = re.compile(r'<a href="(https?://.*?)"')
 match = pattern.search(html)
 if not match:
    return 'No search results found' ### added space
 result_url = match.group(2)
 response = webbrowser.open(result_url)
 if not response:
    return 'Unable to open web browser' ### added space
 return 'Success'
if __name__ == '__main__':
 query = None
 result = search_google(query)
 print(result)

 ## To debug this code I just had to fix to if return placements.