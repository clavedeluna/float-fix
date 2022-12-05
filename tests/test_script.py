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
@mock.patch("script.print")  # do not mock builtins.print!
def test_do_not_change(mock_print):
    run("doenstmatter")
    for idx, result in enumerate(mock_print.call_args_list):
        assert result[0][0] == GOOD[0][idx]

def test_change():
    assert 1==1