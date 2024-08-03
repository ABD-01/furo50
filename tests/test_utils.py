from furo50 import trim_css


def test_trim_css():

    input_css = """
    /* Comment */
    body {
        background: white;    /* another comment */
        color:  black;
    }
    """
    expected_output = "body{background:white;color:black;}"
    assert trim_css(input_css) == expected_output
