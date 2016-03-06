def to_str(bytes_or_str):
    """
    Converts a string or byte sequence to a string

    :param bytes_or_str: data of type str or bytes
    :return: the data as string
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    """
    Converts a string or byte sequence into a byte sequence

    :param bytes_or_str: data of type str or bytes
    :return: the data as bytes
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value
