import requests


class Stack_Overflow:
    def get_question(self, from_date, to_date, tag, page_count=1):

        link = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'fromdate': from_date,
            'todate': to_date,
            'page': str(page_count),
            'pagesize': '50',
            'order': 'desc',
            'sort': 'creation',
            'tagged': tag.lower(),
            'site': 'stackoverflow'
        }
        response = requests.get(link, params=params, timeout=5)
        response.raise_for_status()
        if response.json()['items'] == []:
            return 'Stop'
        for question in response.json()['items']:
            print(f"{question['title']}")


if __name__ == '__main__':
    from_date = '2022-02-08'
    to_date = '2022-02-10'
    tag = 'python'
    quest = Stack_Overflow()
    result = 'Start'
    page = 1

    while result != 'Stop':
        result = quest.get_question(from_date, to_date, tag, page)
        if result == 'Stop':
            break
        page += 1
