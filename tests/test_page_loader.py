from page_loader.page_loader import download

def test_download_with_correct_data():
    file_path1 = download('https://ru.hexlet.io/courses', '/var/tmp')
    file_path2 = download('https://habr.com/ru/articles/740376', '/home/kivvesh/hexlet')

    assert file_path1 == '/var/tmp/ru-hexlet-io-courses.html'
    assert file_path2 == '/home/kivvesh/hexlet/habr-com-ru-articles-740376.html'

def test_download_with_unknown_dir():
    file_path = download('https://ru.hexlet.io/courses', '/varsdfsdf/tmp')

    assert file_path == False

def test_download_with_closed_dir():
    file_path = download('https://ru.hexlet.io/courses','/var')

    assert  file_path == False
