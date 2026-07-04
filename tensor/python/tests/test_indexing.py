from python.indexing import compute_offset


def test_returns_zero_for_first_element():
    assert (
        compute_offset(
            indices=(0, 0),
            shape=(2, 3),
            strides=(3, 1),
        )
        == 0
    )


def test_computes_offset_for_first_row():
    assert (
        compute_offset(
            indices=(0, 2),
            shape=(2, 3),
            strides=(3, 1),
        )
        == 2
    )


def test_computes_offset_for_second_row():
    assert (
        compute_offset(
            indices=(1, 0),
            shape=(2, 3),
            strides=(3, 1),
        )
        == 3
    )


def test_computes_offset_for_last_element():
    assert (
        compute_offset(
            indices=(1, 2),
            shape=(2, 3),
            strides=(3, 1),
        )
        == 5
    )
