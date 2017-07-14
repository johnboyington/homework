=edward's pipe problem base case with extras
*m: SNAP:Symbolic Nuclear Analysis Package,  Version 2.4.2, December 11, 2015
*m: PLUGIN:RELAP Version 4.5.8
*m: CODE:RELAP5 Version 3.3
*m: DATE:4/23/17
******************************
*        Model Options       *
******************************
*            type         state
100           new       transnt
*          iunits        ounits
102            si            si
*   tend minstep maxstep copt pfreq majed rsrtf
201 0.02  1.0e-7  1.0e-3    3     2    10   100
202  0.1  1.0e-7  1.0e-3    3    10    20   100
203  0.5  1.0e-7  1.0e-3    3    10    50   100
*        variable     parameter
301             p     003010000
302             p     003050000
303             p     003100000
304             p     003150000
305             p     003200000
306         voidg     003200000
307         voidj     004000000
308        mflowj     004000000
*             Expanded plot records
20800001        errmax             0
20800002        systms             1
**************************************
*       Interactive Variables        *
**************************************
*
*       name       initial         factor
801        x           0.0           1.0
*
*       name       initial         factor
802       xx           5.0           1.0
*
*       name       initial         factor
805      xxx          10.0           1.0
*
20500000           999
*******************************
*       Control Blocks        *
*******************************
*
*          name type scale ival iflag limit
20500100 "ctl1"  sum   0.5  0.0     1     0
*                   a0         scale     name         param
20500101           0.0           1.0        p       3010000
20500102                         1.0        p       3020000
*
*          name type scale ival iflag limit
20500400 "ctl4" mult   0.5  0.0     1     0
*                input         param
20500401             p       3200000
*
*          name type scale ival iflag limit
20500500 "ctl5" mult   1.0  0.0     1     0
*         input   param input   param input   param
20500501 voidgj 4000000 rhogj 4000000 velgj 4000000
*
*           name type scale ival iflag limit
20501000 "ctl10"  div   1.0  0.0     1     0
*                input         param
20501001             p       3200000
*
*           name type scale ival iflag limit
20501100 "ctl10"  div   1.0  0.0     1     0
*                input         param         input         param
20501101             p       3200000             p       3190000
*
*           name     type scale ival iflag limit
20501200 "ctl12" diffreni   1.0  1.0     0     0
*                input         param
20501201          time             0
*
*           name     type scale ival iflag limit
20501300 "ctl13" integral   1.0  0.0     0     0
*                input         param
20501301          time             0
*
*           name     type scale ival iflag limit
20501400 "ctl14" integral   1.0  0.0     0     0
*                input         param
20501401      cntrlvar            12
*
*           name     type scale ival iflag limit
20501500 "ctl15" diffreni   1.0  0.0     1     0
*                input         param
20501501      cntrlvar            13
*
*            name     type scale ival iflag limit
20520100 "ctl201" function   2.0  0.0     1     0
*                input         param         table
20520101          time             0            10
*
*            name     type scale ival iflag limit
20520200 "ctl202" stdfnctn   2.0  0.0     1     0
*                fnctn         input         param
20520201           sin          time             0
*
*            name     type scale ival iflag limit
20520300 "ctl203" tripunit   2.0  0.0     1     0
*                 trip
20520301           501
*
*            name     type scale ival iflag limit
20520400 "ctl204" tripdlay   2.0  0.0     1     0
*                 trip
20520401           501
*
*            name   type scale ival iflag limit min
20520500 "ctl205" poweri   0.5  0.3     1     1 0.2
*                input         param         power
20520501          time             0             2
*
*            name   type scale ival iflag limit max
20520600 "ctl206" powerr   0.5  0.2     1     2 0.3
*                input         param         power
20520601          time             0           2.0
*
*            name   type scale ival iflag limit min max
20520700 "ctl207" powerx   0.5  0.2     1     3 0.1 0.3
*                input         param         input         param
20520701          time             0          time             0
*
*            name  type scale ival iflag limit
20530000 "ctl300" delay   2.0  0.0     1     0
*                input         param         delay          hold
20530001      cntrlvar            13           0.1            10
*
*            name     type scale ival iflag limit
20530100 "ctl301" prop-int  10.0  0.0     1     0
*                   a1            a2         input         param
20530101           2.0           3.0          time             0
*
*            name type scale ival iflag limit
20530200 "ctl302"  lag  10.0  0.0     1     0
*                  lag         input         param
20530201           0.1          time             0
*
*            name     type scale ival iflag limit
20530300 "ctl303" lead-lag  10.0  0.0     1     0
*                 lead           lag         input         param
20530301          0.05           0.1          time             0
*
*                 name          type         value
20530400      "ctl304"      constant         0.387
*
*                 name          type         value
20540100        "con1"      constant           0.0
*
*                 name          type         value
20540200        "con2"      constant           0.1
*
*             name    type scale ival iflag limit
20540300 "pumpctl" pumpctl   1.0  0.0     0     0
*           input param input param scale integral proport
20540301 cntrlvar   401  time     0   1.0      0.0     0.0
*
*              name     type scale ival iflag limit
20540400 "steamctl" steamctl   5.0  2.0     0     0
*           input param input param scale integral proport
20540401 cntrlvar   402  time     0   2.0      0.0     0.0
*
*             name    type scale ival iflag limit
20540500 "feedctl" feedctl   1.0  0.0     0     0
*                 name         param          name         param         scale
20540501      cntrlvar           401          time             0           0.4
*                 name         param          name         param         scale
20540502      cntrlvar           402          time             0           0.5
*              integral    proportion
20540503           0.0           0.0
*
*******************************
*       Variable Trips        *
*******************************
*
*    var param  r  var param     acon l
501 time     0 gt null     0 0.099999 l
*
*   var   param  r var   param acon l
502   p 3010000 lt   p 3020000  0.0 n
*
*     var   param  r   var   param acon l
505 velfj 3010000 ge velgj 3010000  0.0 n
*
******************************
*       Logical Trips        *
******************************
*
*           trip1          oper         trip2             l
601           505           and           501             l
*
*           trip1          oper         trip2             l
602           602            or           601             n
*
*           trip1          oper         trip2             l
603          -505           xor          -501             l
*
*******************************
*       General Tables        *
*******************************
*
*            type          trip
20200400    htc-t             0
*                 TimeHeat Transfer 
20200401           0.0        2000.0
*
*            type          trip
20201000   reac-t             0
*                 Time    Reactivity
20201001          -1.0           0.0
20201002           0.0           0.0
20201003           0.0           1.5
*
*            type          trip
20201100   reac-t           501
*                 Time    Reactivity
20201101          -1.0           0.0
20201102           0.0           0.0
20201103           0.1         -20.0
*
*            type          trip
20233300     temp             0
*                 Time   Temperature
20233301           0.0         333.6
20233302        5000.0         333.0
*
**************************
*       Materials        *
**************************
*
*                 type
20100100       c-steel
*
*                 type         tflag         vflag
20100300      tbl/fctn             2             2
*        lower  upper    a0      a1      a2      a3      a4      a5       c
20100301   0.0    5.0 46.05 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20
20100302   5.0 2000.0 46.05 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20
*        lower  upper       a0      a1      a2      a3      a4      a5       c
20100351   0.0 2000.0 3.8775e6 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20 1.0e-20
*
*                 type         tflag         vflag
20100400      tbl/fctn             1            -1
*                 temp        thcond
20100401           0.0         46.05
20100402        1000.0         46.05
20100403        2000.0         46.05
*        heat capacity
20100451      3.8775e6
20100452      3.8775e6
20100453      3.8775e6
*
*                 type         tflag         vflag
20100500      tbl/fctn             2             2
*        lower  upper    a0  a1  a2  a3  a4  a5   c
20100501   0.0    5.0 46.05 0.0 0.0 0.0 0.0 0.0 0.0
20100502   5.0 2000.0 46.05 0.0 0.0 0.0 0.0 0.0 0.0
*        lower  upper       a0  a1  a2  a3  a4  a5   c
20100551   0.0 2000.0 3.8775e6 0.0 0.0 0.0 0.0 0.0 0.0
*
*                 type
20100600           gap
*
*                 type
20100700       s-steel
*
*                 type
20100800           uo2
*
*                 type
20100900            zr
*
*************************************
*       Hydraulic Components        *
*************************************
*
*                name          type
0030000    "edward's"          pipe
*              ncells
0030001            20
*              x-area         volid
0030101    4.56037e-3            20
*            x-length         volid
0030301      0.204801            20
*              volume         volid
0030401           0.0            20
*          azim-angle         volid
0030501           0.0            20
*          vert-angle         volid
0030601           0.0            20
*              x-wall           xhd         volid
0030801   1.177911e-6           0.0            20
*             x-flags         volid
0031001             0            20
*       ebt press  water-ie  steam-ie void none id
0031201 000 1200000.0 796962.0 25880.0  0.0  0.0 20
*            jefvcahs       jun num
0031101      00000000            19
*                  vl            vv        unused         junid
0031301           0.0           0.0           0.0            19
*
*                name          type
0040000      "rhtbdy"       sngljun
*                from            to          area
0040101       3200002       5010001    3.96752e-3
*           fwd. loss     rev. loss       efvcahs
0040102           0.0           0.0             0
*           discharge       thermal       
0040103           1.0          0.14
*                flow            vl            vv        unused
0040201             0           0.0           0.0           0.0
*
*                name          type
0050000      "rhtbdy"       tmdpvol
*                area        length           vol
0050101    4.56037e-3      0.204801           0.0
*            az-angle     inc-angle            dz
0050102           0.0           0.0           0.0
*             x-rough          x-hd         flags
0050103   1.177911e-6           0.0             0
*               cword          trip
0050200             2           501
*                srch         press         squal
0050201           0.0         1.0e5           1.0
0050202         100.0         1.0e5           1.0
*
********************************
*       Heat Structures        *
********************************
*
*          nh   np      geom      ssif     leftcoord reflood
10030000   20   11         2         1        0.0381       0
*                 mesh        format
10030100             0             1
*            intervals        radius
10030101            10        0.0441
*             material      interval
10030201             1            10
*                 rpkf      interval
10030301           0.0            10
*          temp source
10030400             0
*                 temp      interval
10030401         500.0            11
*   Left Boundary Condition Data 
*            bound      incr      type      code        factor      node
10030501   3010000         0       101         1      0.204801         1
10030502   3020000         0       101         1      0.204801         2
10030503   3030000         0       101         1      0.204801         3
10030504   3040000         0       101         1      0.204801         4
10030505   3050000         0       101         1      0.204801         5
10030506   3060000         0       101         1      0.204801         6
10030507   3070000         0       101         1      0.204801         7
10030508   3080000         0       101         1      0.204801         8
10030509   3090000         0       101         1      0.204801         9
10030510   3100000         0       101         1      0.204801        10
10030511   3110000         0       101         1      0.204801        11
10030512   3120000         0       101         1      0.204801        12
10030513   3130000         0       101         1      0.204801        13
10030514   3140000         0       101         1      0.204801        14
10030515   3150000         0       101         1      0.204801        15
10030516   3160000         0       101         1      0.204801        16
10030517   3170000         0       101         1      0.204801        17
10030518   3180000         0       101         1      0.204801        18
10030519   3190000         0       101         1      0.204801        19
10030520   3200000         0       101         1      0.204801        20
*   Right Boundary Condition Data 
*            bound      incr      type      code        factor      node
10030601         0         0         0         1      0.204801         1
10030602         0         0         0         1      0.204801         2
10030603         0         0         0         1      0.204801         3
10030604         0         0         0         1      0.204801         4
10030605         0         0         0         1      0.204801         5
10030606         0         0         0         1      0.204801         6
10030607         0         0         0         1      0.204801         7
10030608         0         0         0         1      0.204801         8
10030609         0         0         0         1      0.204801         9
10030610         0         0         0         1      0.204801        10
10030611         0         0         0         1      0.204801        11
10030612         0         0         0         1      0.204801        12
10030613         0         0         0         1      0.204801        13
10030614         0         0         0         1      0.204801        14
10030615         0         0         0         1      0.204801        15
10030616         0         0         0         1      0.204801        16
10030617         0         0         0         1      0.204801        17
10030618         0         0         0         1      0.204801        18
10030619         0         0         0         1      0.204801        19
10030620         0         0         0         1      0.204801        20
*               source          mult          dmhl          dmhr           num
10030701             0           0.0           0.0           0.0            20
*   Left Additional Boundary Condition Data 
10030800             0
*        hthd hlf hlr gslf gslr glcf glcr lbf node
10030801  0.0 3.0 3.0  0.0  0.0  0.0  0.0 1.0   20
*
*          nh   np      geom      ssif     leftcoord reflood
10200000    1   11         1         0           0.0       0
*                 mesh        format
10200100             0             1
*            intervals        radius
10200101            10        6.0e-3
*             material      interval
10200201             4             5
10200202             5            10
*                 rpkf      interval
10200301           0.0            10
*          temp source
10200400             0
*                 temp      interval
10200401          10.0             1
10200402         9.877             2
10200403         9.511             3
10200404          8.91             4
10200405          8.09             5
10200406         7.071             6
10200407         5.878             7
10200408          4.54             8
10200409          3.09             9
10200410         1.564            10
10200411           0.0            11
*   Left Boundary Condition Data 
*            bound      incr      type      code        factor      node
10200501         0         0         0         0         0.122         1
*   Right Boundary Condition Data 
*            bound      incr      type      code        factor      node
10200601         0         0      1333         0         0.122         1
*               source          mult          dmhl          dmhr           num
10200701             0           0.0           0.0           0.0             1
*
******************************
*       Point Kinetics       *
******************************
*                 type      feedback
30000000         point      separabl
*                decay         power         react           dnf
30000001      gamma-ac         1.0e6           0.0         200.0
*                power          time         tunit
30000401         1.0e6         200.0            wk
*              control
30000011            10 * General Table 10
30000012            11 * General Table 11
*              density    reactivity
30000501           0.0         -20.0
30000502           1.0           0.0
*                 temp    reactivity
30000601         300.0          20.0
30000602         400.0           1.0
30000603         500.0           0.0
30000604         600.0          -1.0
*               volume     increment        factor          coef
30000701       3010000             0          0.25           0.0
30000702       3020000             0           0.5           0.0
30000703       3030000             0          0.25           0.0
*                 heat     increment        factor          coef  
30000801         30001             0           0.3           0.0
30000802         30002             0           0.4           0.0
30000803         30003             0           0.3           0.0
.
