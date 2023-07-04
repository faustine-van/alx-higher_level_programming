def text_indentation(text):
    """Prints a text with 2 new lines after each occurrence of ., ? or : in the text.

    Arguments:
    text -- the string to be used

    Raises:
    TypeError -- if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.splitlines()  # Split the text into lines
    processed_lines = []

    delimiters = (".", "?", ":")  # Delimiters to look for

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace from each line
        for delimiter in delimiters:
            if delimiter in line:
                line = line.replace(delimiter, delimiter + "\n\n")  # Add 2 new lines after each delimiter
        processed_lines.append(line)  # Remove leading/trailing spaces from the line


    result = "\n".join(processed_lines)  # Join the processed lines back into a single string
    print(result)

