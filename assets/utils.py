def is_cpf_valid(cpf: str):
    """
    Improved solution from http://wiki.python.org.br/Cpf
    :param cpf: formats are "00000000000" (eleven digits) or "000.000.000-00"
    """
    if not cpf.isdigit():
        cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or cpf in [11 * str(i) for i in range(10)]:
        return False

    cpf_sent = [int(x) for x in cpf]
    final_cpf = cpf_sent[:9]

    while len(final_cpf) < 11:
        result = sum([(len(final_cpf) + 1 - index) * cpf_digit for index, cpf_digit in enumerate(final_cpf)]) % 11
        final_cpf.append(11 - result if result > 1 else 0)

    return final_cpf == cpf_sent
