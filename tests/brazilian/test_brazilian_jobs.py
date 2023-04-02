from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_translation = read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
        )
    assert brazilian_translation[1] == {
            "salary": "3000",
            "title": "Motorista",
            "type": "full time",
    }
