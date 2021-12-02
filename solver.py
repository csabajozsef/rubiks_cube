from algoritmus import *

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

