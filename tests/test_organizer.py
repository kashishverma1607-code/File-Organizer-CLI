from fileorganizer.cli import get_category


def test_pdf_is_document():
    assert get_category("resume.pdf") == "Documents"


def test_jpg_is_image():
    assert get_category("photo.jpg") == "Images"


def test_mp3_is_audio():
    assert get_category("song.mp3") == "Audio"


def test_mp4_is_video():
    assert get_category("movie.mp4") == "Videos"


def test_unknown_file_is_other():
    assert get_category("file.xyz") == "Others"