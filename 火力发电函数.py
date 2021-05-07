from math import log


class FuelAnalyzeFunction():
    #燃料分析计算函数

    def from_Xar_to_Xad(self,Xar,Mad,Mar):
        """
        收到基换算空干基
        :param Xar: 收到基；%
        :param Mad: 空干基水分；%
        :param Mar: 全水分；%
        :return: Xad: 空干基
        """
        Xad= Xar * (100 - Mad) / (100 - Mar)
        return Xad

    def from_Xar_to_Xd(self,Xar,Mar):
        """
        收到基换算干燥基
        :param Xar: 收到基；%
        :param Mar: 全水分；%
        :return: Xd:干燥基
        """
        Xd = Xar * 100 / (100 - Mar)
        return Xd

    def from_Xar_to_Xdaf(self,Xar,Mar,Aar):
        '''
        收到基换算干燥无灰基
        :param Xar:收到基
        :param Mar:全水分
        :param Aar:收到基灰分
        :return:Xdaf: 干燥无灰基
        '''
        Xdaf = Xar * 100 / (100 - Mar - Aar)
        return Xdaf

    def from_Xad_to_Xar(self,Xad,Mar,Mad):
        """
        空干基换算收到基
        :param Xad:空干基
        :param Mar:全水分
        :param Mad:空干基水分
        :return: Xar:收到基

        """
        Xar = Xad * (100 - Mar) / (100 - Mad)
        return Xar

    def from_Xad_to_Xd(self,Xad, Mad):
        '''
        空干基换算干燥基
        :param Xad: 空干基
        :param Mad:空干基水分
        :return:Xd:干燥基
        '''
        Xd = Xad * 100 / (100 - Mad)
        return Xd

    def from_Xad_to_Xdaf(self,Xad,Mad,Adaf):
        '''
        空干基换算干燥无灰基
        :param Xad: 空干基
        :param Mad:空干基水分
        :param Adaf:空干基灰分
        :return: Xdaf:干燥无灰基
        '''
        Xdaf = Xad * 100 / (100 - Mad - Adaf)
        return Xdaf

    def from_Xd_to_Xar(self,Xd,Mar):
        '''
        干燥基换算收到基
        :param Xd: 干燥基
        :param Marf:全水分
        :return: Xar:收到基
        '''
        Xar = Xd * (100 - Mar) / 100
        return Xar

    def from_Xd_to_Xad(self,Xd,Mad):
        '''
        干燥基换算空干基
        :param Xd: 干燥基
        :param Mad: 空干基水分
        :return: Xad: 空干基
        '''
        Xad = Xd * (100 - Mad) / 100
        return Xad

    def from_Xd_to_Xdaf(self,Xd,Ad):
        '''
        干燥基换算干燥无灰基
        :param Xd: 干燥基
        :param Ad:干燥基灰分
        :return: Xdaf: 干燥无灰基
        '''
        Xdaf = Xd * 100 / (100 - Ad)
        return Xdaf

    def from_Xdaf_to_Xar(self,Xdaf,Mar,Aar):
        '''
        干燥无灰基换算收到基
        :param Xdaf: 干燥无灰基
        :param Mar:全水分
        :param Aar:收到基灰分
        :return: Xar: 收到基
        '''
        Xar = Xdaf * (100 - Mar - Aar) / 100
        return Xar
    def from_Xdaf_to_Xad(self,Xdaf,Mad,Adaf):
        '''
        干燥无灰基换算空干基
        :param Xdaf:干燥无灰基
        :param Mad:空干基水分
        :param Adaf:空干基灰分
        :return:Xad:空干基
        '''
        Xad = Xdaf * (100 - Mad - Adaf) / 100
        return Xad
    def from_Xadf_to_Xd(self,Xdaf,Ad):
        '''
        干燥无灰基换算干燥基
        :param Xadf: 干燥无灰基
        :param Ad: 干燥基灰分
        :return: Xd:干燥基
        '''
        Xd = Xdaf * (100 - Ad) / 100
        return Xd




#制粉系统计算函数
class CoalPulverizingSystemFunction():
    def get_Kvti(self,HGI):
        '''
        可磨性指数
        :param HGI: 哈氏可模性指数
        :return: Kvti:可磨性指数
        '''
        Kvti = 0.0149*HGI + 0.32
        return Kvti

    def get_FCdaf(self,Vdaf):
        '''
        煤的干燥无灰基固定碳含量
        :param Vdaf: 空干基挥发分
        :return:  FCdaf:固定碳含量
        '''
        FCdaf = 1 - Vdaf
        return FCdaf
    def get_Qnet_daf(self,Qnet_ar,Mt,Aar):
        '''
        干燥无灰基发热量
        :param Qnet_ar: 收到基低位发热量
        :param Mt:全水分
        :param Aar: 收到基灰分
        :return: Qnet_daf:干燥无灰基发热量
        '''
        Qnet_daf = (Qnet_ar + 2510 * Mt / 100) * 100 / (100 - Mt - Aar)
        return Qnet_daf

    def get_Qvol(self,Qnet_daf,FCdaf,Vdaf):
        '''
        挥发分的热量
        :param Qnet_def:煤的干燥无灰基低位发热量
        :param FCdaf: 煤的干燥无灰基固定碳含量
        :param Vdaf: 空干基挥发分
        :return: Qvol:挥发分的热值
        '''
        Qvol = (Qnet_daf - 7850 * 4.187 * FCdaf) / Vdaf
        return Qvol
    def get_Meagre_D0(self,FCdaf,Hdaf):
        '''
        贫煤和无烟煤除去灰分的纯煤密度
        :param FCdaf: 煤的干燥无灰基固定碳含量
        :param Hdaf: 煤的干燥无灰基氢
        :return:
        '''
        D0 = 100 / (0.56 * FCdaf + 5 * Hdaf)
        return D0

    def get_UnMeagre_D0(self, FCdaf, Hdaf):
        '''
        非贫煤和无烟煤除去灰分的纯煤密度
        :param FCdaf: 煤的干燥无灰基固定碳含量
        :param Hdaf: 煤的干燥无灰基氢
        :return:
        '''
        D0 = 100 / (0.334 * FCdaf + 4.25 * Hdaf + 23)
        return D0
    def get_Dc_ac(self,D0,Ad):
        '''
        煤的真密度
        :param D0:煤除去灰分的纯煤密度
        :param Ad: 煤的干燥基灰分
        :return: Dc_ac:煤的真密度
        '''
        Dc_ac = 100 * D0 / (100 - Ad * (1 - D0 / 2.9))
        return Dc_ac
    def get_Mmax(self,Mar):
        '''
        燃料的最大水分
        :param Mar:收到基水分
        :return:Mmax:燃料的最大水分
        '''
        Mmax = 1 + 1.07*Mar
        return Mmax

    def get_Dc_ap(self,Dc_ac,M,Mar):
        '''
        煤的视载密度
        :param Dc_ac: 煤的真密度
        :param M: 煤含水饱和时的极限水分
        :param Mar: 收到基水分
        :return: Dc_ap:煤的视载密度
        '''
        Dc_ap = 100 * Dc_ac / (100 + (Dc_ac - 1) * M) * (100 - M) / (100 - Mar)
        return Dc_ap


    def get_Dc_b(self,Dc_cp):
        '''
        原煤力度R5.9=20%~30%时的堆积密度
        :param Dc_ap: 煤的视载密度
        :return: Dc_b:原煤的堆积密度
        '''
        Dc_b = 0.63 * Dc_cp
        return Dc_b
    def get_Bunker_Dpc_b(self,Dc_ac,R90):
        '''
        煤粉仓中等密事程度的煤粉自由堆积密度
        :param Dc_ac:
        :param R90:
        :return:
        '''
        Dpc_b = 0.35 * Dc_ac + 0.004 * R90
        return Dpc_b
    def get_CoalFeeder_Dpc_b(self,Dc_ac,Mpc,R90):
        '''
        给粉机疏松程度的煤粉自由堆密度
        :param Dc_ac:煤的真密度
        :param Mpc:煤粉水分
        :param R90:煤粉细度
        :return:Dcp_b: 给粉机煤粉自由堆积密度
        '''
        Dpc_b = 0.3 * Dc_ac * (1 - 0.01*Mpc) + 0.004 * R90
        return Dpc_b

    def get_De(self, A,Lc):
        '''
        管道当量直径
        :param A:管道截面积；m2
        :param Lc:包容截面积A的周界长度；m
        :return:De
        '''
        De = 4 * A / Lc
        return De

    def get_Re(self,w,De,v):
        '''
        雷诺数
        :param w: 气体流速
        :param De: 管道当量直径
        :param v: 气体运动粘度
        :return: Re:雷诺数
        '''
        Re = w * De / v
        return Re
    def get_Air_r(self,Re,di,Dc,d):
        '''
        摩擦阻力系数(纯空气)
        :param Re: 雷诺数
        :param di:管道内部相对粗糙程度
        :param Dc: 管道当量直径
        :param d : 管道内部绝对粗糙程度
        :return:r:摩擦阻力系数
        '''
        if Re < 2000:
            r = 64 / Re

        elif   4000 <Re< 560/d:
            r = 0.0055 * pow((1 + (2 * 10**4* di + 10**6 / Re)) , (1 / 3))
        elif Re > (560/d):
            r=(2*log(Dc/d)+1.14)**-2

        else:
            r = '输入数值有误,请验证后输入'
        return  r

    def get_Powder_r(self,Re,di=None):
        '''
        摩擦阻力系数(含粉) ,可选参数di管道内部绝对粗糙程度
        :param Re:雷诺数
        :return:r:摩擦阻力系数
        '''

        r = (1.8 * log(Re) - 1.64) ** -2
        return r
    def get_dPfo(self,r,L,De,D0,w):
        '''
        管道摩擦阻力
        :param r:  摩擦阻力系数
        :param L: 摩擦阻力计算长度
        :param De: 管道当量直径
        :param D0: 纯气体密度
        :param w: 气体流速
        :return: Dpfo:管道摩擦阻力
        '''
        dPfo =  r * L / De * (D0 * w ** 2) / 2
        return dPfo

class CoalMillFunction():
    def get_fH(self,HGI):
        '''
        磨煤机出力-可磨性修正系数
        :param HGI: 哈氏可磨性指数
        :return: fH:可磨性修正系数
        '''
        fH = (HGI / 55) **0.85
        return fH
    def get_fR(self,R90):
        '''
        磨煤机出力-煤粉细度修正指数
        :param R90: 煤粉细度
        :return: fR: 煤粉细度修正指数
        '''
        fR = (R90 / 23) ** 0.35
        return fR

    def get_LowerGrade_fM(self,Mt):
        '''
        磨煤机出力-低热值煤原煤水分修正系数
        :param Mt: 全水分
        :return: FM:低热值煤原煤水分修正系数
        '''
        if Mt >12:
            fM = 1.0 + (12 - Mt) * 0.0125
        else:
            fM = 1
        return fM
    def get_HighGrade_fM(self,Mt):
        '''
        磨煤机出力-高热值煤原煤水分修正
        :param Mt: 全水分
        :return: fM
        '''
        if Mt >8:
            fM = 1.0 + (8 - Mt) * 0.0125
        else:
            fM = 1
        return fM
    def get_fA(self,Aar):
        '''
        磨煤机出力-原煤灰分修正系数
        :param Aar: 收到基灰分
        :return: fA
        '''
        if Aar > 20:
            fA= 1.0 +(20-Aar)*0.005
        else:
            fA = 1
        return fA

    def get_fsi(self,R90):
        '''
        磨煤机出力-分离器形式修正系数
        :param R90: 煤粉细度
        :return: fsi:分离器形式修正系数
        '''
        if  R90 >25:
            fsi = 1
        elif R90>=18:
            fsi = 1+(25-R90)*0.01
        else:
            fsi = 1.07
        return fsi
    def get_Bm(self,Bm0,fH,fR,fM,fA,fg,fe,fsi):
        '''
        磨煤机碾磨出力
        :param Bm0: 磨煤机的基本出力
        :param fH: 磨煤机出力-可磨性修正系数
        :param fR: 磨煤机出力-煤粉细度修正系数
        :param fM: 磨煤机出力-原煤水分修正系数
        :param fA: 磨煤机出力-原煤灰分修正系数
        :param fg: 磨煤机出力-原煤粒度修正系数
        :param fe: 研磨件磨损之中后期出力降低系数
        :param fsi: 磨煤机出力-分离器形式修正系数
        :return: Bm:磨煤机碾磨出力
        '''
        Bm = Bm0 * fH * fR * fM * fA * fg * fe * fsi
        return Bm
    def get_Qmmf(self,Qgr_ar,Sar,Aar):
        '''
        含水无矿物质基热值
        :param Qgr_ar: 收到基高位发热量
        :param Sar: 收到基硫分
        :param Aar: 收到基灰分
        :return: Qmmf: 含水无矿物质基热值
        '''
        Qmmf = (Qgr_ar - 0.116*Sar) / (100 - (1.08 * Aar + 0.55 * Sar)) * 100
        return Qmmf
    def get_FCar(self,Mar,Aar,Var):
        '''
        收到基固定碳
        :param Mar:收到基水分
        :param Aar: 收到基灰分
        :param Var: 收到基挥发分
        :return: FCar:收到基固定碳
        '''
        FCar=100-(Mar+Aar+Var)
        return FCar
    def get_FCdmmf(self,FCar,Mar,Aar,Sar):
        '''
        干燥无矿物基固定碳
        :param FCar: 收到基固定碳
        :param Mar: 收到基水分
        :param Aar: 收到基灰分
        :param Sar: 收到基硫分
        :return: FCdmmf:干燥无矿物基固定碳
        '''
        FCdmmf = (FCar - 0.116*Sar) / (100 - (Mar + 1.08 * Aar + 0.55 * Sar))
        return FCdmmf

    def get_Nmv(self,Xm):
        '''
        通风率
        :param Xm: 设计出力下的负荷率
        :return: Nmv:通风率
        '''
        if Xm >= 25:
            Nmv = (0.6+0.4*Xm)*100
        else:
            Nmv = 70
        return Nmv




#性质函数
class NatureFunction():
    def get_CpO2(self,T):
        '''
        O2定压比热容
        :param T: 摄氏温度
        :return:CpO2:O2定压比热容
        '''
        if  255 <= (T+273.15) <= 1000:
            CpO2 = 1.40536 - (T + 273) * 1.12295e-3 + (T + 273) ** 2 * 3.6954e-06 - \
                   (T + 273) **3 * 3.647e-9 + ((T +273) **4) *1.227e-12
            return CpO2
        else:
            return '温度超出计算值范围'


    def get_CpCO2(self,T):
        '''
        CO2定压比热容
        :param T: 摄氏温度
        :return: CpCO2: CO2定压比热容
        '''
        if 255 <= (T + 273.15) <= 1000:
            CpCO2 = 0.89172 + (T + 273) * 3.2445e-03 - (T + 273) ** 2 * 2.4541e-06 + (T + 273) **3 * 7.43674e-10 + (
                    T + 273) **4 * 2.3502e-16
            return CpCO2
        else:
            return  '温度超出计算值范围'

    def get_CpCO(self,T):
        '''
        CO定压比热容
        :param T:摄氏温度
        :return:CpCO: CO定压比热容
        '''
        if 255 <= (T + 273.15) <= 1000:
            CpCO = 1.37803 - (T + 273) * 6.0138e-04 + (T + 273) ** 2 * 1.3714e-06 - (T + 273) **3 * 7.5473e-10 + (
                    T + 273) **4 * 8.897e-14
            return  CpCO
        else:
            return '温度超出计算值范围'

    def get_N2(self,T):
        '''
        N2定压比热容
        :param T:摄氏温度
        :return:N2: N2定压比热容
        '''
        if 255 <= (T + 273.15) <= 1000:
            CpN2 = 1.3759 - (T + 273) * 5.2812e-04 + (T + 273) ** 2 * 1.0649e-06 - (T + 273) **3 * 4.4678e-10 - (
                    T + 273) **4 * 5.1831e-15
            return  CpN2
        else:
            return  '温度超出计算值范围'

    def get_H2O(self,T):
        '''
        H2O定压比热容
        :param T:摄氏温度
        :return:  H2O压比热容
        '''

        if 255 <= (T + 273.15) <= 1000:
            CpH2O = 1.54792 - (T + 273) * 6.7253e-04 + (T + 273) ** 2 * 2.2081e-06 - (T + 273) **3 * 1.8077e-09 + (
                        T + 273) ** 4 * 5.67687e-13
            return  CpH2O
        else:
            return  '温度超出计算值范围'

    def get_Cp_fg_d(self,CpO2,CpCO2,CpN2,QO2_fg_d,QCO2_fg_d,QN2_fg_d):
        '''
        干烟气定压比热容
        :param CpO2:O2定压比热容；
        :param CpCO2:CO2定压比热容
        :param CpN2:N2定压比热容
        :param QO2_fg_d:干烟气中O2的体积分数
        :param QCO2_fg_d:干烟气中CO2的体积分数；%
        :param QN2_fg_d:干烟气中N2的体积分数
        :return:Cp_fg_d:干烟气定压比热容
        '''
        Cp_fg_d = CpO2 * QO2_fg_d / 100 + CpCO2 * QCO2_fg_d / 100 + CpN2 * QN2_fg_d / 100
        return  Cp_fg_d


    def get_Cp_a_d(self,T):
        '''
        干空气定压比热容
        :param T:摄氏温度
        :return:Cp_a_d:干空气定压比热容
        '''

        Cp_a_d = 1.37780212 - (T + 273) * 6.46620591e-04 + (T + 273) **2 * 1.60493642e-06 - (
                T + 273) **1.11259405e-09 + (T + 273) ** 4 * 2.52930872e-13
        return  Cp_a_d


    def get_Cair_m10(self,T):
        '''
        湿空气定压比热容  d=10g/kg
        :param T:摄氏温度
        :return:Cair_m10:湿空气定压比热容
        '''
        Cair_m10 = 3.588313e-14 * T ** 4 - 1.442739e-10 * T **3 + 1.870318e-07 * T ** 2 + 1.012172e-05 * T + \
                   1.012981e+00
        return  Cair_m10


    def get_Cair_m30(self,T):
        '''
        湿空气定压比热容  d=30g/kg
        :param T:摄氏温度
        :return:
        '''
        Cair_m30 = 3.888525e-14 * T **4 - 1.553445e-10 * T ** 3 + 2.004992e-07 * T ** 2 + 8.328157e-06 * T + \
                   1.029772e+00
        return  Cair_m30

    def get_Da(self,Pat,Pa,Ta,Da_st=1.293):
        '''
        干空气密度
        :param Da_st: 干空气标准状态密度
        :return:Da:空气密度
        '''
        Da = 2.694 * Da_st * (Pat + Pa) / (273 + Ta) * 10e-03
        return  Da

    def get_Daw(self,Da,d):
        '''
        湿空气密度
        :param Da:干空气标准状态密度
        :param d:干空气含湿度
        :return: Daw:湿空气密度
        '''
        Daw = (1 + 0.001 * d) / (1 / Da + 0.001 * d / 0.804)
        return  Daw
    def get_DryAirPower_y(self,T):
        '''
        干空气动力粘度
        :param T:摄氏温度
        :return:y:干空气动力粘度
        '''
        y = 8.934484e-09 * T ** 3 - 2.572415e-05 * T ** 2 + 4.878233e-02 * T + 1.714108e+01
        return  y
    def get_DryAirMove_y(self,T):
        '''
        干空气运动粘度
        :param T:摄氏温度
        :return:y:干空气运动粘度
        '''
        y = -1.587098e-08 * T ** 3 + 8.802969e-05 * T ** 2 + 9.174350e-02 * T + 1.314801e+01
        return  y
    def get_WetAirPower_y10(self,T):
        '''
        湿空气动力粘度 ,d=10g/kg
        :param T:摄氏温度
        :return:y:湿空气动力粘度 ,d=10g/kg
        '''


        y=8.861489e-09*T**3-2.552522e-5*T**2+4.869396e-2*T+1.705297e+01
        return  y
    def get_WetAirMove_y10(self,T):
        '''
        湿空气运动粘度 ,d=10g/kg
        :param T:摄氏温度
        :return:y:湿空气运动粘度 ,d=10g/kg
        '''
        y = -1.893141e-08 * T ** 3 + 9.376309e-05 * T ** 2 + 8.980629e-02 * T + 1.323096e+01
        return  y

    def get_WetAirPower_y30(self,T):
        '''
        湿空气动力粘度 ,d=30g/kg
        :param T:摄氏温度
        :return:y:湿空气动力粘度 ,d=30g/kg
        '''
        y = 8.557254e-09 * T ** 3 - 2.484946e-05 * T ** 2 + 4.837432e-02 * T + 1.690736e+01
        return  y


    def get_WetAirMove_y30(self,T):
        '''
        湿空气运动粘度 ,d=30g/kg
        :param T:摄氏温度
        :return:y:湿空气运动粘度 ,d=30g/kg
        '''
        y = -1.641026e-08 * T ** 3 + 9.037799e-05 * T ** 2 + 9.244622e-02 * T + 1.317555e+01
        return  y
    def get_AirPower_y(self,T):
        '''
        空气动力粘度
        :param T:摄氏温度
        :return:y:空气动力粘度
        '''
        y = 7.439782e-09 * T ** 3 - 2.353730e-05 * T ** 2 + 4.788772e-02 * T + 1.723007e+01
        return  y

    def get_N2Power_y(self,T):
        '''
        N2动力粘度
        :param T:摄氏温度
        :return:y:N2动力粘度
        '''
        y = 4.156954e-09 * T ** 3 - 1.332168e-05 * T ** 2 + 3.995493e-02 * T + 1.674196e+01
        return  y
    def get_O2Power_y(self,T):
        '''
        O2动力粘度
        :param T: 摄氏温度
        :return: y:N2动力粘度
        '''
        y = 4.156954e-09 * T ** 3 - 1.332168e-05 * T ** 2 + 3.995493e-02 * T + 1.674196e+01
        return y

    def get_CO2Power_y(self,T):
        '''
        O2动力粘度
        :param T: 摄氏温度
        :return: y:N2动力粘度
        '''
        y = 2.350427e-09 * T ** 3 - 8.548951e-06 * T ** 2 + 4.374048e-02 * T + 1.396643e+01
        return y

    def get_H2OPower_y(self,T):
        '''
        H2O动力粘度
        :param T: 摄氏温度
        :return: y:H2O动力粘度
        '''
        y = -2.136752e-09 * T ** 3 + 9.813520e-06 * T ** 2 + 3.639666e-02 * T + 8.260000e+00
        return y

    def get_COPower_y(self,T):
        '''
        CO动力粘度
        :param T: 摄氏温度
        :return: y:H2动力粘度
        '''
        y = 8.741259e-09 * T **3 - 2.087413e-05 * T ** 2 + 4.476224e-02 * T + 1.616643e+01
        return y


    def get_H2Power_y(self,T):
        '''
        H2动力粘度
        :param T: 摄氏温度
        :return: y:H2动力粘度
        '''
        y = 2.525253e-09 * T ** 3 - 7.196970e-06 * T**2 + 2.001263e-02 * T + 8.370000e+00
        return y

    def get_CH4Power_y(self,T):
        '''
        CH4动力粘度
        :param T: 摄氏温度
        :return: y:CH4动力粘度
        '''
        y = 5.555556e-09 * T ** 3 - 1.095238e-05 * T **2 + 2.925397e-02 * T + 1.039762e+01
        return y

    def get_ARIrower_y(self,T):
        '''
         空气动力粘度
        :param T: 摄氏温度
        :return: y:空气动力粘度
        '''
        y = -1.763792e-08 * T ** 3 + 8.983683e-05 * T ** 2 + 9.145843e-02 * T + 1.316014e+01

        return y


    def get_N2Move_y(self,T):
        '''
         N2运动粘度
        :param T: 摄氏温度
        :return: y:N2运动粘度
        '''
        y = -8.974359e-09 * T ** 3 + 8.417249e-05 * T ** 2 + 8.754662e-02 * T + 1.304336e+01
        return y

    def get_O2Move_y(self,T):
        '''
         O2运动粘度
        :param T: 摄氏温度
        :return: y:O2运动粘度
        '''
        y = -1.394716e-08 * T ** 3 + 9.851981e-05 * T ** 2 + 8.598679e-02 * T + 1.356923e+01
        return y


    def get_CO2Move_y(self,T):
        '''
         CO2运动粘度
        :param T: 摄氏温度
        :return: y:CO2运动粘度
        '''
        y = -5.439005e-09 * T ** 3 + 6.622960e-05 * T ** 2 + 4.811325e-02 * T + 7.085105e+00
        return y

    def get_HO2Move_y(self,T):
        '''
         HO2运动粘度
        :param T: 摄氏温度
        :return: y:HO2运动粘度
        '''
        y = -1.437451e-09 * T ** 3 + 1.146445e-04 * T ** 2 + 8.050913e-02 * T + 1.005667e+01

        return y

    def get_COMove_y(self,T):
        '''
         CO运动粘度
        :param T: 摄氏温度
        :return: y:CO运动粘度
        '''
        y = -1.406371e-08 * T ** 3 + 9.522145e-05 * T ** 2 + 8.552059e-02 * T + 1.319790e+01

        return y

    def get_H2Move_y(self,T):
        '''
         H2运动粘度
        :param T: 摄氏温度
        :return: y:H2运动粘度
        '''

        y = -8.896659e-08 * T ** 3 + 6.405594e-04 * T ** 2 + 5.844561e-01 * T + 9.240559e+01

        return y
    def get_CH4Move_y(self,T):
        '''
         CH4运动粘度
        :param T: 摄氏温度
        :return: y:CH4运动粘度
        '''

        y = -5.421011e-20 * T ** 3 + 1.141667e-04 * T ** 2 + 9.567857e-02 * T + 1.446905e+01
        return y


class DewPointFunction():
    #露点函数

    def get_Tdp(self,d2):
        '''
        水露点
        :param d2:空气；含湿量
        :param Pa:空气绝对压力
        :return:
        '''

        if  550 >=  d2 >= 3.8:
            Tdp = 16.538 * log(d2) - 23.996
        elif d2 >=550:
            Tdp = 10.445 * log(d2) + 14.553
        else:
            Tdp = '输入参数有误'
        return Tdp

    def get_Tdp_s(self,Aar,Qnet_ar,CaO,MgO,Fe2O3,afly,Sc_ar,aF,Tdp,B=125):

      '''
        酸露点
      :param Aar: 收到基灰分
      :param Qnet_ar:收到基低位发热量
      :param CaO:灰中CaO百分比
      :param MgO:灰中MgO百分比
      :param Fe2O3:灰中Fe2O3百分比
      :param afly:飞灰份额
      :param Sc_ar:燃料可燃硫
      :param aF:炉膛出口过量空气系数
      :param B:炉膛出口过量空气系数相关参数，一般取125
      :param Tdp:水露点
      :return:Tdp_s:酸露点
      '''
      Asp = Aar * 4182 / Qnet_ar
      Ab = 0.239
      afly * Asp * (7 * CaO + 3.5 * MgO + Fe2O3)
      Ks = 0.63 + 0.345 * 0.99 * Ab
      Ssp = Sc_ar * 4182 / Qnet_ar
      n = afly * Asp
      if aF==1.2:
        B = 121
      else:
            if 15 >=aF >= 1.4 :
                B = 129
      Tdp_s = Tdp + B * (Ks * Ssp) **(1 / 3) / 1.05 ** n
      return Tdp_s

    def get_Tdp_to_d(self,Tdp):
        '''
        空气含湿度和露点的关系(空气绝对气压Pa=100.725)
        :param Tdp: 露点
        :return: d: 空气含湿度
        '''
        if  80 >=Tdp>=0 :
            d = 1.818361E-08 * Tdp ** 6 - 3.418121E-06 * Tdp ** 5 + 2.562357E-04 * Tdp ** 4 - 8.675212E-03 * Tdp ** 3 + 1.522366E-01 * Tdp ** 2 - 6.218166E-01 * Tdp + 4.968625E+00
        elif 90  >= Tdp>=80:
            d = 2.573529E-04 * Tdp ** 6 - 1.287019E-01 * Tdp ** 5 + 2.682858E+01 * Tdp ** 4 - 2.983606E+03 * Tdp ** 3 + 1.866869E+05 * Tdp ** 2 - 6.231163E+06 * Tdp + 8.667209E+07
        else:
            d= '输入数据超出范围,请重新输入'
        return d

class FuelBoilerEfficiencyFunction():
    #固体燃料/液体燃料锅炉效率计算函数


    def get_VN2(self,Va_d_th_er,Nar):
        '''
        原煤燃烧生成的N2理论容积

        :param Va_d_th_er:修正的理论干空气量
        :param Nar:收到基氮
        :return:VN2 :生成N2理论容积
        '''
        VN2 = 0.79 * Va_d_th_er + 0.8 * Nar / 100
        return  VN2

    def get_VRO2(self,Car,Sr_ar):
        '''

        :param Car:收到基碳
        :param Sr_ar:收到基可燃硫
        :return:生成的RO2理论容积
        '''
        VRO2 = 1.866 / 100 * (Car + 0.375 * Sr_ar)
        return  VRO2

    def get_VH2O(self,Har,Mar,Va_d_th_er):
        '''
        原煤燃烧生成的H2O理论容积
        :param Har:收到基氢
        :param Mar:收到基水分
        :param Va_d_th_er:修正的理论干空气量
        :return VH2O: 生成的H2O理论容积
        '''
        VH2O = 0.111 * Har + 0.0124 * Mar + 0.0161 * Va_d_th_er
        return VH2O

    def get_Cs_rs_m(self,alz, afh,acj,Clz,Cfh,Ccj):
        '''
        灰渣平均可燃物质量分数
        :param alz:炉渣占燃料总灰量的质量分数
        :param afh:飞灰占燃料总灰量的质量分数
        :param acj:沉降灰占燃料总灰量的质量分数
        :param Clz:炉渣中可燃物的质量分数
        :param Cfh:飞灰中可燃物的质量分数
        :param Ccj:沉降灰中可燃物的质量分数
        :return:Cs_rs_m :灰渣平均可燃物质量分数
        '''
        Cs_rs_m = alz * Clz / (100 - Clz) + afh * Cfh / (100 - Cfh) + acj * Ccj / (100 - Ccj)
        return Cs_rs_m

    def get_Va_d_th_er(self,C_b,Sar,Har,Oar):
        '''
        修正的理论干空气量
        :param C_b:实际燃烧掉的碳占入炉燃料的质量分数
        :param Sar:收到基硫分
        :param Har:收到基氢
        :param Oar:收到基氧
        :return:Va_d_th_er:干空气量
        '''
        Va_d_th_er = 0.0888*C_b + 0.0333*Sar + 0.2647*Har - 0.0334*Oar
        return Va_d_th_er

    def get_Vfg_d_th(self,Car,Sar,Va_d_th_er,Nar):
        '''
        理论烟气量
        :param Car:
        :param Sar:
        :param Va_d_th_er:
        :return:
        '''
        Vfg_d_th = 1.8658 * Car / 100 + 0.6989 * Sar / 100 + 0.79 * Va_d_th_er + 0.8 * Nar / 100
        return Vfg_d_th



    def  get_Vfg_d_th_er(self,C_b,Sar,Va_d_th_er,Nar):
        '''

        :param C_b:实际燃烧掉的碳占入炉燃料的质量分数
        :param Sar:收到基硫分
        :param Va_d_th_er:修正的理论干空气量
        :param Nar:收到基氮
        :return:Vfg_d_th_er :
        '''
        Vfg_d_th_er = 1.8658 * C_b / 100 + 0.6989 * Sar / 100 + 0.79 * Va_d_th_er + 0.8 * Nar / 100
        return Vfg_d_th_er

    def get_acr(self,VO2_fg_d):
        '''
        修正的过量空气系数
        :param VO2_fg_d:干烟气中O2的体积分数
        :return:acr:修正的过量空气系数
        '''

        acr= 21 / (21 - VO2_fg_d)
        return  acr

    def get_Vfg_d_AH_lv(self,acr,Vfg_d_th_er,Va_d_th_er):
        '''
        每千克(Nm3)燃料燃烧生成空预器出口干烟气体积
        :param acr:修正的过量空气系数
        :param Vfg_d_th_er:修正的理论干烟气量
        :param Va_d_th_er:修正的理论干空气量
        :return:Vfg_d_AH_lv:每千克(Nm3)燃料燃烧生成空预器出口干烟气体积
        '''
        Vfg_d_AH_lv = Vfg_d_th_er + (acr - 1) * Va_d_th_er
        return  Vfg_d_AH_lv


    def get_VCO2_c_b(self,C_b):
        '''
        每千克(Nm3)燃料实际燃烧掉的碳计算CO2的体积
        :param C_b:实际燃烧掉的碳占入炉燃料的质量分数
        :return:VCO2_c_b:每千克(Nm3)燃料实际燃烧掉的碳计算CO2的体积
        '''
        VCO2_c_b = 1.8658 * C_b / 100
        return  VCO2_c_b

    def get_RCa_S(self,CaCO3_des,Sar,qm_c,qm_des):
        '''
        钙硫摩尔比
        :param CaCO3_des:脱硫剂中碳酸钙的质量分数
        :param Sar:收到基硫分
        :param qm_c:入炉燃料的质量流量
        :param qm_des:入炉脱硫剂质量流量
        :return:RCa_S:钙硫摩尔比

        '''

        RCa_S = 32.066 / 100.086 * CaCO3_des / Sar * qm_des / qm_c
        return RCa_S



    def get_nSO2(self,QSO2_fg_d,Sar,Vfg_d):
        '''
        脱硫效率
        :param QSO2_fg_d:干烟气中SO2的体积分
        :param Sar:收到基硫分
        :param Vfg_d:SO2含量测量位置处每千克燃料燃烧生成的干烟气体积
        :return:nSO2:脱硫效率
        '''
        nSO2 = (1 - 32.066 / 22.41 * QSO2_fg_d / Sar * Vfg_d)
        return  nSO2

    def get_Aar_des(self,Sar,Car,CaCO3_des,RCa_S):
        '''
        脱硫剂灰分的质量分数分数
        :param Sar:收到基硫分
        :param Car:收到基碳
        :param CaCO3_des:脱硫剂中碳酸钙的质量分数
        :param RCa_S:钙硫摩尔比
        :return:Aar_des:脱硫剂灰分的质量分数分数
        '''

        Aar_des = 100.086 / 32.066 * Sar / CaCO3_des * RCa_S * Car
        return  Aar_des


    def get_CaCO3_ud(self,Sar,RCa_S,nCaCO3_dec):
        '''
        脱硫剂未分解的碳酸钙的质量分数
        :param Sar:收到基硫分
        :param RCa_S:钙硫摩尔比
        :param nCaCO3_dec:碳酸钙分解率
        :return:
        '''
        CaCO3_ud = 100.086 / 32.066 * Sar * RCa_S * (1 - nCaCO3_dec)
        return CaCO3_ud

    def get_CaSO4(self,Sar,nSO2):
        '''
       脱硫后生成的硫酸钙的质量分数
        :param Sar:收到基硫分
        :param nSO2:脱硫效率
        :return:CaSO4:硫后生成的硫酸钙的质量分数
        '''
        CaSO4 = 136.140 / 32.066 * nSO2 / 100 * Sar
        return  CaSO4

    def get_CaO(self,Sar,nSO2,RCa_S,nCaCO3_dec):
        '''
        脱硫剂锻烧反应后未发生硫酸盐化反应的氧化钙质量分数
        :param Sar:收到基硫分
        :param nSO2:脱硫效率
        :param RCa_S:钙硫摩尔比
        :param nCaCO3_dec:碳酸钙分解率)
        :return:CaO :脱硫剂锻烧反应后未发生硫酸盐化反应的氧化钙质量分数
        '''
        CaO = 56.077 / 32.066 * (RCa_S * nCaCO3_dec / 100 - nSO2 / 100) * Sar
        return CaO


    def get_Cs_to_des(self,Aar,Aar_des,CaCO3_ud,CaSO4,CaO):
        '''
        每千克入炉燃料的灰分质量分数
        :param Aar:收到基灰分
        :param Aar_des:脱硫剂灰分的质量分数
        :param CaCO3_ud:脱硫剂未分解的碳酸钙的质量分数
        :param CaSO4:脱硫后生成的硫酸钙的质量分数
        :param CaO:脱硫剂锻烧反应后未发生硫酸盐化反应的氧化钙质量分数
        :return:
        '''
        Cs_to_des = Aar + Aar_des + CaCO3_ud + CaSO4 + CaO
        return  Cs_to_des

    def get_QCO2_fg_d(self,VCO2_c_b,Vfg_d_AH_lv,QCO_fg_d):
        '''
        空预器出口干烟气CO2体积分数
        :param VCO2_c_b:每千克(Nm3)燃料实际燃烧掉的碳计算CO2的体积
        :param Vfg_d_AH_lv:每千克(Nm3)燃料燃烧生成空预器出口干烟气体积)
        :param QCO_fg_d:空气预热器出口干烟气中CO体积分数
        :return:QCO2_fg_d: 空预器出口干烟气CO2体积分数
        '''
        QCO2_fg_d = 100 * VCO2_c_b / Vfg_d_AH_lv - QCO_fg_d
        return  QCO2_fg_d

    def get_C_b_des(self,Car,Cs_to_des,Cs_rs_m):
        '''
        添加脱硫剂后实际燃烧的碳占人炉燃料的质量分数
        :param Car:收到基碳
        :param Cs_to_des:每千克入炉燃料的灰分质量分数
        :param Cs_rs_m:灰渣平均可燃物质量分数
        :return:C_b_des
        '''
        C_b_des = Car - Cs_to_des / 100 * Cs_rs_m
        return  C_b_des

    def get_Va_d_th_cr_des(self,C_b_des,Sar,Har,Oar,nSO2):
        '''
        添加脱硫剂后修正的理论干空气量
        :param C_b_des:添加脱硫剂后实际燃烧的碳占人炉燃料的质量分数
        :param Sar:收到基硫分
        :param Har:收到基氢
        :param Oar:收到基氧
        :param nSO2:脱硫效率
        :return:
        '''
        Va_d_th_cr_des = 0.0888 * C_b_des + 0.333 * Sar + 0.2647 * Har - 0.0334 * Oar + 0.0166 * Sar * nSO2 / 100
        return  Va_d_th_cr_des
    def get_Vfg_d_th_cr_des(self,C_b_des,Sar,nSO2,Va_d_th_cr_des,Nar,RCa_S,nCaCO3_dec):
        '''
        添加脱硫剂后修正的理论干烟气量
        '''
        Vfg_d_th_cr_des = 1.8658 * C_b_des / 100 + 0.6989 * Sar / 100 + 0.79 * Va_d_th_cr_des + 0.8 * Nar / 100 + 0.6989 * (
                    RCa_S * nCaCO3_dec / 100 - nSO2 / 100) * Sar / 100
        return  Vfg_d_th_cr_des

    def get_acr_des(self,Va_d_des,Va_d_th_cr_des):
        '''
        添加脱硫剂后修正的过量空气系数
        :param Va_d_des:添加脱硫剂后的人炉干空气量
        :param Va_d_th_cr_des:添加脱硫剂后修正的理论干空气量
        :return:
        '''
        acr_des = Va_d_des / Va_d_th_cr_des
        return  acr_des


    def get_Vfg_d_AH_lv_des(self,Vfg_d_th_cr_des,acr_des,Va_d_th_cr_des):
        '''
        添加脱硫剂后每千克(Nm3)燃料燃烧生成空预器出口干烟气体积
        :param Vfg_d_th_cr_des:添加脱硫剂后修正的理论干烟气量
        :param acr_des:添加脱硫剂后修正的过量空气系数
        :param Va_d_th_cr_des:(添加脱硫剂后修正的理论干空气量
        :return:
        '''
        Vfg_d_AH_lv_des = Vfg_d_th_cr_des + (acr_des - 1) * Va_d_th_cr_des
        return Vfg_d_AH_lv_des


    def get_VCO2_c_b_des(self,Sar,C_b,RCa_S,nCaCO3_dec):
        '''
        添加脱硫剂后每千克(Nm3)实际燃烧掉的碳计算CO2的体积
        :param Sar:收到基硫分
        :param C_b:实际燃烧掉的碳占入炉燃料的质量分数
        :param RCa_S:钙硫摩尔比
        :param nCaCO3_dec:碳酸钙分解率
        :return:
        '''
        VCO2_c_b_des = 1.8658 * C_b / 100 + 0.6989*RCa_S * nCaCO3_dec / 100 * Sar / 100
        return VCO2_c_b_des

    def get_QCO2_fg_d_(self,VCO2_c_b_des,Vfg_d_AH_lv_des,QCO_fg_d):
        '''
        添加脱硫剂空预器出口干烟气CO2体积分数
        :param VCO2_c_b_des:添加脱硫剂后每千克(Nm3)实际燃烧掉的碳计算CO2的体积
        :param Vfg_d_AH_lv_des:添加脱硫剂后每千克(Nm3)燃料燃烧生成空预器出口干烟气体积)
        :param QCO_fg_d:空气预热器出口干烟气中CO体积分数
        :return:
        '''
        QCO2_fg_d = 100 * VCO2_c_b_des / Vfg_d_AH_lv_des - QCO_fg_d
        return  QCO2_fg_d


    def get_Crs(self,Trs):
        '''
        灰渣比热
        :param Trs:灰渣温度
        :return:
        '''
        Crs = 0.71 + 5.02e-04 * Trs
        return Crs

    def get_Cc(self,Vdaf,Tc):
        '''
        煤中可燃物质的比热
        :param Vdaf:空干基挥发分
        :param Tc:煤的温度
        :return:
        '''
        Cc = 0.84 + 37.68 * 10E-6 * (13 + Vdaf) * (130 + Tc)
        return  Cc

    def get_Cc_d(self,Crs,Ad,Cc):
        '''
        煤的干燥基比热
        :param Crs:灰渣比热容
        :param Ad:干燥基灰分
        :param Cc:煤中可燃物质的比热容
        :return:
        '''
        Cc_d = 0.01 * (Crs * Ad + Cc * (100 - Ad))
        return  Cc_d

    def get_Cc_ar(self,Cc_d,Mar):
        '''
        入炉煤比热
        :param Cc_d:煤的干燥基比热容
        :param Mar:收到基水分
        :return:
        '''
        Cc_ar = Cc_d * (100 - Mar) / 100 + 4.1868 * Mar / 100
        return  Cc_ar


    def get_Cfo(self,Tf,Tre):
        '''
        燃油比热
        :param Tf:进入系统边界的燃料温度
        :param Tre:(基准温度
        :return:
        '''

        Cfo=1.738+0.003*(Tf-Tre)/2

        return  Cfo


    def get_Qf_im(self,Mar,Mad):
        '''
        解冻燃料用热量
        :param Mar:收到基水分
        :param Mad:空干基水分
        :return:
        '''
        Qf_im = 3.35 * (Mar - Mad * (100 - Mar) / (100 - Mad))
        return  Qf_im

    def get_Cdes(self,Tdes, ):
        '''
        脱硫剂比热

        '''
        Cdes=0.71+5.02e-04*Tdes
        return Cdes

    def get_Qdes(self,qm_des,qm_f,Cdes,Tdes,Tre=25):
        '''
        脱硫剂物理显热
        :param qm_des:入炉脱硫剂质量流量
        :param qm_f:燃料质量流量
        :param Cdes:脱硫剂比热容
        :param Tdes:(脱硫剂温度
        :param Tre:(基准温度,
        :return:
        '''
        Qdes = qm_des / qm_f * Cdes * (Tdes - Tre)
        return Qdes

    def get_Pwv_sat(self,Ta):
        '''
        大气温度下(0~50℃)的水蒸气饱和压力
        :param Ta:Ta(空气温度；℃)
        :return:
        '''
        Pwv_sat = 611.7927 + 42.7809 * Ta + 1.6883 * Ta ** 2 + 1.2079 * 10E-02 * Ta ** 3 + 6.1637 * 10e-04 * Ta ** 4
        return Pwv_sat

    def get_ha_ab(self,ha_re,Pwv_sat,Pat):
        '''
        空气绝对湿度
        :param ha_re:空气相对湿度
        :param Pwv_sat:大气温度下的水蒸气饱和压力
        :param Pat:Pat(
        :return:
        '''
        ha_ab = 0.622 * ha_re * Pwv_sat / 100 / (Pat - ha_re * Pwv_sat / 100)
        return  ha_ab

    def get_Qwv(self,acr,Va_d_th_er,ha_ab,CpH2O,Ta_wm,Tre=25):
        '''
        进入系统的空气中水蒸气所携带的热量
        :param acr:修正的过量空气系数
        :param Va_d_th_er:修正的理论干空气量
        :param ha_ab:空气绝对湿度
        :param CpH2O:水蒸气定压比热容
        :param Ta_wm:进入系统的空气加权平均温度
        :param Tre:Tre
        :return:
        '''
        Qwv = 1.293 * acr * Va_d_th_er * ha_ab * CpH2O * (Ta_wm - Tre)
        return  Qwv


    def get_Vwv_fg_AH_lv(self,Har,Mar,acr,Va_d_th_er,ha_ab,qm_st_at,qm_f):
        '''
        每千克燃料燃烧生成的烟气中水蒸气的体积
        :param Har:收到基氢
        :param Mar:收到基水分
        :param acr:修正的过量空气系数
        :param Va_d_th_er:修正的理论干空气量
        :param ha_ab:空气绝对湿度
        :param qm_st_at:燃油雾化蒸汽质量流量
        :param qm_f:燃料质量流量
        :return:
        '''
        Vwv_fg_AH_lv = 1.24 * ((9 * Har + Mar) / 100 + 1.293 * acr * Va_d_th_er * ha_ab + qm_st_at / qm_f)
        return  Vwv_fg_AH_lv


    def get_Q3(self,Vfg_d_AH_lv,QCO_fg_d,QCH4_fg_d,QH2_fg_d,QCmHn_fg_d):
        '''
        气体未完全燃烧热损失
        :param Vfg_d_AH_lv:每千克(Nm3)燃料燃烧生成空预器出口干烟气体积
        :param QCO_fg_d:干烟气中CO的体积分数
        :param QCH4_fg_d:干烟气中CH4的体积分数
        :param QH2_fg_d:干烟气中H2的体积分数
        :param QCmHn_fg_d:干烟气中CmHn的体积分数
        :return:
        '''
        Q3 = Vfg_d_AH_lv * (126.36 * QCO_fg_d + 358.18 * QCH4_fg_d + 107.98 * QH2_fg_d + 590.79 * QCmHn_fg_d)
        return  Q3


    def get_Q4(self,Aar,Cs_rs_m):
        '''
        固体未完全燃烧热损失
        :param Aar:收到基灰分
        :param Cs_rs_m:灰渣平均可燃物质量分数
        :return:
        '''
        Q4 = 3.3727 * Aar * Cs_rs_m
        return  Q4

    def get_Q7_des(self,Sar,Rca_S,nCaCO3_dec,nSO2):
        '''
        脱硫损失热量
        :param Sar:收到基硫分
        :param Rca_S:钙硫摩尔比
        :param nCaCO3_dec:碳酸钙分解率
        :param nSO2:脱硫效率
        :return:
        '''
        Q7_des = Sar / 100 * (57.19 * Rca_S * nCaCO3_dec - 151.59 * nSO2)
        return Q7_des

    def get_Tfg_AH_lv_er_a(self,Ta_AH_en_d,Tfg_AH_en_m,Tfg_AH_lv_m,Ta_AH_en_m):
        '''
        送风温度修正后的排烟温度
        :param Ta_AH_en_d:设计的(保证的)空气预热器进口空气温度
        :param Tfg_AH_en_m:实测空气预热器进口烟气温度
        :param Tfg_AH_lv_m:实测空气预热器出口烟气温度
        :param Ta_AH_en_m:实测空气预热器进口空气温度
        :return:
        '''
        Tfg_AH_lv_er_a = (Ta_AH_en_d * (Tfg_AH_en_m - Tfg_AH_lv_m) + Tfg_AH_en_m * (Tfg_AH_lv_m - Ta_AH_en_m)) / (
                    Tfg_AH_en_m - Ta_AH_en_m)
        return  Tfg_AH_lv_er_a


    def get_Tfg_AH_lv_er_fw(self,Tfg_AH_lv_m,Tfg_ECO_en,Tfg_ECO_lv,Tfw_m,Tfg_AH_lv,Ta_AH_en,Tfg_AH_en,Tfw_d):
        '''
        给水温度修正后的排烟温度
        :param Tfg_AH_lv_m:实测空气预热器出口烟气温度
        :param Tfg_ECO_en:省煤器(如双级交错布置时为低温级省煤器)进口烟气温度
        :param Tfg_ECO_lv:煤器(如双级交错布置时为低温级省煤器)出口烟气温度
        :param Tfw_m:实测的给水温度
        :param Tfg_AH_lv:实测空气预热器出口烟气温度
        :param Ta_AH_en:实测空气预热器进口烟气温度
        :param Tfg_AH_en:实测空气预热器进口空气温度
        :param Tfw_d:设计的(保证的)给水温度
        :return:
        '''
        Tfg_AH_lv_er_fw = Tfg_AH_lv_m + (Tfg_ECO_en - Tfg_ECO_lv) / (Tfg_ECO_en - Tfw_m) * (Tfg_AH_lv - Ta_AH_en) / (
                    Tfg_AH_en - Ta_AH_en) * (Tfw_d - Tfw_m)
        return  Tfg_AH_lv_er_fw



class AirPreHeaterPerformance():
    #空预器性能

    def get_nlg_AH_1(self,Wfg_AH_lv,Wfg_AH_en):
        '''
        空预器漏风率1
        :param Wfg_AH_l:空气预热器进口烟气质量分数
        :param Wfg_AH_en:空气预热器出口烟气质量分数
        :return:
        '''
        nlg_AH = (Wfg_AH_lv - Wfg_AH_en) / Wfg_AH_en * 100
        return  nlg_AH

    def get_Dfg_d(self,C_b,Sar,Nar,Va_th_er,Vfg_d_th_er):
        '''

        :param C_b:实际燃烧掉的碳占入炉燃料的质量分数
        :param Sar:收到基硫分
        :param Nar:收到基氮
        :param Va_th_er:修正的理论干空气量
        :param Vfg_d_th_er:修正的理论干烟气量
        :return:
        '''

        Dfg_d = (3.6641 * C_b / 100 + 1.9979 * Sar / 100 + 0.9876*Va_th_er+Nar / 100) / Vfg_d_th_er
        return  Dfg_d


    def get_nlg_AH_2(self,aAH_lv_er,aAH_en_er,Va_th_er,Vfg_th_er,Da_d,Dfg_d,):
        '''
        空预器漏风率2
        :param aAH_lv_er:修正的空气预热器进口过量空气系数；
        :param aAH_en_er:修正的空气预热器出口过量空气系数
        :param Va_th_er:修正的理论干空气量
        :param zVfg_th_er:修正的理论干烟气量
        :param Da_d:干空气密度
        :param Dfg_d:按修正理论烟气量计算的干烟气密度
        :return:
        '''

        nlg_AH = (aAH_lv_er - aAH_en_er) * Va_th_er * Da_d / (
                    aAH_en_er * Va_th_er * Da_d + (Vfg_th_er * Dfg_d - Va_th_er * Da_d) * 100)
        return  nlg_AH


    def get_nlg_AH_3(self,QCO2_AH_en,QCO2_AH_lv,Dfg_AH_en,Dfg_AH_lv):
        '''
        空预器漏风率3
        :param QCO2_AH_en:空预器进口CO2体积分数
        :param QCO2_AH_lv:空预器出口CO2体积分数
        :param Dfg_AH_en:空气预热器进口烟气密度
        :param Dfg_AH_lv:(空气预热器出口烟气密度
        :return:
        '''

        nlg_AH = (QCO2_AH_en * Dfg_AH_lv - QCO2_AH_lv * Dfg_AH_en) / QCO2_AH_lv * Dfg_AH_en * 100
        return  nlg_AH


    def get_Tfg_AH_lv_nl(self,nlg_AH,Cp_a,Cp_fg,Tfg_AH_lv_m,Ta_AH_en_m):
        '''

        :param nlg_AH:空预器漏风
        :param Cp_a:在温度Ta_AH_en_m和Tfg_AH_lv_m之间的空气定压比热容
        :param Cp_fg:在温度Tfg_AH_lv_m和Tfg_AH_lv_nl之间的空气定压比热容
        :param Tfg_AH_lv_m:空预器出口烟气温度
        :param Ta_AH_en_m:空预器进口空气温度
        :return:
        '''
        Tfg_AH_lv_nl = nlg_AH * Cp_a * (Tfg_AH_lv_m - Ta_AH_en_m) / Cp_fg / 100 + Tfg_AH_lv_m
        return  Tfg_AH_lv_nl



    def get_nfg_AH(self,Tfg_AH_en_m,Tfg_AH_lv_nl,Ta_AH_en_m):
        '''

       空预器烟气侧效率
        '''
        nfg_AH=(Tfg_AH_en_m-Tfg_AH_lv_nl)/(Tfg_AH_en_m-Ta_AH_en_m)*100
        return  nfg_AH




# 风机性能函数
class DraughtFanPerformance():

    def get_Aw(self,Tw):
        '''
        给定温度下水蒸气分压修正系数
        :param Tw:湿球温度计温度
        :return:
        '''
        if Tw < 0:
            Aw = 5.94e-04
        elif 0 < Tw < 150:
            Aw = 6.66e-04
        else:
            Aw = None
        return Aw

    def get_Pv_1(self,Psat,Pa,Aw,Ta,Tw):
        '''
        水的饱和蒸汽压力Psat与湿球温度Tw的关系1
        :param Psat:湿球温度Tw下的饱和蒸汽压力
        :param Pa:大气压
        :param Aw:给定温度下水蒸气分压修正系数
        :param Ta:干球温度
        :param Tw:湿球温度
        :return:
        '''
        Pv = Psat - Pa * Aw * (Ta - Tw)
        return  Pv


    def get_Pv_2(self,Tw,DTi_w):
        '''

        :param Tw:
        :param DTi_w:
        :return:
        '''
        switch ={

            0  :lambda Tw : 0.0007*Tw**3+0.0018*Tw**2+0.5404*Tw+6.1736,
            0.1:lambda Tw : 0.0007*Tw**3+0.0016*Tw**2+0.5502*Tw+6.1788,
            0.2:lambda Tw : 0.0007*Tw**3+0.0014*Tw**2+0.5601*Tw+6.181,
            0.3:lambda Tw : 0.0007*Tw**3+0.002*Tw**2+0.5603*Tw+6.1828,
            0.4:lambda Tw : 0.0007*Tw**3+0.0018*Tw**2+0.5695*Tw+6.1847,
            0.5:lambda Tw : 0.0007*Tw**3+0.0006*Tw**2+0.5947*Tw+6.1777,
            0.6:lambda Tw : 0.0007*Tw**3+0.0005*Tw**2+0.5963*Tw+6.1955,
            0.7:lambda Tw : 0.0007*Tw**3-0.0005*Tw**2+0.6323*Tw+6.1684,
            0.8:lambda Tw : 0.0007*Tw**3+1E-05*Tw**2+0.6198*Tw+6.1961,
            0.9:lambda Tw : 0.0007*Tw**3-0.0002*Tw**2+0.6299*Tw+6.2007,

        }
        try:
            Pv = switch[DTi_w](Tw)
        except :
            return ("参数有误")

        return Pv


    def get_Rw(self,Pv,Pa):
        '''
        湿空气气体常数
        :param Pv:空气中水蒸气分压力
        :param Pa:大气压
        :return:
        '''
        Rw = 287 / (1 - 0.378 * Pv / Pa)
        return  Rw


    def get_Ma(self,v,k,Rw,K):
        '''
        某点的马赫数
        :param v:流体绝对速度
        :param k:等熵指数
        :param Rw:湿空气气体常数
        :return:
        '''
        Ma = v / (k * Rw * K) ** -2
        return  Ma

    def get_Psg(self,p,k,Ma):
        '''
        某点的绝对滞止压力
        :param p:某点绝对压力
        :param k:等熵指数
        :param Ma:该点马赫数
        :return:
        '''
        Psg = p * (1 + (k - 1) / 2 * Ma ** 2) ** (k / (k - 1))
        return  Psg


    def get_Pd(self,D,v):
        '''
        某点的动压
        :param D:某点空气密度
        :param v:某点空气速度
        :return:
        '''
        Pd = D * v ** 2 / 2
        return  Pd

    def get_Pt_Static(self,Psg,Pa):
        '''
        全压(静压)
        :param Pe:某点的绝对滞止压力
        :param Pa:大气压
        :return:
        '''
        Pt = Psg - Pa
        return  Pt

    def get_Pt_Move(self,Pe,Pd):
        '''
        全压(动压)

        :param Pe:表压
        :param Pd:某点的动压
        :return:
        '''
        Pt = Pe + Pd
        return  Pt


    def get_PdF_1(self,D2,vm2):
        '''
        风机动压1
        :param D2:风机出口平均密度
        :param vm2:风机出口流速
        :return:
        '''
        PdF = D2 * vm2 ** 2 / 2
        return  PdF
    def get_PdF_2(self,D2,qm,A2):
        '''
        风机动压2
        :param D2:风机出口平均密度
        :param qm:质量流量
        :param A2:风机出口截面积
        :return:
        '''
        PdF=1/(2*D2)*(qm/A2)**2
        return  PdF


def get_Concentration(Di,DO2i,DO2):
    #大气污染物基准氧含量排放浓度折算
    D = Di * (21 - DO2i) / (21 - DO2)
    return D



############################################# 自动公式文本信息  #############################################
def outfunc(fuc_str:str,*args,**kwargs):
    for k,v in kwargs.items():
         fuc_str= fuc_str.replace(k,str(v))

    res = eval(fuc_str)
    return  res

from math import pow
s= 'pow(16,1/2)'
res = outfunc(s,a=5,b =2)

s  =FuelAnalyzeFunction()


