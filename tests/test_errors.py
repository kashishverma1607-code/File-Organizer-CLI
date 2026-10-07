from fileorganizer.cli import organize_files


def test_missing_folder():
    result = organize_files("D:\\Kashish\\ABC123")

    assert result == 2