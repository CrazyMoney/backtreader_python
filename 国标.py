from functools import reduce
from math import log, pi, exp

############################### 公用函数(累加)  ###############################

#累加函数 ∑(l1+l2)
def summation_fuc(l):
    ans = reduce(lambda x,y :x+y,l)
    return  ans

#累加两个向量相加 ∑(l1+l2)
def summation_summary_func(l1,l2):
    if not len(l1) == len(l2):
        return "数据有误"
    res = []
    for i in range(len(l1)):
        res.append(l1[i] + l2[i])

    ans = reduce(lambda x, y: x + y, res)
    return  ans

#累加两个向量相乘   ∑(l1*l2)
def summation__multiply_fuc(l1,l2):
    if not len(l1) == len(l2):
        return  "数据有误"
    res = []
    for i in range(len(l1)):
        res.append(l1[i]*l2[i])

    ans = reduce(lambda x,y:x+y ,res)
    return  ans






############################### 国标函数   ###############################
class  SurfaceFeedHeater():
    # 表面式加热器
    def get_Hwbmjr(self,Hwo,Hwi):
        #表面式加热器给水焓升
        Hwbmjr = Hwo - Hwi
        return  Hwbmjr

    def get_Qbmjr(self,Iebmjr,Isbmjr):
        #表面式加热器抽汽放热
        Qbmjr = Iebmjr - Isbmjr
        return  Qbmjr

    def get_Hsbmjr(self,Hsbmjr1,Hsbmjr2):
         #表面式加热器疏水放热
         Hsbmjr = Hsbmjr1 - Hsbmjr2
         return  Hsbmjr
    def get_Qfbmjr(self,Ifbmjr,Isbmjr):
        #表面式加热器辅汽放热
        Qfbmjr = Ifbmjr - Isbmjr
        return  Qfbmjr

    def get_Gsbmjr(self,GsbmjrA,GsbmjrB,GsbmjrC,GsbmjrD):
        #表面式加热器疏水流量
        Gsbmjr = GsbmjrA + GsbmjrB + GsbmjrC + GsbmjrD
        return  Gsbmjr
class   Mixing_Heater():
    #混合式加热器

    def get_Gshhjr(self,Gshhjr1 ,Gshhjr2 , Gshhjr3 , Gshhjr4):
        #混合式加热器疏水放热流量

        Gshhjr = Gshhjr1 + Gshhjr2 + Gshhjr3 + Gshhjr4
        return Gshhjr

    def get_Qehhjr(self,Iehhjr ,Hwhhjri):
        #混合式加热器抽汽放热量
        Qehhjr = Iehhjr - Hwhhjri
        return  Qehhjr

    def get_Gehhjr(self,Gwhhjro , Hwhhjro ,Gshhjr ,Hshhjr, Gwhhjri , Hwhhjri, Qehhjr):
        #混合式加热器抽汽流量
        Gehhjr = ((Gwhhjro * Hwhhjro - Gshhjr * Hshhjr) - Gwhhjri * Hwhhjri) / Qehhjr
        return  Gehhjr






class Statistics():
    #t 统计类
    def get_Tdcs(self,Tbh ,Two):
        # 表面式加热器上端差
        Tdcs = Tbh - Two
        return  Tdcs


    def ge_(self,Ts , Twi):
        #表面式加热器下端差

        Tdcs = Ts - Twi
        return  Tdcs

    def get_Tdc(self,Tdc1,Tdc2, Tdc3 , Tdc4 , Tdc5 ,Tdc6 , Tdc7 ,Tdc8 , Tdc9):
        #加热器指标合计值
        Tdc = Tdc1 + Tdc2 + Tdc3 + Tdc4 + Tdc5 + Tdc6 + Tdc7 + Tdc8 + Tdc9
        return  Tdc


class Cold_Side():
    #冷端

    def  get_cxh(self,Txh):
        #循环水平均比热
        cxh = 4.166 + 1.52 / 10 ** 3 * Txh - 2.06 / 10 ** 5 * Txh ** 2
        return  cxh

    def get_Dtdswysj(self,Z1,Z2):
        #对数温差
        Dtdswysj = log(Z1 / Z2)
        return  Dtdswysj


    def get_ksj(self,Gxh ,cxh , Dtdswysj, Fw):
        #实际传热系数
        ksj = 1000 * Gxh * cxh * Dtdswysj / Fw
        return  ksj




    def get_Ths(self,Txhi):
        #华氏温度
        Ths = 1.8 * Txhi + 32
        return Ths



    def get_Rt(self,Ths):
        #冷却水温度修正系数
        if Ths<=60:
            Rt = -5.468E-05 * Ths ** 2 + 1.4904E-02 * Ths + 0.23114
        elif  Ths>60 and Ths<=80:
            Rt = 5.556E-06 * Ths ** 3 - 1.3046E-03 * Ths ** 2 + 0.1063 * Ths - 1.9541
        else:
            Rt = 5.156E-07 * Ths ** 3 - 1.7424E-04 * Ths ** 2 + 0.021562 * Ths + 0.17049
        return  Rt

    def get_Di(self,Do,Ddo):
        #内径
        Di = Do - 2 * Ddo
        return  Di


    def get_Fn(self,Di):
        #凝汽器冷却管截面积(冷却水流通面积)
        Fn = (Di / 2) ** 2 * pi
        return  Fn


    def get_wxh(self,Gxh,vxh,n,nlc,Fn):
        #循环水流速
        wxh = 1000 * Gxh * vxh / (3600 * n / nlc * Fn)
        return  wxh

    def get_kqj(self,c,Rm,Rt,wxh):
        #清洁传热系数
        kqj = 3600 * c * Rm * Rt * wxh ** 0.5
        return  kqj

    def get_Rcn_(self,ksj , kqj):
        #凝汽器洁净系数
        Rcn = ksj / kqj
        return  Rcn

    def get_DTwyb(self,Qn , Fw , kqj , Rcnd):
        DTwyb = Qn / (Fw * kqj * Rcnd)
        return  DTwyb

    def get_DTdswyb(self, DTxh , Dtwyb):
        #凝汽器基准状态下温压
        DTdswyb = DTxh / Dtwyb
        return  DTdswyb



    def get_mm(self,DTdswyb):
        #凝汽器基准状态下对数温差比
        mm = exp(DTdswyb)
        return  mm

    def get_Tbhb2(self,mm , Txho , Txhi):
        #凝汽器基准状态下饱和温度
        Tbhb2 = (mm * Txho - Txhi) / (mm - 1)
        return  Tbhb2

    def get_z(self,n,vxh,wxh,Di,m,Gni):
        #循环水流程数
        z = (pi * n / vxh * wxh * Di ** 2) / (4 * m * Gni / 3600)
        return  z

    def get_DPxh(self,z,b,c,L,wxh):
        #凝汽器水阻
        DPxh = z * (b * c * L / 1000 * wxh ** 1.75 + 0.135 * wxh ** 1.5) * 9.81
        return  DPxh

    def get_Tngl(self,Tbhdp , Tns):
        #过冷度
        Tngl = Tbhdp - Tns
        return  Tngl

    def get_hzk(self,Pc,Pam):
        #真空度
        hzk = abs((Pc - Pam)/Pam)*100
        return  hzk

    def get_Qi(self,P,M,C,T):
        #循环系统排出热量
        Qi = P + (M * C * T)
        return   Qi


class Pump():
    #泵


    def get_W(self,N):
        #角速度
        W = 2 * pi * N
        return W

    def get_Q(self,q,Rho):
        #体积流量

        Q = q / Rho
        return  Q



    def get_U(self,Q,A):
        #平均速度
        U = Q / A
        return U


    def get_H(self,y,g):
        #水头
        H = y / g
        return  H



    def get_Hs(self,U,g):
        #速度水头
        Hs = U ** 2 / (2 * g)
        return  Hs



    def get_Hx(self,Zx,Px,Rho,g,Ux):
        #总水头
        Hx = Zx + Px / (Rho * g) + Ux ** 2 / (2 * g)
        return Hx

    def get_Hx_Absolute(self,Zx,Px,Rho ,g,Pamb,Ux ):
        #绝对总水头
        Hx = Zx + Px / (Rho * g) + Pamb / (Rho * g) + Ux ** 2 / (2 * g)
        return  Hx

    def get_H1(self,Z1,P1,Rho , g ,U1):
        #入口水头
        H1 = Z1 + P1 / (Rho * g) + U1 ** 2 / (2 * g)
        return  H1

    def get_H2(self,Z2,P2,Rho ,g , U2):
        #出口水头
        H2 = Z2 + P2 / (Rho * g) + U2 ** 2 / (2 * g)
        return  H2

    def get_Hyc1(self, H2 ,H1):
        #扬程1(压缩性可忽略)
        Hyc1 = H2 - H1
        return  Hyc1

    def get_Hyc2(self,P1,P2,Z1,Z2,U2,U1,g):
        #扬程2(压缩性不可忽略)
        Pm = (P1 + P2) / 2
        Hyc2 = Z2 - Z1 + (P2 - P1) / (Pm * g) + (U2 ** 2 - U1 ** 2) / (2 * g)
        return  Hyc2

    def get_NPSH(self,H1,Zd,Pamb,Pv,Rho1 , g):
        #汽蚀余量
        NPSH = H1 - Zd + (Pamb - Pv) / (Rho1 * g)
        return  NPSH

    def get_y(self,g ,H):
        #比能
        y = g * H
        return  y

    def get_K(self,n,Q,g,H):
        #型式数
        K = (2 * pi * n * Q**(1/2)) / ((g*H) ** (3 / 4))
        return K

    def get_Ph(self,Rho ,Q , g , H):
        #泵输出功率
        Ph = Rho * Q * g * H
        return  Ph

    def get_Eta(self,Ph ,P2):
        #泵效率
        Eta= Ph / P2
        return Eta

    def get_Eta_Total(self, Ph ,Pgr):
        #泵总效率
        Eta = Ph / Pgr
        return  Eta



    def get_P(self,Pm , Rho1 ,g ,Zm , Z):
        #压力修正
        P = Pm + Rho1 * g * (Zm - Z)
        return  P


class Efficiency():
    #效率

    def get_Eta_Heat_1(self, P ,Mi, Deltah:list):
        #热效率1
        Eta  = P /Mi * summation_fuc(Deltah)
        return Eta



    def get_Eta_Heat_2(self, P,M1 , H1 , H11, M3 , H3 ,H2):
        #热效率2
        Eta = P / (M1 * (H1 - H11) + M3 * (H3 - H2))
        return  Eta

    def get_Eta_td(self, Pb,M1,Hs1):
        td=Pb/(M1*Hs1,4)
        return  td
    def get_Eta_(self, Pb,M1,Hs1):

        td=Pb/(M1*Hs1,4)
        return  td

    def get_Eta_tsdd(self, Mj:list,hsj:list,P):
        #抽汽式分级计算效率
        td=P/summation__multiply_fuc(Mj,hsj)
        return  td

    def get_cyl(self,Hin,Hout,Hs):
        #缸效
        cyl = (Hin - Hout) / Hs
        return  cyl


class General():
    #通用
    def get_FPC(self, Min, Pin,Vin,Pout):
        #通流能力
        FPC =  (Min/(Pin/Vin)**-2) * ((1-(Pout/Pin))**2 -2 )
        return  FPC




class  LowPressureCylinder():
    #低压缸
    def get_Plp(self,Pi,Php,Pip):
        #低压缸功率
        Plp = Pi - Php - Pip
        return  Plp


    def get_Min(self,Mei:list,M4:list):
        #低压缸进口流量
        Min = summation_summary_func(Mei,M4)
        return Min

    def get_Plp_Alxe(self,Mei,M4,hueep):
        #低压缸轴功率
        Plp =summation_summary_func(Mei,M4)+ M4 * hueep
        return Plp


    def get_ueep_1(self,Hin,Hueep,Hsp):
        #效率1(有效能终点焓)
        ueep=(Hin-Hueep)/Hsp
        return ueep


    def get_elep_2(self,Hin,Helep,Hs):
        #效率2(膨胀线终点焓)
        uelep=(Hin-Helep)/Hs
        return uelep

    def get_loss(self,Hueep,Helep):
        #排汽损失
        loss =Hueep-Helep
        return loss


class  Condenser():
    #凝汽器


    def get_Q_(self,W,Cp,T2,T1):
        #凝汽器热负荷
        Q = W * Cp * (T2 - T1)
        return  Q



    def get_LMTD(self,T2,T1,Ts):
        #对数平均温差
        LMTD = (T2 - T1) / log((Ts - T1) / (Ts - T2))
        return  LMTD

    def get_U_(self,Q,LMTD):
        #总体传热系数
        U = Q / (Q * LMTD)
        return U

    def get_Rm(self,Do,km,Di):
        #冷却管管壁热阻
        Rm = Do / (2 * km) * log(Do / Di)
        return  Rm



    def get_Re(self,Rho ,V,Di,u):
        #雷诺数
        Re = (Rho * V * Di) / u
        return Re

    def get_Pr(self,Cp,u,K):
        #普朗特数
        Pr = (1000 * Cp * u) * K
        return Pr


    def get_V(self,W,Rho,N,n,Di):
        #测量冷却水流速
        V = W / (3600 * Rho * (N / n) * (pi / 4) * (Di ** 2))
        return V



    def get_Rt_(self,k,Di,Re,Pr):
        #冷却管管侧热阻
        Rt = (0.0158 * (k / Di) * (Re ** 0.835) * (Pr ** 0.462)) ** -1
        return Rt

    def get_Tb(self,T2,T1):
        #循环水平均水温
        Tb = 0.5 * (T2 - T1)
        return  Tb


    def get_Rf_i (self,Ao,n,W,Cp,Ts,T1f_i,T2f_i,T1c_i,T2c_i):
        #管束i的污垢热阻
        Rf_i = Ao / (n * W * Cp) * ((1 / log((Ts - T1f_i) / (Ts - T2f_i))) - (1 / log((Ts - T1c_i) / (Ts - T2c_i))))
        return Rf_i

    def get_Rf(self,J,Rf_i:list):
        #污垢热阻
        Rf = (1 / J) *summation_fuc(Rf_i)
        return  Rf

    def get_Rs(self,U,Rm,Rt,Do,Di,Rf):
        #壳侧热阻
        Rs = (1 / U) - Rm - Rt * (Do / Di) - Rf
        return  Rs

    def get_Rex(self,Rhox,Vx,Di,ux):
        #设计雷诺数
        Rex=(Rhox * Vx * Di) / ux
        return Rex



    def get_Prx(self,Cpx,ux,kx):
        #设计普朗特数
        Prx=(1000*Cpx*ux)*kx
        return Prx


    def get_Vx(self,Wx,px,N,n,Di):
        #设计测量冷却水流速
        Vx=Wx/(3600*px*(N/n)*(pi/4)*(Di^2))
        return Vx

    def get_Rt(self,kx,Rex,Prx,Di):
        #设计冷却管管侧热阻
        Rt = (0.0158 * (kx / Di) * (Rex ** 0.835) * (Prx ** 0.462)) ** -1
        return Rt




    def get_LMTDx(self,T2x,Tsx,T1x,):
        #设计对数平均温差
        LMTDx=(T2x-T1x) / log((Tsx-T1x) / (Tsx-T2x))
        return LMTDx

    def get_Ux(self,Qx,Ao,LMTDx):
        #设计总体传热系数
        Ux=Qx / (Ao * LMTDx)
        return Ux

    def get_Rfx(self,Cfx,Ux):
        #设计污垢热阻
        Rfx=(1 - Cfx) / Ux
        return Rfx

    def get_Rsx(self,Rsx,Ws,Wsx,u,ux,kx,k,Rhox,Rho):
        #修正后的壳侧热阻
        Rsx=Rsx*(Ws / Wsx) ** (1 / 3) * (u / ux) ** (1 / 3) * (kx / k) * (Rhox / Rho) ** (2 / 3)
        return Rsx

    def get_TFx(self,Tsx,LMTDx):
        #设计凝结层平均温度
        TFx=Tsx-0.2 * LMTDx
        return TFx

    def get_TF(self,Ts,LMTD):
        #凝结层平均温度
        TF=Ts-0.2 * LMTD
        return TF

    def get_Uo(self,Rmx,Do,Di,Rfx,Rso,Rtx):
        #修正后的总体传热系数
        Uo=1 / (Rmx+Rtx * (Do / Di) + Rfx+Rso)
        return  Uo


    def get_NTUo(self,Uo,Ax,Cpx,wx):
        #修正后传热单元数
        NTU0=(Uo * Ax) / (Cpx * wx)
        return  NTU0



    def get_Tso(self,T2x,T1x,NTUo,e,):
        #修正后凝汽器温度
        Tso=((T2x-T1x) * e ** (-NTUo)) / (1 - e ** (-NTUo))
        return Tso

    def get_Ps(self,Psx,Pso):
        #凝汽器压差(修正后压力与设计压力)
        Ps = Psx-Pso
        return Ps
class Deaerator():
    def get_TTD(self,th,t2):
        #端差
        TTD = th - t2
        return  TTD

    def get_balance_1(self,Wsp,hs,hfx,Ww,h1,hdl,hfs,Wf,hf,Wdn,Wdl,hdn):
        #除氧器热平衡1
        ans = Wsp * (hs - hfs) + Ww * (h1 - hfs) + Wdl * (hdl - hfs) + Wf * (hf - hfs) + Wdn * (hdn - hfs)
        return  ans
    def get_banance_2(self,Ws,hs,h2,h1,Wdl,hdl,Wf,hf,Wdn,hdn,Ww):
        #除氧器热平衡2
        ans = Ws*(hs-h2)+Ww*(h1-h2)+Wdl*(hdl-h2)+Wf*(hf-h2)+Wdn*(hdn-h2)
        return ans

    def get_Q(self,Ww,Wdl,Wf,Wdn,h2,h1,hdl,hdn,hf):
        #除氧器热负荷
        Q = (Ww + Wdl + Wf + Wdn) * h2 - (Ww * h1 + Wdl * hdl + Wf * hf + Wdn * hdn)
        return Q

    def get_DOis(self,DOi,Doio):
        #空白试样测量值
        DOis = DOi + Doio
        return DOis

    def get_DO(self,Dots,Dois,Dor):
        #水中溶解氧
        DO = Dots - (Dois + Dor)
        return DO

    def get_DOts(self,DO,DOi,DOr,DOio):
        #总的溶解氧
        DOts = DO + DOi + DOr + DOio
        return  DOts

    def get_balabce(self,V,Vi,Vts,Vr,Vio):
        #平衡方程
        ans = V + Vi  - Vts + (Vr + Vio)
        if ans  ==  0:
            return True
        else:
            return  False

    def get_Vio(self,cio,cpao):
        #相当于随试剂加入试验样中溶解氧的氧化苯胂标准滴定溶液体积
        Vio = 2 * cio / cpao
        return  Vio

    def get_balabce2(self,V,Vi,Vts,cio,cpao):
        #相当于2号试剂加入两个试样任一个中的游离碘的氧化苯胂标准滴定溶液体积
        ans  =  V + Vi -(Vts + ((0.000652 + 2 * cio) / cpao))
        return

    def get_Dots(self,cpao,V,Vi,Vjts):
        # #计算试验试样中的溶解氧和干扰物得空白值相当的溶解氧
        Dots = 8000000 * cpao * (V + Vi) / Vjts
        return Dots



    def get_Vi_balance(self,cio,cpao,Vi,Vis):
        #相当于两者中任一试样干扰物空白值的氧化苯胂标准滴定溶液体积
        ans  =(Vis-2*cio/cpao) -Vi
        if ans == 0:
            return True
        else:
            return False


    def get_Doi(self,cpao,Vi,Vji):
        #水中干扰物的空白值
         Doi = 8000000 * cpao * Vi / Vji
         return  Doi

    def get_D0(self,Dots,Doi):
        #水中净溶解氧
        D0 = Dots - Doi
        return D0


class Heater():
    #加热器
    def get_TYL(self,Hyx,Hgj):
        #投运率
        TYL = (Hyx - Hgj) / Hyx
        return TYL



class PipeValvesflangesAndCounterflanges():
    #管道、阀门、孔板


    def get_Pt(self,Kpn,PN,Deltat,Deltas):
        #设计温度下的允许工作压力
        Pt = Kpn * PN * Deltat / Deltas
        return Pt

    def get_Sm_pipe_out(self,P,Do,Delta,Eta,Y,C):
        #按管子外径确定壁厚
        Sm = (P * Do)/ (2 * Delta*Eta+2*P*Y)+C
        return Sm

    def get_Sm_pipe_in(self,P,Di,Delta,Eta,C,Y):
        #按管内外径确定壁厚
        Sm = (P * Di + 2 * Delta*Eta*C+2*P*Y)/(2*Delta * Eta-2 * P * (1-Y))
        return Sm

    def get_c1(self,m,Sm):
        #管子壁厚负偏差附加值
        c1 = (m * Sm) / (100 - m)
        return c1

    def get_Sc(self,Sm,c1):
        #管子计算厚壁
        Sc = Sm + c1
        return Sc

    def get_I_in(self,R,Do):
        #弯管和弯头内弧处
        I = (4 * R / Do - 1) / (4 * R / Do - 2)
        return I

    def get_I_out(self,R,Do):
        #弯管和弯头外弧处
        I = (4 * R / Do + 1) / (4 * R / Do + 2)
        return  I


    def get_Sm__out(self,P,Do,Delta,Eta,Y,C,I):
        #按管外径确定壁厚
        Sm = (P * Do) / (2 * Delta*Eta/I+2*P*Y)+C
        return Sm


    def get_Sm_in(self,P,Di,Delta,Eta,I,Y,C):
        #按管内外径确定壁厚
        Sm = (P * Di + 2 * Delta*Eta*C/I+2*P*Y)/(2*(Delta* Eta / I+Y * P-P))
        return  Sm

    def get_(self,Dob,Sb):
        #主管上经加工的支管开孔沿纵向中心线尺寸
        d1 = Dob - 2 * Sb
        return d1

    def get_A2(self,Lb,Sb,Smb):
        #补强范围内支管的补强面积
        A2 = 2 * Lb * (Sb - Smb)
        return    A2
    def get_A1(self,Lh,d1,Sh,Smh):
        #补强范围内主管的补强面积
        A1 = (2 * Lh - d1) * (Sh - Smh)
        return  A1

    def get_A_(self,Smh,d1):
        #需要补强的面积
        A = Smh * d1
        return  A

    # def get_(self,):
    #     A1 + A2 + A3 > A
    #     return  A1

    def get_Dm(self,Do,S):
        #异径管平均直径；mm
        Dm = Do - S
        return Dm



    def get_Sm1(self,P,Dm,Delta,Eta,Y,p,C,cos_Th):
        #异径管壁厚(Sm1、Sm2取最小值
        Sm1 = (P * Dm + 2 * Delta*Eta*C+2*Y*P*C)/(2*Delta * Eta-2 * p * (1-Y) * cos_Th)
        return  Sm1

    def get_Sm2(self,Do,P,Delta,Eta,p,Y,C):
        #异径管壁厚(Sm1、Sm2取最小值)
        Sm2 = (P * Do) / (2 * Delta*Eta+2*p*Y)+C
        return  Sm2


    def get_Sm(self,dG,P,Delta,Eta):
        #法兰在压力作用下的设计厚度
        Sm = dG(3 * P / (16 * Delta*Eta))**0.5
        return Sm

    def get_S(self,Sm,C):
        #法兰盲板厚度
        S = Sm + C
        return S

    def get_Sm1_max(self,K,P,Di,C,Delta,Eta):
        #最小壁厚(椭球型封头，取Sm1、Sm2较大值)
        Sm1 = (K * P * Di) / (2 * Delta*Eta-0.5*P)+C
        return  Sm1


    def get_Sm2_max(self,K,P,Di,Y,C,p,Delta,Eta):
        #最小壁厚(椭球型封头，取Sm1、Sm2较大值)
        Sm2 = K * (P * Di + 2 * Delta*Eta*C+2*p*Y*C)/(2*Delta * Eta-2 * P * (1-Y))
        return  Sm2

    def get_Sm_max(self,K,Di,P,Delta,Talent):
        #对焊封头和平封头壁厚
        Sm = K*Di*(P/(Delta * Talent))**0.5
        return Sm

    # def get_(self):
    #     {Deltacp = P * (0.5 * Do - Y * (Ss - C)) / (Eta * (Ss - C))} <= 1.0 * Delta
    #     return
    def get_W(self,Do,Di):
        #管子截面抗弯矩
        W = pi / (32 * Do) * (Do ** 4 - Di ** 4)
        return W

    def get_N(self,NE,n,r):
        #管道全温度周期性的交变次数
        ans  = 0
        l = len(n)
        try:
            for i  in range(l):
                ans = r[i]*85 *n[i] +ans
        except Exception as e :
            ans = "输入参数有误"
        return ans


    #
    # def get_(self):
    #     {DeltaL = (P * Di ** 2) / (Do ** 2 - Di ** 2) + 0.75 * (i * MA) / W} <= 1.0 * Delta
    #     '
    #     return Ellipsis
    # def get_(self):
    #     (P * Di ** 2) / (Do ** 2 - Di ** 2) + 0.75 * (i * MA) / W + 0.75 * (i * MB) / W <= K * Delta
    #     return PendingDeprecationWarning
    # def get_(self,i,Mc,W,f,DeltaL):
    #     DeltaE = i * Mc / W <= f * (1.2 * [Delta]20+0.2 *[Delta]+([Delta]-DeltaL)))
    #     return DeltaE
    def get_Deltamax_stress(self,q,L,Pj,W):
        #水平直管最大弯曲应力(一般钢管的自重应力不宜大于16MPa)
        Deltamax = ((q * L + 2 * Pj) * W) / (8 * W)
        return Deltamax

    def  get_L(self,Pj,q,W,Deltamax):
        #支吊架间距(按强度条件确定)
        L = ((Pj ** 2 + 8 * q * W * Deltamax) ** 0.5 - Pj) / q
        return L

    def get_Deltamax_angle(self,L,Et,I,Pj,q):
        #最大挠度(按刚度条件确定)
        Deltamax = L ** 3 / (Et * I) * (5 / 384 * q * L + 1 / 48 * Pj) * 10 ** 5
        return Deltamax

    def get_mu(self,Dmax,Dmin):
        #弯管的圆度偏差
        mu = (Dmax - Dmin) / Dmax * 100
        return mu

    def get_A_Full(self,dt):
        #安全阀最小泄放面积(全启式)
        A = pi / 4 * dt ** 2
        return A

    def get_A_LowFlat(self,dv,h):
        #安全阀最小泄放面积(微启式平面型密封面)
        A = pi * dv * h
        return A

    def get_A_LowTaper(self,dt,h,sinx):
        #安全阀最小泄放面积(微启式锥面型密封面)
        A = pi * dt * h * sinx
        return A



    def get_C_air(self,k):
        #气体特性指数
        C = 520 * (k * (2 / (k + 1)) ** ((k + 1) / (k - 1)))
        return C

    def get_Ws(self,H,q):
        #安全泄放量
        Ws = H / q
        return Ws

    def get_po_balance(self,k,po,pd):
        #安全阀最小泄放面积临界条件(蒸汽)
        ans = ( (2 / (k + 1)) ** (k / (k - 1)) )- (po / pd)
        if ans >= 0:
            return True
        else:
            return False


    def get_A_min(self,Ws,C,K,Pd,M,Z,T):
        #安全阀最小泄放面积(临界；蒸汽)
        A = Ws / (0.076 * C * K * Pd * (M / (Z * T)) ** 0.5)
        return A

    def get_pd_balance(self,po,pd,k):
        #安全阀最小泄放面积亚临界条件(蒸汽)
        ans  =  po/pd -( (2 / (k + 1)) ** (k / (k - 1)))
        if ans >0:
            return True
        else:
            return False




    def get_A_MinSteam(self,K,Pd,M,Z,T,k,po,pd,Ws):
        #安全阀最小泄放面积(亚临界；蒸汽)
        A = Ws / (55.84 * K * Pd * (M / (Z * T)) ** 0.5 * (
                    k / (k - 1) * ((po / pd) ** (2 / k) - (po / pd) ** ((k + 1) / k))) ** 0.5)
        return A

    def get_A_MinWater(self,Ws,K,pd,po ,Rho1):
        #安全阀最小泄放面积(水)
        A = Ws / (5.1 * K * (Rho1 / (pd - po)) ** 0.5)
        return A

    def get_A_SaturatedSteam(selfA,Ws,K,pd):
        #安全阀最小泄放面积(饱和蒸汽pd<=10MPa)
        if pd < 10:
            A = Ws / (5.25 * K * pd)
        else:
            A = Ws / (5.25 * K * pd * ((190.6 * pd - 6895) / (229.2 * pd - 7315)))
        return A


    def get_Beta(self,d,D):
        #直径比
        Beta = d / D
        return Beta

    def get_Tau(self,P1,P2):
        #压力比
        Tau = P2 / P1
        return Tau



    def get_A_outflow(self,Beta,ReD):
        #流出系数计算用A
        A = (19000 * Beta / ReD) ** 0.8
        return A

    def get_L1p(self,L1,D):
        #孔板上游端面到上游取压口的距离除以管道直径的商
        L1p=L1/D
        return L1p

    def get_L2p(self,L2,D):
        #孔板下游端面到上游取压口的距离除以管道直径的商
        L2p=L2/D
        return L2p


    def get_M(self,L2,Beta):
        #流出系数计算用Mp
        M=2*L2 / (1 - Beta)
        return M
    def get_C1(self,Beta,Red,ReD,L1,M2p,A,e,):
        #流出系数
        C = 0.5961 + 0.0261 * Beta ** 2 - 0.216 * Beta ** 8 + 0.000521 * (1000000 * Beta / ReD) ** 0.7 + (
                    0.0188 + 0.0063 * A) * Beta ** 3.5 * (1000000 / Red) ** 0.3 + (
                        0.043 + 0.080 * e ** (-10 * L1) - 0.123 * e ** (-7 * L1)) * (1 - 0.11 * A) * (
                        Beta ** 4 / (1 - Beta ** 2)) - 0.031 * (M2p-0.8*(M2p ** 1.1))*Beta ** 1.3
        return C


    def get_C2(self,Beta,ReD,Red,L1,M2p,A,e,D):
        #流出系数(D<71.12mm)
        C = 0.5961 + 0.0261 * Beta ** 2 - 0.216 * Beta ** 8 + 0.000521 * (1000000 * Beta / ReD) ** 0.7 + (
                    0.0188 + 0.0063 * A) * Beta ** 3.5 * (1000000 / Red) ** 0.3 + (
                        0.043 + 0.080 * e ** (-10 * L1) - 0.123 * e ** (-7 * L1)) * (1 - 0.11 * A) * (
                        Beta ** 4 / (1 - Beta ** 2)) - 0.031 * (M2p-0.8*(M2p ** 1.1))*Beta ** 1.3 + 0.011 * (0.75 - Beta)*(2.8 - D / 25.4)
        return C

    def get_Eps(self,Beta,p2,p1,k):
        #可膨胀系数
        Eps = 1 - (0.351 + 0.256 * Beta ** 4 + 0.93 * Beta ** 8) * (1 - (p2 / p1) ** (1 / k))
        return  Eps

    def get_Epsk(self,DeltaP,k,P1):
        #可膨胀系数不确定度
        Epsk = 3.5 * (DeltaP / (k * P1))
        return Epsk


    def get_Pressure_loss(self,B,C,P):
        #压力损失
        ans =(((1-B**4*(1-C**2)-C*B**2)**0.5)-C*B**2)/((((1-B**4*(1-C**2)-C*B**2)**0.5)+C*B**2))*P
        return ans



    def get_qm(self,C,Beta,Eps,d,DeltaP,Rho1):
        #质量流量
        qm = C / (1 - Beta ** 4) ** 0.5 * Eps * pi * 0.25 * d ** 2 * (2 * DeltaP * Rho1) ** 0.5
        return  qm

    def get_qv(self,qm,Rho):
        #体积流量
        qv = qm / Rho
        return qv

    def get_Cbqd1(self,Beta):
        #流出系数不确定度1(对于角接取压)
        Cbqd1 = 0.7 - Beta
        return Cbqd1
    #
    # def get_(self):
    #     Cbqd2 = 0.5
    #     return Cbqd2

    def get_Cbqd3(self,Beta):
        #流出系数不确定度3(对于法兰取压口)
        Cbqd3 = 1.677 * Beta - 0.5
        return Cbqd3


    def get_Cbqd4(self,Beta,D):
        #流出系数不确定度4(D<71.12mm)
        Cbqd4 = 0.9 * (0.75 - Beta) * (2.8 - D / 25.4)
        return Cbqd4

    def get_K1(self,Beta,C):
        #孔板的压力损失系数1
        K = ((1 - Beta ** 4 * (1 - C ** 2)) ** 0.5 / (C * Beta ** 2) - 1) ** 2
        return  K

    def get_K2(self,Deltapa,Rho1,v):
        #孔板的压力损失系数2
        K = Deltapa / (0.5 * Rho1 * v ** 2)
        return K

    def get_K(self,DeltaPc,Rho,v):
        #管束流动整体压力损失系数
        K = DeltaPc / (0.5 * Rho * v ** 2)
        return K


    def get_d(self,dm,dk):
        #修正后节流孔直径
        d = dm * (1 + 0.55 * (dk / dm) ** 2)
        return d

    def get_d_upstream(self,dm,dk):
        #修正后节流孔直径(排泄孔穿透喷嘴上游端面)
        d = dm * (1 + 0.4 * (dk / dm) ** 2)
        return d


    def get_Cp(self,dk,dm):
        #流出系数不确定度增加量(估算流量测量总不确定度)
        Cp= 0.55 * (dk / dm) ** 2
        return Cp


    def get_C(self,ReD):
        #流出系数C(带角取压接口的直角边缘孔板)
        C = 0.5961 + 0.000521 * (1000000 / ReD) ** 0.7
        return  C


    def get_Eps_Theory(self,p2,p1,k):
        #可膨胀系数(带角取压接口的直角边缘孔板)
        Eps = 1 - 0.351 * (1 - (p2 / p1) ** (1 / k))
        return Eps

    def get_Eps_expansion(self,k,Tau):
        #膨胀系数
        Eps = ((k * Tau ** (2 / k) / (k - 1)) * ((1 - Tau ** ((k - 1) / k)) / (1 - Tau)) ** 1/2)
        return Eps

    def get_Epsb(self,DeltaP,P1):
        #膨胀系数不确定度
        Epsb = 4 * (DeltaP / P1)
        return Epsb

    def get_Red(self,Beta):
        #雷诺数
        Red = 1000 * Beta + 9.4 * 1000000 * (Beta - 0.24) ** 8
        return Red

    def get_Rex(self,dtap,d,ReD):
        #喉部取压口雷诺数
        Rex=dtap / d * ReD
        return Rex

    def get_C_(self,sp,e,Re):
        #流出系数(文丘里管相对粗糙度、喉部雷诺数、喉部取压口雷诺数)
        C = 1.0252 - 2.5 * sp - 0.008 * e ** (-0.4 * Re / 100000)
        return  C

    def get_q(self,T1,Tm,qx):
        #换算后的散热损失
        q = qx*(T1-Tm)/(T1 - Tm)
        return  q


    def get_Ts1(self,Tf,Ta,Tfp,Tap,Tsp):
        #设计工况下保冷结构外表面温度
        Ts=(Tf-Ta)/(Tfp-Tap)*(Tsp-Tap)+Ta
        return  Ts

    def get_Ts2(self,Tf,Ta,Tfp,Tap,Tsp,ap,a):
        #设计工况下保冷结构外表面温度(测试值低于测试工况的露点温度)
        Ts=(Tf-Ta)/(Tfp-Tap)*(ap/a)*(Tsp-Tap)+Ta
        return Ts



    def get_q_longer(self,Tf,Ta,Tfp,Tap,ap,R,a,qp,Rp):
        #设计工况下的冷损失量(设备公称直径大于1m)
        q=((Tf-Ta)/(Tfp-Tap))*((Rp+1/ap)/(R+1/a))*qp
        return q

    def get_q_shorter(self,Tf,Ta,Tfp,Tap,Rp,ap,Dop,Do,qp,R,a):
        #设计工况下的冷损失量(设备公称直径小于1m)
        q=((Tf-Ta)/(Tfp-Tap))*((Rp+1/(ap*pi*Dop))/(R+1/(a*pi*Do)))*qp
        return q


    def get_q1(self,qs,pi,D):
        #单位管长的热损失(对于管道可将单位面积散热损失换算成单位长度的散热损失)
        q1 = qs * pi * D
        return q1

    def get_mw(self,aD,Rhos,Rhoa):
        #凝露时对流传质量
        mw = aD * (Rhos - Rhoa)
        return mw

    def get_q_codeLoss(self,a,Ts,ta,mW,rs):
        #保冷结构凝露表面冷损失量
        q = a * (Ts - ta) + mW * rs
        return q

    def get_t(self,ta,td):
        #特征温度
        t = (ta + td) / 2
        return t

    def get_aD(self,a,cp,Le,Rho):
        #传质系数
        aD = a / (Rho * cp * Le ** (2 / 3))
        return aD

    def get_Rhoa(self,Rhod,Rho,cp,Le,rd,ta,td):
        #环境水蒸气质量浓度
        Rhoa = Rhod - (Rho * cp * Le ** (2 / 3) / rd) * (ta - td)
        return Rhoa



class PipingInsulation():
    #管道保温

    def get_q(self,a,TW,TF):
        #热流密度
        q = a * (TW - TF)
        return q

    def get_a_flat(self,TW,TF):
        #换热系数(平壁，二三级测定)
        a = 9.77 + 0.07 * (TW - TF)
        return a



    def get_a_circle(self,TW,TF):
        #换热系数(圆筒壁，二三级测定)
        a = 9.42 + 0.05 * (TW - TF)
        return a


    def get_a_open_air(self,w):
        #露天布置的设备及管道
        a = 11.63 + 7 * (w ** 0.5)
        return a

    def get_at(self,Eps,Delta,TW,TF):
        #辐射换热系数(一级测定)
        at = Eps * Delta * ((TW ** 4 - TF ** 4) / (TW - TF))
        return at

    def get_DeltaT(self,TW,TF):
        #外壁表面温度和环境温度之差
        DeltaT = TW - TF
        return DeltaT

    def get_T(self,TW,TF):
        #外壁表面温度和环境温度之差
        T = (TW + TF) / 2
        return T


    def get_Beta(self,T):
        #空气膨胀系数
        Beta = 1 / T
        return Beta

    def get_Gr(self,Beta,g,L,DeltaT,v):
        #格拉晓夫数
        Gr = Beta * g * (L ** 3) * DeltaT / (v ** 2)
        return Gr

    def get_acw(self,Nu,a,L):
        #强制对流换热系数
        acw = Nu * a / L
        return acw

    def get_Re(self,L,v,w):
        #雷诺数(风垂直吹向横卧管)
        Re = w * L / v
        return Re

    def get_Nu_convection(self,A,Re,Pr,n):
        #强制对流换热系数(风垂直吹向横卧管)
        Nu = 1.11 * A * (Re ** n) * (Pr ** 0.31)
        return Nu

    def get_Nu_boundary(self,Re,Pr):
        #努塞尔数(层流边界；Re<=500000)
        Nu = 0.664 * (Re ** 0.5) * (Pr ** (1 / 3))
        return Nu

    def get_Nu_turbulence(self,Re,Pr):
        #努塞尔数(紊流边界；Re<=500000)
        Nu = 0.036 * (Re ** (4 / 5)) * (Pr ** (1 / 3))
        return Nu


    def get_a(self,ar,aca):
        #表面换系数(对于室内设备和管道或风速小于0.1m/s的室外设备和管道)
        a = ar + aca
        return a


    def get_a2(self,ar,aca,acw):
        #表面换系数(对于室外设备和管道当0.1<Gr/Re<10)
        a=ar+aca+acw
        return a


class Pump2():
    #泵

    def get_Eh(self,Vm,p2,p1,aa2,U2,aa1,U1,g,z2,z1):
        #水力比能
        Eh = Vm * (p2 - p1) + (aa2 * U2 ** 2 - aa1 * U1 ** 2) / 2 + g * (z2 - z1)
        return Eh

    def get_phi(self,qmi,qm2):
        #单元流路流量与主出口流量比值
        phi = qmi / qm2
        return  phi

    def get_DeltaEm(self,phi,hsi,hei,Usi,Uei,g,zsi,zei):
        #单位质量机械能修正项
        l  = len(hsi)
        sum_  =0
        try:
            for i in range(l):
                sum_ = sum_  + (phi[i] * (hsi[i] - hei[i] + (Usi[i] ** 2 - Uei[i] ** 2)) / 2 + g * (zsi[i] - zei[i]))
        except Exception as e :
            DeltaEm = "输入参数有误"
            return  DeltaEm

        return sum_
    def get_Em(self,h21,h11,aa2,U22,aa1,U11,z11,z21,DeltaEm,g):
        #每单位质量机械能
        Em = h21 - h11 + (aa2 * U22 ** 2 - aa1 * U11 ** 2) / 2 + g * (z21 - z11) + DeltaEm
        return Em

    def get_Eta(self,Em,Ex,Eh):
        #泵效率
        Eta = Eh / (Em + Ex)
        return Eta




































































































































