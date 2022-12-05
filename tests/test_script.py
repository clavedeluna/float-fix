import mock
from script import run

GOOD = [
    ["var = 1.",
    "var = 1.00000",
    "var = 1.2",
    "#10.d",
    "var = 30.20",
    "var = '22.'",
    ] # lines with only floats

    # TODO: longer lines with other things
]
@mock.patch("fileinput.input", mock.MagicMock(return_value=GOOD[0]))
@mock.patch("script.no_change")
@mock.patch("script.change")
def test_do_not_change(mock_change, mock_no_change):
    run("doenstmatter")
    assert mock_change.call_count == 0
    assert mock_no_change.call_count == len(GOOD[0])

def test_change():
    assert 1==1