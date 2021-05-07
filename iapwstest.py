import copy

from iapws import IAPWS97
"""
    T : float
        Temperature, [K]
    P : float
        Pressure, [MPa]
    h : float
        Specific enthalpy, [kJ/kg]
    s : float
        Specific entropy, [kJ/kgK]
    x : float
        Vapor quality, [-]
    l : float, optional
        Wavelength of light, for refractive index, [nm]
        The calculated instance has the following properties:

            * P: Pressure, [MPa]
            * T: Temperature, [K]
            * g: Specific Gibbs free energy, [kJ/kg]
            * a: Specific Helmholtz free energy, [kJ/kg]
            * v: Specific volume, [m³/kg]
            * rho: Density, [kg/m³]
            * h: Specific enthalpy, [kJ/kg]
            * u: Specific internal energy, [kJ/kg]
            * s: Specific entropy, [kJ/kg·K]
            * cp: Specific isobaric heat capacity, [kJ/kg·K]
            * cv: Specific isochoric heat capacity, [kJ/kg·K]
            * Z: Compression factor, [-]
            * fi: Fugacity coefficient, [-]
            * f: Fugacity, [MPa]

            * gamma: Isoentropic exponent, [-]
            * alfav: Isobaric cubic expansion coefficient, [1/K]
            * xkappa: Isothermal compressibility, [1/MPa]
            * kappas: Adiabatic compresibility, [1/MPa]
            * alfap: Relative pressure coefficient, [1/K]
            * betap: Isothermal stress coefficient, [kg/m³]
            * joule: Joule-Thomson coefficient, [K/MPa]
            * deltat: Isothermal throttling coefficient, [kJ/kg·MPa]
            * region: Region

            * v0: Ideal specific volume, [m³/kg]
            * u0: Ideal specific internal energy, [kJ/kg]
            * h0: Ideal specific enthalpy, [kJ/kg]
            * s0: Ideal specific entropy, [kJ/kg·K]
            * a0: Ideal specific Helmholtz free energy, [kJ/kg]
            * g0: Ideal specific Gibbs free energy, [kJ/kg]
            * cp0: Ideal specific isobaric heat capacity, [kJ/kg·K]
            * cv0: Ideal specific isochoric heat capacity [kJ/kg·K]
            * w0: Ideal speed of sound, [m/s]
            * gamma0: Ideal isoentropic exponent, [-]

            * w: Speed of sound, [m/s]
            * mu: Dynamic viscosity, [Pa·s]
            * nu: Kinematic viscosity, [m²/s]
            * k: Thermal conductivity, [W/m·K]
            * alfa: Thermal diffusivity, [m²/s]
            * sigma: Surface tension, [N/m]
            * epsilon: Dielectric constant, [-]
            * n: Refractive index, [-]
            * Prandt: Prandtl number, [-]
            * Pr: Reduced Pressure, [-]
            * Tr: Reduced Temperature, [-]
            * Hvap: Vaporization heat, [kJ/kg]
            * Svap: Vaporization entropy, [kJ/kg·K]

    Examples  Liquid:液体 Vapor:蒸汽
    --------
    >>> water=IAPWS97(T=170+273.15, x=0.5)
    >>> water.Liquid.cp, water.Vapor.cp, water.Liquid.w, water.Vapor.w
    4.3695 2.5985 1418.3 498.78

    >>> water=IAPWS97(T=325+273.15, x=0.5)
    >>> water.P, water.Liquid.v, water.Vapor.v, water.Liquid.h, water.Vapor.h
    12.0505 0.00152830 0.0141887 1493.37 2684.48

    >>> water=IAPWS97(T=50+273.15, P=0.0006112127)
    >>> water.cp0, water.cv0, water.h0, water.s0, water.w0
    1.8714 1.4098 2594.66 9.471 444.93
"""

# water = IAPWS97(T=500.0+273.15,P=29.0)
# #water = IAPWS97(P=20.0,h=800)
# #water = IAPWS97(P=20.0,s=6.7)
# #water = IAPWS97(P=20.0,x=1.0)
# #water = IAPWS97(P=20.0,x=0.5)
# #water = IAPWS97(T=200.0+273.15,h=2200.0) 当前版本暂不支持
# #water = IAPWS97(T=200.0+273.15,s=6.7) 当前版本暂不支持
# #water = IAPWS97(T=200.0+273.15,x=0.5)
# #print(water.T-273.15)
# #print(water.P)
# #print(water.x)
# # print(water.v)
# #print(water.h)
# #print(water.s)
# print(water.cp)
# print(water.cv)
##############################################        装饰器        ########################################################

def except_decorate_N273(func):
    def inner(*args,**kwargs):
        try:
            res = func(*args,**kwargs)
            return res
        except Exception as e:
            res = ' 输出:{}, 错误原因:{}.'.format(-273.5,e)
            return res
    return inner


def except_decorate_N0(func):
    def inner(*args,**kwargs):

        try:
            res = func(*args,**kwargs)
            return res
        except Exception as e:
            res = ' 输出:{}, 错误原因:{}.'.format(0, e)
            return res

    return inner
def except_decorate_N_1(func):


    def inner(*args,**kwargs):

        try:
            res = func(*args,**kwargs)
            return res
        except Exception as e:
            res = ' 输出:{}, 错误原因:{}.'.format(-1, e)
            return res

    return inner





#############################################################   计算函数    ####################################################

#由压力和焓值求温度
@except_decorate_N273
def AphT(P,h):
    #返回单位  摄氏度
    #所有区
    res = IAPWS97(P=P,h=h).T
    return  res





#由压力和熵值求温度
@except_decorate_N273
def ApsT(P,s):
    #所有区
    res = IAPWS97(P=P, s=s).T - 273.15
    return  res




#由温度和焓值求压力
@except_decorate_N0
def AthP(T,h):
    pass


#由温度和压力求定压热容
@except_decorate_N0
def AtpCp(T,P):
    #除饱和区的其它区
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).cp
    return  res



#由温度和压力求定容热容
@except_decorate_N0
def AtpCv(T,P):
    #除饱和区的其它区
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).cv
    return  res




#由温度和压力求焓值
@except_decorate_N0
def AtpH(T,P):
    #除饱和区的其它区
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).h
    return res



#由温度和压力求熵值
@except_decorate_N0
def AtpS(T,P):
    #除饱和区的其它区
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).s
    return res




# 由温度和熵值求压力
def AtsP(T,s):
    pass




#由温度和压力求比容
@except_decorate_N0
def AtpV(T,P):
    #所有区
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).v
    return res



#由温度和压力计算水的焓值
@except_decorate_N0
def ftpH(T,P):
    #水区，f表示fluid
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).v
    return res




#由温度和压力计算水的熵值
@except_decorate_N0
def ftpS(T,P):
    #水区，f表示fluid
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).s
    return res





#由温度和压力计算水的熵值
@except_decorate_N0
def gtpH(T,P):
    #汽区，f表示gas
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).h
    return res




#由温度和压力计算汽的焓值
@except_decorate_N0
def gtpS(T,P):
    #汽区，f表示gas
    T = T +273.15
    res  =  IAPWS97(T=T,P=P).s
    return res




#由温度和压力计算汽的熵值
@except_decorate_N_1
def phA_P(P,h):
    #所有区
    res = IAPWS97(P=P,h=h).P
    return  res



#由温度和压力计算汽的熵值
@except_decorate_N_1
def phA_x(P,h):
    #所有区
    res = IAPWS97(P=P,h=h).x
    return  res



#由压力和焓值求焓值
@except_decorate_N_1
def phA_h(P,h):
    #所有区
    res = IAPWS97(P=P,h=h).h
    return  res





#由压力和焓值求熵值
@except_decorate_N_1
def phA_s(P,h):
    #所有区
    res = IAPWS97(P=P,h=h).s
    return  res



#由压力和熵值求压力
@except_decorate_N_1
def psA_P(P,s):
    #所有区
    res = IAPWS97(P=P,s=s).P
    return  res




#由压力和熵值求干度
@except_decorate_N_1
def psA_x(P,s):
    #所有区
    res = IAPWS97(P=P,s=s).x
    return  res




#由压力和熵值求焓值
@except_decorate_N_1
def psA_h(P,s):
    #所有区
    res = IAPWS97(P=P,s=s).h
    return  res




#由压力和熵值求熵值
@except_decorate_N_1
def psA_s(P,s):
    #所有区
    res = IAPWS97(P=P,s=s).s
    return  res




#相应压力下的饱和温度
@except_decorate_N_1
def pT(P):
    #饱和区 x默认为1.0
    res = IAPWS97(P=P, x=1.0).T - 273.15
    return  res



#由压力和干度求焓值
@except_decorate_N_1
def pxH(P,x=0.5):
    # 饱和区 x默认为0.5
    res = IAPWS97(P=P,x=x).h
    return  res




#由压力和干度求熵值
@except_decorate_N_1
def pxS(P,x=0.5):
    # 饱和区 x默认为0.5
    res = IAPWS97(P=P,x=x).s
    return  res



#相应饱和温度下的压力
@except_decorate_N_1
def tP(T):
    # 饱和区
    T = T+ 273.15
    res = IAPWS97(T=T , x=1.0).P
    return  res


#由温度和压力求干度
@except_decorate_N_1
def tpA(T,P):
    #除饱和区的其它区
    T = T + 273.15
    res = IAPWS97(T=T,P=P).x
    return  res


#由温度和干度求焓值
@except_decorate_N0
def txH(T,x=0.5):
    #饱和区
    if x <0 :
        x = 0
    if x >1:
        x =1
    T = T + 273.15
    res = IAPWS97(T=T, x=x).h
    return  res




#由温度和干度求熵值
@except_decorate_N0
def  txS(T,x=0.5):
    #饱和区
    if x <0 :
        x = 0
    if x >1:
        x =1
    T = T + 273.15
    res = IAPWS97(T=T, x=x).s
    return  res










