
def wrapper (td, kernel, resource):
    """
    The kernel executable will become the new executable.  The old executable
    gets pre-pended to the argument list.
    """

    if not td.executable:
        raise ValueError ("cannot apply wrapper filter to TD w/o executable")

    if not td.arguments:
        td.arguments = list()

    td.arguments.insert (0, td.executable)


