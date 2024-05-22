from src.page_loader import download

def test_download():
    file_path1 = download('https://ru.hexlet.io/courses', '/var/tmp')
    file_path2 = download('https://ru.hexlet.io/courses', '/varsdfsdf/tmp')
    file_path3 = download('https://habr.com/ru/articles/740376','/home/kivvesh/hexlet')

    assert file_path1 == '/var/tmp/ru-hexlet-io-courses.html'
    assert file_path2 == False
    assert file_path3 == '/home/kivvesh/hexlet/habr-com-ru-articles-740376.html'