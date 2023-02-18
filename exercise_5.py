
def version_comparison(ver_A, ver_B): # версии от 1.0 до 1.10, где 1.1 < 1.10. Тип данных предположительно текстовый.

    ver_A = ver_A.split(".") ; ver_A = int(ver_A[1])
    ver_B = ver_B.split(".") ; ver_B = int(ver_B[1])

    if ver_A < ver_B: # А старше B, B новее A
        return -1
    elif ver_A > ver_B: # А новее B, B старше A
        return 1
    else:
        return 0 # версии равны


