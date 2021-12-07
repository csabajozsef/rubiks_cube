from cube import *

import numpy as np
"""
    A beginner-method algoritmusának lépései:
        Tartalmazza: egy berakandó cubie a helyének megtalálása majd helytől függően célpozícióba rakása

    https://cubesolve.com/rubik-kocka-kirakasa-hu/?fbclid=IwAR1V9QHqIRLmV9AY7XFY4gw4mXqWfyY4g556KynOu-R73viBLE-15oWDkW4
"""
"""
    A fehér kereszt megformálása:

"""

# Első fehér cubie berakása ( fehér-kék cubie )
def white_cross_first(c, x=-1, y=3, z=4):
    """
     A Fehér-kék cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    first = cube_method_findcolour(c, x, y, z)  # megkeressük hol a cubie
    if first[0][2] == 0:  # z szerint 1 héj

        if first[0][1] == 0:  # y szerint 1 héj
            # c.cube_method_mixer("UU")
            c.U()
            c.U()

        if first[0][1] == 1:

            if first[0][0] == 0:  # x szerinti 1 héj
                # c.cube_method_mixer("FUU")
                c.F()
                c.U()
                c.U()

            if first[0][0] == 2:
                # c.cube_method_mixer("fUU")
                c.F_r()
                c.U()
                c.U()

        if first[0][1] == 2:
            # c.cube_method_mixer("FFUU")
            c.F()
            c.F()
            c.U()
            c.U()

    if first[0][2] == 1:  # z szerint 2

        if first[0][1] == 0:  # y szerint 1

            if first[0][0] == 0:  # x szerint 1

                c.U()

            if first[0][0] == 2:
                c.U_r()

        if first[0][1] == 2:  # y szerint 2

            if first[0][0] == 0:
                # c.cube_method_mixer("LLU")
                c.L()
                c.L()
                c.U()

            if first[0][0] == 2:
                # c.cube_method_mixer("RRu")
                c.R()
                c.R()
                c.U_r()

    if first[0][2] == 2:  # z szerint 3 héj

        if first[0][1] == 0:
            pass  # ez a megfelelő pozíciója

        if first[0][1] == 1:

            if first[0][0] == 0:
                c.B_r()

            if first[0][0] == 2:
                c.B()

        if first[0][1] == 2:
            # c.cube_method_mixer("BB")
            c.B()
            c.B()

    if cube_method_good_orient(first[2], x, y,
                               z) == True:  # itt már a helyén van a kocka, de nem biztos, hogy a megfelelő orientációban

        return True

    else:

        # c.cube_method_mixer("Bru")
        c.B_r()
        c.R_r()
        c.U_r()

        return True


# Második fehér cubie berakása ( fehér-piros cubie )
def white_cross_second(c, x=1, y=3, z=-1):  # piros fehér
    """
         A Fehér-piros cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    second = cube_method_findcolour(c, x, y, z)  # megkeressük a kis cubie-t
    if second[0][2] == 0:  # z szerint 1 héj

        if second[0][1] == 0:  # y szerint 1 héj
            # c.cube_method_mixer("FR")
            c.F()
            c.R()

        if second[0][1] == 1:

            if second[0][0] == 0:
                # c.cube_method_mixer("fdRR")
                c.F()
                c.F()
                c.R()

            if second[0][0] == 2:
                c.R()

        if second[0][1] == 2:
            # c.cube_method_mixer("dRR")
            c.F_r()
            c.R()

    if second[0][2] == 1:  # z szerint első héj

        if second[0][1] == 0:

            if second[0][0] == 0:
                # c.cube_method_mixer("lFFR")
                c.L()
                c.F()
                c.F()
                c.R()

            if second[0][0] == 2:
                pass  # ez a megfelelő pozíciója

        if second[0][1] == 2:

            if second[0][0] == 0:
                # c.cube_method_mixer("DDRR")
                c.D()
                c.D()
                c.R()
                c.R()

            if second[0][0] == 2:
                # c.cube_method_mixer("RR")
                c.R()
                c.R()

    if second[0][2] == 2:

        if second[0][1] == 0:
            pass  # itt már helyén van az előző lépés általi kis cubie

        if second[0][1] == 1:

            if second[0][0] == 0:
                # c.cube_method_mixer("LDDRR")
                c.L_r()
                c.D()
                c.D()
                c.R()
                c.R()

            if second[0][0] == 2:
                c.R_r()

        if second[0][1] == 2:
            # c.cube_method_mixer("DRR")
            c.D_r()
            c.R()
            c.R()

    if cube_method_good_orient(second[2], x, y,
                               z) == True:  # itt már a helyén van a kocka, de nem biztos, hogy a megfelelő orientációban

        return True

    else:

        # c.cube_method_mixer("rrDfR")
        c.R_r()
        c.R_r()
        c.D_r()
        c.F_r()
        c.R()

        return True


# Harmadik fehér cubie berakása ( fehér-zöld cubie )
def white_cross_third(c, x=-1, y=3, z=6):
    """
        A Fehér-zöld cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    third = cube_method_findcolour(c, x, y, z)  # megkeressük hol a kis cubie
    if third[0][2] == 0:

        if third[0][1] == 0:
            pass  # a helyén van

        if third[0][1] == 1:

            if third[0][0] == 0:
                c.F()

            if third[0][0] == 2:
                c.F_r()

        if third[0][1] == 2:
            # c.cube_method_mixer("FF")
            c.F()
            c.F()

    if third[0][2] == 1:

        if third[0][1] == 0:

            if third[0][0] == 0:
                # c.cube_method_mixer("lF")
                c.L()
                c.F()

            if third[0][0] == 2:
                pass  # az előző cubie már itt van a helyén(1,3,-1)

        if third[0][1] == 2:

            if third[0][0] == 0:
                # c.cube_method_mixer("dFF")
                c.D()
                c.F()
                c.F()

            if third[0][0] == 2:
                # c.cube_method_mixer("DFF")
                c.D_r()
                c.F()
                c.F()

    if third[0][2] == 2:

        if third[0][1] == 0:
            pass  # az előző cubie-k egyike már a helyén(-1, 3, 4)

        if third[0][1] == 1:

            if third[0][0] == 0:
                # c.cube_method_mixer("LdFF")
                c.L_r()
                c.D()
                c.F()
                c.F()

            if third[0][0] == 2:
                # c.cube_method_mixer("RDrFF")
                c.R()
                c.D_r()
                c.R_r()
                c.F()
                c.F()

        if third[0][1] == 2:
            # c.cube_method_mixer("DDFF")
            c.D()
            c.D()
            c.F()
            c.F()

    if cube_method_good_orient(third[2], x, y,
                               z) == True:  # itt már a helyén van a kocka, de nem biztos, hogy a megfelelő orientációban

        return True

    else:

        # c.cube_method_mixer("fldFF")
        c.F_r()
        c.L()
        c.D()
        c.F()
        c.F()

        return True


# negyedik fehér cubie berakása ( fehér-narancs cubie )
def white_cross_fourth(c, x=5, y=3, z=-1):
    """
            A Fehér-narancs cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    fourth = cube_method_findcolour(c, x, y, z)  # megkersessük a cubie-t
    if fourth[0][2] == 0:

        if fourth[0][1] == 0:
            pass  # megfelelő helyen van már egy előző cubie (-1,3,6)

        if fourth[0][1] == 1:

            if fourth[0][0] == 0:
                c.L_r()

            if fourth[0][0] == 2:
                # c.cube_method_mixer("fflFF")
                c.F_r()
                c.F_r()
                c.L_r()
                c.F()
                c.F()

        if fourth[0][1] == 2:
            # c.cube_method_mixer("DLL")
            c.D_r()
            c.L()
            c.L()

    if fourth[0][2] == 1:

        if fourth[0][1] == 0:

            if fourth[0][0] == 0:
                pass  # itt a megfelelő helyen van

            if fourth[0][0] == 2:
                pass  # itt (1,3,-1) van a helyén

        if fourth[0][1] == 2:

            if fourth[0][0] == 0:
                # c.cube_method_mixer("LL")
                c.L()
                c.L()

            if fourth[0][0] == 2:
                # c.cube_method_mixer("DDLL")
                c.D()
                c.D()
                c.L()
                c.L()

    if fourth[0][2] == 2:

        if fourth[0][1] == 0:
            pass

        if fourth[0][1] == 1:

            if fourth[0][0] == 0:
                c.L()

            if fourth[0][0] == 2:
                # c.cube_method_mixer("BdLLb")
                c.B_r()
                c.D()
                c.L()
                c.L()
                c.B()

        if fourth[0][1] == 2:
            # c.cube_method_mixer("dLL")
            c.D()
            c.L()
            c.L()

    if cube_method_good_orient(fourth[2], x, y,
                               z) == True:  # itt már a helyén van a kocka, de nem biztos, hogy a megfelelő orientációban

        return True

    else:

        # c.cube_method_mixer("LLdFLf")
        c.L()
        c.L()
        c.D()
        c.F()
        c.L_r()
        c.F_r()

        return True


"""
    A fehér oldal sarkainak berakása
"""


# ötödik fehér cubie berakása ( fehér-zöld-piros cubie )
def cube_method_firstcorner(c, x=1, y=3, z=6):
    """
        A Fehér-zöld-piros cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    first = cube_method_findcolour(c, x, y, z)  # megkeressük, hol van
    if first[0][2] == 2:

        if first[0][1] == 0:

            if first[0][0] == 0:
                # c.cube_method_mixer("LDDl")
                c.L_r()
                c.D()
                c.D()
                c.L()

            if first[0][0] == 2:
                # c.cube_method_mixer("Rdrdd")
                c.R()
                c.D()
                c.R_r()
                c.D_r()
                c.D_r()

        if first[0][1] == 2:

            if first[0][0] == 0:
                # c.cube_method_mixer("DD")
                c.D()
                c.D()

            if first[0][0] == 2:
                c.D_r()

    if first[0][2] == 0:

        if first[0][1] == 0:

            if first[0][0] == 0:
                # c.cube_method_mixer("ldL")
                c.L()
                c.D()
                c.L_r()

            if first[0][0] == 2:
                pass  # itt lesz a megfelelő helyen

        if first[0][1] == 2:

            if first[0][0] == 0:
                c.D()

            if first[0][0] == 2:
                # c.cube_method_mixer("DrdR")
                c.D_r()
                c.R_r()
                c.D()
                c.R()

    first = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel
    while cube_method_good_orient(first[2], x, y,
                                  z) == False:  # itt addig végzi el ezt a forgatás sorozatot amíg be nem fordul a megfelelő orientációban
        # c.cube_method_mixer("rDRDDFDf")
        c.R_r()
        c.D_r()
        c.R()
        c.D()
        first = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel
    return True


# hatodik fehér cubie berakása ( fehér-zöld-narancs cubie )
def cube_method_secondcorner(c, x=5, y=3, z=6):
    """
            A Fehér-zöld-narancs cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    second = cube_method_findcolour(c, x, y, z)  # itt megkeressük
    if second[0][2] == 2:

        if second[0][1] == 0:

            if second[0][0] == 0:
                # c.cube_method_mixer("bdB")
                c.B()
                c.D()
                c.B_r()

            if second[0][0] == 2:
                # c.cube_method_mixer("Bddb")
                c.B_r()
                c.D()
                c.D()
                c.B()

        if second[0][1] == 2:

            if second[0][0] == 0:
                c.D()

            if second[0][0] == 2:
                # c.cube_method_mixer("DD")
                c.D()
                c.D()
                c.D()
                c.L()
                c.D_r()
                c.L_r()

    if second[0][2] == 0:

        if second[0][1] == 0:

            if second[0][0] == 0:
                pass  # itt a megfelelő helyen van

            if second[0][0] == 2:
                pass  # (1,3,6) cubie

        if second[0][1] == 2:

            if second[0][0] == 2:
                # c.cube_method_mixer("lDL")
                c.L()
                c.D_r()
                c.L_r()
                c.D()
                c.L()
                c.D_r()
                c.L_r()

            if second[0][0] == 0:
                # c.cube_method_mixer("blDL")
                c.D()
                c.L()
                c.D_r()
                c.L_r()

    second = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel
    while cube_method_good_orient(second[2], x, y,
                                  z) != True:  # itt addig végzi el ezt a forgatás sorozatot amíg be nem fordul a megfelelő orientációban
        # c.cube_method_mixer("lDLdlDL")
        c.L()
        c.D()
        c.L_r()
        c.D_r()
        second = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel

    return True


def cube_method_thirdcorner(c, x=5, y=3, z=4):
    """
                A Fehér-zöld-narancs cubie megkeresése majd helyre rakása, végül megfelelő orientációba rakás
    """
    third = cube_method_findcolour(c, x, y, z)  # megkeressük
    if third[0][2] == 0:

        if third[0][1] == 0:

            if third[0][0] == 0:
                pass

            if third[0][0] == 2:
                pass

        if third[0][1] == 2:

            if third[0][0] == 0:
                c.D_r()
                c.D()
                c.B()
                c.D_r()
                c.B_r()

            if third[0][0] == 2:
                # c.cube_method_mixer("DD")
                c.D_r()
                c.D_r()
                c.D()
                c.B()
                c.D_r()
                c.B_r()

    if third[0][2] == 2:

        if third[0][1] == 0:

            if third[0][0] == 0:
                pass

            if third[0][0] == 2:
                # c.cube_method_mixer("Rdr")
                c.R()
                c.D()
                c.R_r()
                c.D()
                c.B()
                c.D_r()
                c.B_r()

        if third[0][1] == 2:

            if third[0][0] == 2:
                c.D()
                c.D()
                c.B()
                c.D_r()
                c.B_r()

            if third[0][0] == 0:
                # c.cube_method_mixer("dbDB")
                c.D()
                c.B()
                c.D_r()
                c.B_r()

    third = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel

    while cube_method_good_orient(third[2], x, y,
                                  z) != True:  # addig csináljuk ez a forgatási sorozatot míg a megfelelő orient-ben nem lesz
        # c.cube_method_mixer("bDBdbDB")
        c.B()
        c.D()
        c.B_r()
        c.D_r()

        third = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel

    return True


def cube_method_fourthcorner(c, x=1, y=3, z=4):
    """
        A Fehér-Piros-kék cubie helyrerakása
    """
    fourth = cube_method_findcolour(c, x, y, z)  # megkeressük
    if fourth[0][2] == 0:

        if fourth[0][1] == 0:

            if fourth[0][0] == 0:
                pass  # (5,3,6) cubie

            if fourth[0][0] == 2:
                pass  # (1,3,6) cubie

        if fourth[0][1] == 2:

            if fourth[0][0] == 0:
                # c.cube_method_mixer("DD")
                c.D_r()
                c.D_r()
                c.D()
                c.R()
                c.D_r()
                c.R_r()

            if fourth[0][0] == 2:
                c.D()
                c.D()
                c.R()
                c.D_r()
                c.R_r()

    if fourth[0][2] == 2:

        if fourth[0][1] == 0:

            if fourth[0][0] == 0:
                pass  # itt a helyén van

            if fourth[0][0] == 2:
                pass  # (1,3,4) cubie

        if fourth[0][1] == 2:

            if fourth[0][0] == 0:
                c.D_r()
                c.D()
                c.R()
                c.D_r()
                c.R_r()

            if fourth[0][0] == 2:
                # c.cube_method_mixer("dRdr")
                c.D()
                c.R()
                c.D_r()
                c.R_r()

    fourth = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel
    while cube_method_good_orient(fourth[2], x, y, z) != True:  # addig forgatjuk amíg megfelelő orient-ben nem lesz
        # c.cube_method_mixer("BDbdBDb")
        c.B_r()
        c.D_r()
        c.B()
        c.D()
        fourth = cube_method_findcolour(c, x, y, z)  # forgatások után megnézzük újra hol van és milyen orient-tel

    return True


def cube_method_middle1(c, x=5, y=-1, z=6):
    """
        A Zöld-narancs cubie-helyrerakása (előtte fejrefordítottuk a kockát) (sárga felül)
    """

    c.cube_method_flipper("x")  # itt forgatjuk át sárga felsőre zöld elülső oldalra
    c.cube_method_flipper("x")
    c.cube_method_flipper("y")
    c.cube_method_flipper("y")

    first = cube_method_findcolour(c, x, y, z)  # megkeressük a cubie-t

    if first[0][1] == 1:

        if first[0][2] == 0:

            if first[0][0] == 0:

                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

            elif first[0][0] == 2:

                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

        elif first[0][2] == 2:  # ha hátul van akkor előre fordítjuk a hátsó oldalt

            if first[0][0] == 0:
                c.cube_method_flipper("y")  # ezzel forítjuk előre
                c.cube_method_flipper("y")

                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

                c.cube_method_flipper("y")  # visszafordítjuk
                c.cube_method_flipper("y")
            elif first[0][0] == 2:
                c.cube_method_flipper("y")  # ezzel forítjuk előre
                c.cube_method_flipper("y")

                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

                c.cube_method_flipper("y")  # visszafordítjuk
                c.cube_method_flipper("y")

    first = cube_method_findcolour(c, x, y, z)  # lelellenőrízzük a helyét is orientációját
    if first[0][1] == 0:

        if first[0][0] == 0:
            c.U_r()

        if first[0][0] == 1:

            if first[0][2] == 0:
                pass

            if first[0][2] == 2:
                c.U()
                c.U()

        if first[0][0] == 2:
            c.U()

    c.U()  # a felső sorból a helyére forgatjuk
    c.R()
    c.U_r()
    c.R_r()
    c.U_r()
    c.F_r()
    c.U()
    c.F()

    first = cube_method_findcolour(c, x, y, z)  # ellenőrízzük a helyét és orient-tet
    if cube_method_good_orient(first[2], x, y, z) == True:  # megfelelő orientációba forgatjuk

        return True

    else:
        c.U()
        c.R()
        c.U_r()
        c.R_r()
        c.U_r()
        c.F_r()
        c.U()
        c.F()
        c.U_r()
        c.R()
        c.U_r()
        c.R_r()
        c.U_r()
        c.F_r()
        c.U()
        c.F()

        return True


def cube_method_middle2(c, x=1, y=-1, z=6):
    """
        A Piros-zöld helyrerakása az előzző middle-ös alapján
    """

    second = cube_method_findcolour(c, x, y, z)  # megkeressük

    if second[0][1] == 1:

        if second[0][2] == 0:

            if second[0][0] == 0:
                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

            if second[0][0] == 2:
                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

        if second[0][2] == 2:

            if second[0][0] == 0:
                c.cube_method_flipper("y")  # ha hátulva előre forgatjuk
                c.cube_method_flipper("y")

                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

                c.cube_method_flipper("y")  # visszaforgatjuk
                c.cube_method_flipper("y")

            if second[0][0] == 2:
                c.cube_method_flipper("y")  # előreforgatjuk
                c.cube_method_flipper("y")

                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

                c.cube_method_flipper("y")  # visszaforgatjuk
                c.cube_method_flipper("y")

    second = cube_method_findcolour(c, x, y, z)  # ellenőrzünk
    if second[0][1] == 0:

        if second[0][0] == 0:
            c.U_r()

        if second[0][0] == 1:

            if second[0][2] == 1:
                pass

            if second[0][2] == 2:
                c.U()
                c.U()

        if second[0][0] == 2:
            c.U()

    c.U_r()
    c.L_r()
    c.U()
    c.L()
    c.U()
    c.F()
    c.U_r()
    c.F_r()

    second = cube_method_findcolour(c, x, y, z)
    if cube_method_good_orient(second[2], x, y, z) == True:  # megfelelő orentációba forgatjuk, ha kell

        return True

    else:

        c.U_r()
        c.L_r()
        c.U()
        c.L()
        c.U()
        c.F()
        c.U_r()
        c.F_r()
        c.U()
        c.L_r()
        c.U()
        c.L()
        c.U()
        c.F()
        c.U_r()
        c.F_r()
        c.U_r()

        return True


def cube_method_middle3(c, x=1, y=-1, z=4):
    """
        A piros-kék helyrerakása, először a kék oldalt előre forgatjuk
    """

    c.cube_method_flipper("y")  # itt forgatjuk előre
    c.cube_method_flipper("y")

    third = cube_method_findcolour(c, x, y, z)  # megkeressük

    if third[0][1] == 1:

        if third[0][2] == 0:

            if third[0][0] == 0:
                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

            if third[0][0] == 2:
                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

        if third[0][2] == 2:

            if third[0][0] == 0:
                c.cube_method_flipper("y")  # ha előlről htára forgatjuk
                c.cube_method_flipper("y")

                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

                c.cube_method_flipper("y")  # visszaforgatjuk
                c.cube_method_flipper("y")

            if third[0][0] == 2:
                c.cube_method_flipper("y")  # előre forgatjuk
                c.cube_method_flipper("y")

                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

                c.cube_method_flipper("y")  # visszaforgatjuk
                c.cube_method_flipper("y")

    third = cube_method_findcolour(c, x, y, z)  # ellenőrzünk
    if third[0][1] == 0:

        if third[0][0] == 0:
            c.U_r()

        if third[0][0] == 1:

            if third[0][2] == 1:
                pass

            if third[0][2] == 2:
                c.U()
                c.U()

        if third[0][0] == 2:
            c.U()

    c.U()  # felsősorból helyére forgatjuk
    c.R()
    c.U_r()
    c.R_r()
    c.U_r()
    c.F_r()
    c.U()
    c.F()

    third = cube_method_findcolour(c, x, y, z)  # ellenőrzünk
    if cube_method_good_orient(third[2], x, y, z) == True:  # megfelelő orientációba forgatjuk, ha kell

        return True

    else:

        c.U()
        c.R()
        c.U_r()
        c.R_r()
        c.U_r()
        c.F_r()
        c.U()
        c.F()
        c.U_r()
        c.R()
        c.U_r()
        c.R_r()
        c.U_r()
        c.F_r()
        c.U()
        c.F()

        return True


def cube_method_middle4(c, x=5, y=-1, z=4):
    """
        A narancs-kék helyére forgatása
    """

    fourth = cube_method_findcolour(c, x, y, z)  # ellemőrizzük

    if fourth[0][1] == 1:

        if fourth[0][2] == 0:

            if fourth[0][0] == 0:
                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

            if fourth[0][0] == 2:
                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

        if fourth[0][2] == 2:

            # c.cube_method_flipper("y")
            # c.cube_method_flipper("y")

            if fourth[0][0] == 0:
                c.cube_method_flipper("y")  # ha hátul van előre forgatjuk
                c.cube_method_flipper("y")

                c.U()
                c.R()
                c.U_r()
                c.R_r()
                c.U_r()
                c.F_r()
                c.U()
                c.F()

                c.cube_method_flipper("y")  # visszaforgatjuk
                c.cube_method_flipper("y")
            if fourth[0][0] == 2:
                c.cube_method_flipper("y")  # előre forgatjuk
                c.cube_method_flipper("y")

                c.U_r()
                c.L_r()
                c.U()
                c.L()
                c.U()
                c.F()
                c.U_r()
                c.F_r()

                c.cube_method_flipper("y")  # hátra forgatjuk
                c.cube_method_flipper("y")

    fourth = cube_method_findcolour(c, x, y, z)  # ellenőrzünk
    if fourth[0][1] == 0:

        if fourth[0][0] == 0:
            c.U_r()

        if fourth[0][0] == 1:

            if fourth[0][2] == 1:
                pass

            if fourth[0][2] == 2:
                c.U()
                c.U()

        if fourth[0][0] == 2:
            c.U()

    c.U_r()
    c.L_r()
    c.U()
    c.L()
    c.U()
    c.F()
    c.U_r()
    c.F_r()

    fourth = cube_method_findcolour(c, x, y, z)  # ellenőrzünk
    if cube_method_good_orient(fourth[2], x, y, z) == True:  # helyére forgatjuk

        return True

    else:
        c.U_r()
        c.L_r()
        c.U()
        c.L()
        c.U()
        c.F()
        c.U_r()
        c.F_r()
        c.U()
        c.L_r()
        c.U()
        c.L()
        c.U()
        c.F()
        c.U_r()
        c.F_r()

        return True


def cube_method_yellow_cross(c, p=[[1, 0, 0], [2, 0, 1], [1, 0, 2]]):
    """
        A sárga kereszt helyére rakása ennek a három cubie ellenőrzésével majd helyére rakásával
    """
    upperfirstmiddle = cube_method_which_colour(c, p[0])  # ezek a keresett cubiek színeit nézik
    uppersecondright = cube_method_which_colour(c, p[1])
    upperbackmiddle = cube_method_which_colour(c, p[2])

    if upperfirstmiddle[2][1] == 2:

        if uppersecondright[2][1] == 2:

            if upperbackmiddle[2][1] == 2:
                return True

            else:
                c.U()
                c.U()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True

        else:

            if upperbackmiddle[2][1] == 2:
                c.U()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True

            else:
                c.U()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True
    else:

        if uppersecondright[2][1] == 2:

            if upperbackmiddle[2][1] == 2:
                c.U_r()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True

            else:
                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True

        else:

            if upperbackmiddle[2][1] == 2:
                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                return True

            else:
                c.F()
                c.R()
                c.U()
                c.R_r()
                c.U_r()
                c.F_r()

                cube_method_yellow_cross(
                    c)  # ha ide fut be azt jelenti, hogy a sárga keresztből csak a középső van a helyén, ezen forgatási sorozat után már lesz egy L alak, így rekurzívan meghívva a függvényt, már kirakja ( nem lesz végtelen ciklus)

                return True


p = ['100', '201', '102']


def cube_method_fifth_step1(c, p=[[1, 0, 0], [0, 0, 1], [1, 0, 2]]):
    """
        A Sárga lap kék-sárga keresztben lévő cubie helyrerakása
    """
    upperfirstmiddle = cube_method_which_colour(c, p[0])  # ezen cubiek segítségével
    uppersecondleft = cube_method_which_colour(c, p[1])
    upperbackmiddle = cube_method_which_colour(c, p[2])

    if upperfirstmiddle[2][2] == 4:

        return True  # itt ha a helyén van

    else:

        if uppersecondleft[2][0] == 4:

            c.R()
            c.U()
            c.R_r()
            c.U()
            c.R()
            c.U()
            c.U()
            c.R_r()
            c.U()

            return True

        else:
            if upperbackmiddle[2][2] == 4:

                c.R()
                c.U()
                c.R_r()
                c.U()
                c.R()
                c.U()
                c.U()
                c.R_r()
                c.U()

                c.cube_method_flipper("y")
                c.cube_method_flipper("y")

                c.U()

                c.cube_method_flipper("y")
                c.cube_method_flipper("y")
                c.cube_method_flipper("y")

                c.R()
                c.U()
                c.R_r()
                c.U()
                c.R()
                c.U()
                c.U()
                c.R_r()
                c.U()

                c.cube_method_flipper("y")
                c.cube_method_flipper("y")
                c.cube_method_flipper("y")

                return True

            else:

                if cube_method_good_orient(cube_method_which_colour(c, [2, 0, 1])[2], 4, 2,
                                           -1):  # itt egy gyorsító lépés

                    c.U()
                else:

                    c.cube_method_flipper("y")
                    c.cube_method_flipper("y")
                    c.cube_method_flipper("y")

                    c.R()
                    c.U()
                    c.R_r()
                    c.U()
                    c.R()
                    c.U()
                    c.U()
                    c.R_r()
                    c.U()

                    c.cube_method_flipper("y")

                    return True


p = ['100', '201', '102']


def cube_method_fifth_step2(c, p=[[1, 0, 0], [0, 0, 1]]):
    """
        A Sárga-narancs cubie helyérerakása
    """

    c.cube_method_flipper("y")  # forgatjuk, hogy a megfelelő oldal elülre kerüljön
    c.cube_method_flipper("y")
    c.cube_method_flipper("y")

    upperfirstmiddle = cube_method_which_colour(c, p[0])
    uppersecondleft = cube_method_which_colour(c, p[1])

    if upperfirstmiddle[2][2] == 5:

        return True  # helyén van

    else:

        if uppersecondleft[2][0] == 5:
            c.R()
            c.U()
            c.R_r()
            c.U()
            c.R()
            c.U()
            c.U()
            c.R_r()
            c.U()

            return True

        else:

            c.cube_method_flipper("y")

            c.R()
            c.U()
            c.R_r()
            c.U()
            c.R()
            c.U()
            c.U()
            c.R_r()
            c.U()

            c.cube_method_flipper("y")
            c.cube_method_flipper("y")
            c.cube_method_flipper("y")

            c.R()
            c.U()
            c.R_r()
            c.U()
            c.R()
            c.U()
            c.U()
            c.R_r()
            c.U()

            c.U()
            c.U()

            return True
    c.cube_method_flipper("y")  # visszaforgatás kezdő pozícióba


def cube_method_fifth_step3(c, string1=[1, 0, 0]):
    """
        A zöld-sárga cubie helyére forgatása
    """
    c.cube_method_flipper("y")  # megfelelő oldalt elülre forgatjuk
    c.cube_method_flipper("y")
    c.cube_method_flipper("y")
    upperfirstmiddle = cube_method_which_colour(c, string1)  # ezen cubie segítségével

    if upperfirstmiddle[2][2] == 6:

        pass

    else:
        c.R()
        c.U()
        c.R_r()
        c.U()
        c.R()
        c.U()
        c.U()
        c.R_r()
        c.U()

        return True


"""
    A Sárga kereszt kész úgy, hogy az oldalsó színek is a helyén vannak
"""

dict_of_color_num = {"R": 1, "Y": 2, "W": 3, "B": 4, "O": 5, "G": 6}


def cube_method_sixth_step(c):
    """
        Sárga sarok cubie-k helyükre tevése, de még az orentáció nem biztos, hogy helyes
    """
    # minden alkalommal amikor cube_method_get_cubie_pos_name_color-t használjuk akkor lekérdezzük ezen cubiek adatait [2,0,0], [0, 0, 0]

    l0 = c.cube_method_get_cubie_pos_name_color()
    sixth1 = l0[18][2]
    sixth2 = l0[0][2]

    if cube_method_findcolourbool(sixth1, 5, 2, 6):

        if cube_method_findcolourbool(sixth2, 1, 2, 6):

            return True  # mind a négy jó helyen van mivel ha kettő jo helyen van akkor az összes

        else:

            c.U()
            c.R()
            c.U_r()
            c.L_r()
            c.U()
            c.R_r()
            c.U_r()
            c.L()

            l1 = c.cube_method_get_cubie_pos_name_color()
            sixth3 = l1[0][2]

            if cube_method_findcolourbool(sixth3, 1, 2, 6):
                return True

            else:
                # mind a négy jó helyen van mivel ha kettő jo helyen van akkor az összes
                c.U()
                c.R()
                c.U_r()
                c.L_r()
                c.U()
                c.R_r()
                c.U_r()
                c.L()

                if len(cubie_checkingbool(c, [([2, 0, 0], np.array([5, 2, 6])), ([2, 0, 2], np.array([5, 2, 4])),
                                              ([0, 0, 0], np.array([1, 2, 6])),
                                              ([0, 0, 2], np.array([1, 2, 4]))])) != 0:
                    c.U()
                    c.R()
                    c.U_r()
                    c.L_r()
                    c.U()
                    c.R_r()
                    c.U_r()
                    c.L()

                return True

    else:

        end = False

        while end == False:  # ez azért while ciklus, mivel lehet, hogy nem lesz mind a helyén így meg le kell futattni az
            c.cube_method_flipper("y")
            l2 = c.cube_method_get_cubie_pos_name_color()
            sixth4 = l2[18][2]
            sixth5 = l2[0][2]

            if cube_method_findcolourbool(sixth4, 4, 2, 5):

                if cube_method_findcolourbool(sixth5, 6, 2, 5):

                    c.cube_method_flipper("y")
                    c.cube_method_flipper("y")
                    c.cube_method_flipper("y")

                    end = True

                else:

                    c.U()
                    c.R()
                    c.U_r()
                    c.L_r()
                    c.U()
                    c.R_r()
                    c.U_r()
                    c.L()

                    l3 = c.cube_method_get_cubie_pos_name_color()
                    sixth6 = l3[0][2]

                    if cube_method_findcolourbool(sixth6, 5, 2, 6):

                        c.cube_method_flipper("y")
                        c.cube_method_flipper("y")
                        c.cube_method_flipper("y")

                        end = True

                    else:

                        c.U()
                        c.R()
                        c.U_r()
                        c.L_r()
                        c.U()
                        c.R_r()
                        c.U_r()
                        c.L()

                        c.cube_method_flipper("y")
                        c.cube_method_flipper("y")
                        c.cube_method_flipper("y")

                        cube_method_sixth_step(
                            c)  # itt újra meg kell hívni mivel, azon cubie-k helyét is meg kell nézni, amelyeket az else ág előtt kezeltünk, de nem romlik az állapot így nem lesz végtelen ciklus

            else:

                c.cube_method_flipper("y")
                l4 = c.cube_method_get_cubie_pos_name_color()
                sixth7 = l4[18][2]
                sixth8 = l4[0][2]

                if cube_method_findcolourbool(sixth7, 1, 2, 4):

                    if cube_method_findcolourbool(sixth8, 5, 2, 4):

                        c.cube_method_flipper("y")
                        c.cube_method_flipper("y")

                        end = True

                    else:

                        c.U()
                        c.R()
                        c.U_r()
                        c.L_r()
                        c.U()
                        c.R_r()
                        c.U_r()
                        c.L()

                        l5 = c.cube_method_get_cubie_pos_name_color()
                        sixth9 = l5[0][2]

                        if cube_method_findcolourbool(sixth9, 5, 2, 4):

                            c.cube_method_flipper("y")
                            c.cube_method_flipper("y")

                            end = True

                        else:

                            c.U()
                            c.R()
                            c.U_r()
                            c.L_r()
                            c.U()
                            c.R_r()
                            c.U_r()
                            c.L()

                            c.cube_method_flipper("y")
                            c.cube_method_flipper("y")

                            cube_method_sixth_step(
                                c)  # itt újra meg kell hívni mivel, azon cubie-k helyét is meg kell nézni, amelyeket az else ág előtt kezeltünk, de nem romlik az állapot így nem lesz végtelen ciklus


                else:

                    c.cube_method_flipper("y")
                    l6 = c.cube_method_get_cubie_pos_name_color()
                    sixth10 = l6[18][2]

                    if cube_method_findcolourbool(sixth10, 4, 2, 1):

                        c.U()
                        c.R()
                        c.U_r()
                        c.L_r()
                        c.U()
                        c.R_r()
                        c.U_r()
                        c.L()

                        c.cube_method_flipper("y")

                        cube_method_sixth_step(
                            c)  # itt újra meg kell hívni mivel, azon cubie-k helyét is meg kell nézni, amelyeket az else ág előtt kezeltünk, de nem romlik az állapot így nem lesz végtelen ciklus


                    else:
                        c.U()
                        c.R()
                        c.U_r()
                        c.L_r()
                        c.U()
                        c.R_r()
                        c.U_r()
                        c.L()

                        c.cube_method_flipper(
                            "y")  # ezen végső forgatással egy helyére kerül, de újra kell ellenőrizni, hogy végül mind a neégy helyére kerüljön

    return end


def cube_method_seventh_step(c):
    """
        A Sárga sarok kockák megfelelő orientációba tevése

    """

    counter = 0
    while counter <= 4:  # azért while, hogy addig csinálja míg mind a négy helyére nem kerül
        if yellow(c):

            counter += 1
            c.U()

        else:

            c.R_r()
            c.D_r()
            c.R()
            c.D()

    c.U_r()

    if counter == 4:
        return True

# ([2, 0, 2], np.array([1, 3, 4])), ([2, 0, 0], np.array([1, 3, 6])),([0, 0, 0], '000', array([5, 3, 6])) , ([1, 0, 2], np.array([-1,  3,  4])), ([0, 0, 2], np.array([5, 3, 4])), ([2, 0, 1], np.array([ 1,  3, -1])), ([1, 0, 0], np.array([-1,  3,  6])), ([0, 0, 1], np.array([ 5,  3, -1]))])
# ([0, 0, 0], np.array([5, 3, 6]))
# ([2, 0, 0], np.array([1, 3, 6])),
# ([2, 0, 2], np.array([1, 3, 4])), ([0, 0, 2], np.array([5, 3, 4]))
# ([2, 1, 0], np.array([ 1, -1,  6])), ([0, 1, 2], np.array([ 5, -1,  4])),
# ([2, 1, 2], np.array([1, -1,  4]))
# ([2, 0, 0], np.array([5, 2, 6]))
# ([2, 0, 2], np.array([5, 2, 4]))
# ([0, 0, 0], np.array([1, 2, 6]))([0, 0, 2], np.array([1, 2, 4]))



def cube_solver(c):
    white_cross_first(c)
    white_cross_second(c)
    white_cross_third(c)
    white_cross_fourth(c)
    cube_method_firstcorner(c)
    cube_method_secondcorner(c)
    cube_method_thirdcorner(c)
    cube_method_fourthcorner(c)
    cube_method_middle1(c)
    cube_method_middle2(c)
    cube_method_middle3(c)
    cube_method_middle4(c)
    cube_method_yellow_cross(c)
    cube_method_fifth_step1(c)
    cube_method_fifth_step2(c)
    cube_method_fifth_step3(c)
    cube_method_sixth_step(c)
    cube_method_seventh_step(c)

    c.cube_method_flipper("y")
    c.cube_method_flipper("y")
    c.cube_method_flipper("x")
    c.cube_method_flipper("x")
