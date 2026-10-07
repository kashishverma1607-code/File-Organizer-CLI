from fileorganizer.cli import organize_files


def test_files_are_organized(tmp_path):

    # Create test files
    resume = tmp_path / "resume.pdf"
    photo = tmp_path / "photo.jpg"
    song = tmp_path / "song.mp3"

    resume.write_text("test resume")
    photo.write_text("test photo")
    song.write_text("test song")

    # Run organizer
    result = organize_files(str(tmp_path))

    # Check successful result
    assert result == 0

    # Check files moved to correct folders
    assert (tmp_path / "Documents" / "resume.pdf").exists()
    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Audio" / "song.mp3").exists()
    