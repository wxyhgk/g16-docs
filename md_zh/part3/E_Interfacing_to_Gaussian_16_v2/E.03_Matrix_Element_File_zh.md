### E.3 矩阵元文件

矩阵元文件是一种简单的无格式文件,旨在以可扩展的格式交换数据,例如重叠矩阵、核哈密顿矩阵以及双电子积分。它既可以写成适合其他 Fortran 程序处理的 Fortran 无格式文件,也可以写成不带记录标志或长度信息的原始二进制文件,适合在 C/C++/Perl/Python 中处理。该文件格式可以作为通过外部接口(使用 External 关键字)运行的程序的输入和/或输出,也可以由 Gaussian 写成文件,供其他程序单独使用(使用 Output=MatrixElement 或 Output=RawMatrixElement 关键字)。与这些关键字之一结合使用的 Output 各选项,可在文件中选择各种附加数据(例如分子轨道上的双电子积分)。最后,任何 Gaussian 内部文件中的数据,都可以通过 Output=Files 选项包含在矩阵元文件中。矩阵元文件的无格式结构如下。文件开头部分包含与分子结构及其他作业一般特征相关的记录:

**记录格式与说明**

1`Character*64 LabFil, Integer IVers, Integer NLab, Character*64 GVers` 文件类型的标签、文件格式的版本号、位于矩阵元数据之前的通用数据记录数(包括本记录),以及写入该文件的 Gaussian 版本。2`Character*64 Title, Integer NAtoms, Integer NBasis, NBsUse, ICharg, Multip,`

```
NE,Len12L,Len4L,IOpCl,ICGU
```

创建该文件的运行任务中标题部分的前 64 个字符,以及原子数和基函数数。*NBsUse* 为线性无关基函数的数目。*ICharg* 为分子电荷,*Multip* 为自旋多重度(1 = 单重态,依此类推),*NE* 为电子数。*Len12L* 为稀疏一维和二维矩阵整数标签所用的字节数,*Len4L* 为四维矩阵(双电子积分)所用的字节数。若文件以原始模式写入(即所有整数均为 I*4),则 *Len12L* 和 *Len4L* 均为 4,以便与其他语言兼容。

*IOpCl* 为闭壳层/开壳层标志,若矩阵元文件是在初始猜测或 SCF 完成之后写入的,则该标志被设置(否则其值为 -1,表示未指定)。*ICGU* 以比 *IOpCl* 更简单的方式编码计算是否为复数和/或 GHF。其三位数值解释为 *klm*:*k* 为 1 表示自旋对齐情形,为 2 表示 GHF;*l* 为 1 表示实数,为 2 表示复数;*m* 为 1 表示 RHF/GHF,为 2 表示 UHF(即 1 或 2 个自旋块)。当 *k*=2 时,*NBasis* 为空间基函数的数目,但算符矩阵是在自旋轨道基上定义的,因此其维度为 *k*NBasis*。当该文件被读回 Gaussian 时,*IOpCl* 可以为 -1,以表示应使用 *ICGU* 来指定这些参数。若 *IOpCl*≥*0* 且 *ICGU*≥*0*,则会检查二者是否一致。3`Integer IAn(NAtoms)` 原子序数,若使用 I*4 则补齐为偶数个整数。4`Integer IAtTyp(NAtoms)` 原子类型信息。对其他程序而言,主要关注的是负值表示在 ONIOM 模型体系计算中为非活性原子。默认情况下,文件写入时会从所有数组中省略非活性原子,并将 *NAtoms* 设为活性原子数,但也可以选择包含全部原子。若使用 I*4,则补齐为偶数个整数。5`Real*8 AtmChg(NAtoms)` 核电荷;若使用了 ECP,其值可能与原子序数不同。6`Real*8 C(3,NAtoms)` 核的笛卡尔坐标,单位为玻尔(Bohr)。

```
Integer IBfAtm(NBasis), IBfTyp(NBasis) 7
```

*IBfAtm* 为基函数到原子的映射。*IBfTyp* 为每个基函数的类型标志,其形式为 *lllmmm*,其中 *lll* 为角动量,*mmm* 为分量编号。负值表示纯函数,正值表示笛卡尔函数。因此,笛卡尔 *d* 函数编号为 2001 至 2006,纯 *d* 函数编号为 -2001 至 -2005。8`Real*8 AtmWgt(NAtoms)` 原子量。9`NFC, NFV, ITran, IDum` 分子轨道双电子积分的窗口信息。分子轨道包括 *NFC* 个冻结内层轨道和 *NFV* 个冻结虚轨道,因此分子轨道双电子积分将针对 *NBsUse-NFC-NFV* 个轨道。若未存储分子轨道积分,则 *ITran*=0;若仅存储了至少涉及一个占据轨道的分子轨道,则 *ITran*=4;若进行了完整变换,则 *ITran*=5。10 关于计算的其他标量数据(如适用)。*NLab* 记录 10 仅在 *NLab*>9 时出现。它包含 *NLab*-10 个整数,每个整数指定对应初始记录中的 32 位字数(以便在文件存储时不含记录标记/长度的情况下,程序能够跳过这些记录)。例如,若 *NLab* 为 13,则记录 10 将包含 3 个整数,分别指定第 11 至第 13 个初始记录的长度。目前,*NLab* 的最大值为 11,记录 10 包含单个整数 **16**。1116 个附加整数,其中目前只使用前五个:*NShellAO*:需要壳层数据时,AO 基函数收缩壳层的数目。*NPrimAO*:AO 原始壳层的数目。

*NShellDB*:需要拟合壳层数据时,密度拟合函数收缩壳层的数目。*NPrimDB*:密度拟合原始壳层的数目。*NBTot*:连接性数据中键的总数(如有)。

通常,程序应在文件开头读取(或跳过)*NLab* 个记录,以到达矩阵元数据。这样做可以确保在后续版本的矩阵元文件中添加的额外初始记录得到正确处理。这 *NLab* 个记录之后是零个或多个矩阵分段,每个分段都有一个初始记录:

```
Character*64Label,IntegerNI,NR,NTot,NPerRec,N1,N2,N3,N4,N5,ISym
```

其中各字段分别为:标签、每个元素的整数数目和实数数目、元素总数,以及每条记录中的元素数。对于稠密矩阵(存储时包含零元素),*NI* 可以为零。*NR* 为负值时表示数据为复数而非实数。*N1* 至 *N5* 为该对象作为矩阵的维度,未使用的维度为 0,下三角矩阵的维度为负值。例如,若 *NBasis*=50 且 *NBsUse*=49,则重叠矩阵的 *N1* ··· *N5* 为 **-50**
**50 0 0 0**,而到正交基的变换的 *N1* ··· *N5* 为 **50 49 0 0 0**。对于反对称/厄米矩阵,*ISym*=-1。文件末尾由标签为 **END**、所有整数值均为 0 的记录标记。该初始记录之后是 *(NTot+NPerRec-1)/NPerRec* 个记录,每个记录为以下形式之一:

```
IntegerID(NI,NPerRec),Real*8DX(NR,NPerRec)
```

或仅为:

```
Real*8DX(NR,NPerRec)
```

若 *NI*=0 或 *NR*<0,则格式为:

```
IntegerID(NI,NPerRec),Complex*16DX(-NR,NPerRec)
```

或

```
Complex*16DX(NR,NPerRec)
```

标签(如有)位于 *ID* 中,数值位于 *DX* 中。所有矩阵元都是在纯函数或笛卡尔基函数上定义的,具体取决于 Gaussian 路由段中指定的内容,或特定基组的默认设置。

#### E.3.1 带标签的分段

可能的标签和分段包括以下几种:

```
OVERLAP
COREHAMILTONIANALPHA
COREHAMILTONIANBETA
KINETICENERGY
```

每一项都是以稠密方式存储(包含全部 *N**(*N*+1)/2 个元素,不带标签)的下三角矩阵。除非施加了 Fermi 接触微扰,否则两个核哈密顿矩阵是相同的。

```
ORTHOGONALBASIS
```

若存在,则为一个 (*NBasis*,*NBsUse*) 矩阵,给出从 AO 到线性无关正交归一基组的变换。

```
DIPOLEINTEGRALS
```

若存在,则包含三个下三角矩阵,分别保存 X、Y 和 Z 方向的偶极矩阵元。

```
QUADRUPOLEINTEGRALS
OCTOPOLEINTEGRALS
HEXADECAPOLEINTEGRALS
```

若存在,这些项分别为 6、10 或 15 个笛卡尔多极积分矩阵。

```
DIPVELINTEGRALS
RXDELINTEGRALS
```

若存在,这些项为 Del 与 RxDel 单电子算符的 3 个矩阵。

```
GIAOD2H/DBDM
```

若存在,每个都是 9×*NAtoms* 的下三角矩阵,分别保存 GIAO 核哈密顿对外场和核磁矩的二阶导数(即抗磁屏蔽项所需的矩阵元)。

```
GIAOL/R3
```

若存在,每个都是 3×*NAtoms* 的下三角矩阵,保存 GIAO 磁微扰(即顺磁屏蔽项所需的矩阵)。

```
ALPHAORBITALENERGIES
```

若存在,这是一个长度为 *NBsUse* 的向量,包含初始猜测或收敛的轨道能量。

```
ALPHAMOCOEFFICIENTS
```

若存在,这是一个 *NBasis*×*NBsUse* 的矩阵,包含初始猜测或收敛的轨道。

```
BETAORBITALENERGIES
```

若存在,这是一个长度为 *NBsUse* 的向量,包含初始猜测或收敛的轨道能量。

```
BETAMOCOEFFICIENTS
```

若存在,这是一个 *NBasis*×*NBsUse* 的矩阵,包含初始猜测或收敛的轨道。

```
ALPHADENSITYMATRIX
```

若存在,这是一个下三角矩阵,包含由群体分析等选项所选定的密度矩阵的 α 自旋部分。若将其读回 Gaussian,则它将替代 SCF 密度存储。

```
BETADENSITYMATRIX
```

若存在,这是一个下三角矩阵,包含由群体分析等选项所选定的密度矩阵的 β 自旋部分。若将其读回 Gaussian,则它将替代 SCF 密度存储。

```
ALPHASCFDENSITYMATRIX
```

若存在,这是一个下三角矩阵,包含初始猜测或收敛的 SCF α 密度。

```
BETASCFDENSITYMATRIX
```

若存在,这是一个下三角矩阵,包含初始猜测或收敛的 SCF β 密度。

```
[ALPHA,BETA][MP2,MP3,MP4,CI,QCI/CC]DENSITYMATRIX
```

若存在,这些是包含所示类型电子相关的 α 与 β 密度。

```
[MULLIKEN,ESP,AIM,NPA,MBS]CHARGES
```

特定类型的原子电荷。根据 Population 关键字的选项,可能存在多个电荷分段。注意,所有类型的静电势拟合电荷都标记为“ESP CHARGES”。

```
GAUSSIANSCALARS
```

这是一个带标签实数的向量。标签在 1 至 1000 之间的元素对应 Gaussian /Gen/ 文件中的元素(表格见下文)。标签大于 1000 的元素保留给与外部程序交换的特定标量。

```
ALPHADENSITYDERIVATIVES
BETADENSITYDERIVATIVES
```

若存在,这些项保存在 CPHF 过程中对所施加的各种微扰的 AO 密度导数(下三角矩阵)。矩阵的数目等于微扰的数目,且数目各不相同。

```
ALPHAMODERIVATIVES
BETAMODERIVATIVES
```

若存在,这些是关于磁场的 MO 系数导数,分别为 (*NBasis*,*NAE*,3) 和 (*NBasis*,*NBE*,3)。

```
ALPHAFOCKMATRIX
```

若存在,这是 α 自旋的 Fock 矩阵,对于闭壳层和 GHF 则是唯一的 Fock 矩阵。

```
BETAFOCKMATRIX
```

若存在,这是非限制 SCF 计算中的 β 自旋 Fock 矩阵。

```
NUCLEARGRADIENT
```

若存在,则包含能量相对于核坐标的 3*NAtoms 个导数。这更可能是外部程序返回的字段,而不是作为外部程序输入使用的字段。

```
NUCLEARFORCECONSTANTS
```

若存在,这些是能量相对于核坐标的二阶导数。这更可能是外部程序返回的字段,而不是作为外部程序输入使用的字段。它们以维度为 3*NAtoms 的下三角矩阵形式存储。

```
ELECTRICDIPOLEMOMENT
ELECTRICDIPOLEDERIVATIVES
ELECTRICDIPOLEPOLARIZABILITY
DIPOLEPOLARIZABILITYDERIVATIVES
ELECTRICDIPOLEHYPERPOLARIZABILITY
ATOMICAXIALTENSORS
```

若存在,这些是关于静态外电场的导数。若将其返回 Gaussian,则仅更新文件中包含的性质,Gaussian 内部数据中已有的其他性质保持不变。

```
SHELLTYPE
NUMBEROFPRIMITIVESPERSHELL
CONTRACTIONCOEFFICIENTS
P(S=P)CONTRACTIONCOEFFICIENTS
COORDINATESOFEACHSHELL
```

这些项用于指定基组,其格式与 fchk 文件中相同字段的格式一致。以 `DENSITY` 为前缀的同名字段用于指定密度拟合基组(如有)。

```
OVERLAPDERIVATIVES
COREHAMILTONIANDERIVATIVES
F(X)
DENSITYDERIVATIVES
FOCKDERIVATIVES
ALPHAUX
BETAUX
```

这些记录包含导数 SCF(CPHF)计算的结果,采用文献 [795] 中的记号:Sx、Hx、F(x)、Px、Fx、Ux 和 Cx。对于开壳层,F(x) 和 Fx 先包含所有 α 的 Fock 导数,随后是所有 β 的 Fock 导数;而 Ux 和 Cx 的两种自旋情形则分别位于独立的记录中。

```
[Alpha,Beta][SCF,MP2,MP3,MP4,CIRho(1),CI,CC]DENSITY
```

这些记录保存 SCF 后的密度,对于开壳层,先为 α 再为 β。

```
REGULAR2EINTEGRALSor
RAFFENETTI2EINTEGRALS
```

仅存储非零积分,其四个指标满足 *i* ≥*j*、*i* ≥*k*、*k* ≥*l*、*j* ≥*l*(当 *i* = *k* 时)。*NR* 对于普通积分为 1,对于 Raffenetti 积分组合则为 1、2 或 3:

*R* 1(*i*, *j*,*k*,*l*) = (*ij*|*kl*)−1/4[(*ik*|*jl*)+(*il*|*jk*)] *R* 2(*i*, *j*,*k*,*l*) = (*ij*|*kl*)+(*il*|*jk*) *R* 3(*i*, *j*,*k*,*l*) = (*ik*|*jl*)−(*il*|*jk*)

默认情况下,闭壳层体系仅使用 *R1*,UHF 则使用 *R1* 和 *R2*。NoRaff 关键字强制使用普通积分,而 IOp(3/11=*N*) 可用于强制使用特定的 Raffenetti 积分组合。若请求了分子轨道双电子积分,则这些积分以稠密方式存储(包括零元素,且不带整数标签)。对于限制性计算,若进行完整变换(即上文中的 *ITran*=5),则会有一组标记为 `AA MO 2E INTEGRALS` 的积分,按唯一的四元组指标存储。也就是说,若 *NROrb = NBsUse - NFC - NFV* 为活性轨道数(参与变换的轨道),则在完整变换的情况下将有 *NO4*=(*NOrbTT**(*NOrbTT*+1))/2 个积分,其中 *NOrbTT*=(*NROrb**(*NROrb*+1))/2。对于非限制计算且进行完整变换,则会有 3 组积分,即 AA、BA 和 BB。AA 和 BB 的长度为 *NO4*,BA 的长度为 *NOrbTT*²,其中 β 自旋指标变化最快。

对于部分变换(*ITran*=4),限制性计算会有一组分子轨道积分,其维度为 (*NOrbTT,NROrb,NOA*),其中 *NOA*=*NAE*-*NFC* 为活性占据轨道数。对于限制性计算,还会有 AA、AB、BA 和 BB,其维度分别为 (*NOrbTT,NROrb,NOA*)、(*NOrbTT,NROrb,NOB*)、(*NOrbTT,NROrb,NOA*) 和 (*NOrbTT,NROrb,NOB*)。

```
TRANSMOCOEFFICIENTS
```

若包含了分子轨道双电子积分,则该记录保存变换中使用的分子轨道系数(即省略了冻结内层或虚轨道),先为 α 再为 β 自旋。

#### E.3.2 Gaussian 标量

1 维里比 2-4 所施加外电场的分量(如有) 5 2e SCF 能量 6 SCRF g 因子 7 SCRF a0 8 热能 9 E(CI/CC/QCI/BD) 10 E(CCD+ST4(CCD)/QCISD(T)/BD(T)/CI+Davidson) 11 E(VAR1) 12 零点能 13 多步(G1、G2 等)能量 14 虚频数目 15 D(PUHF) 16 EPUHF 17 ECBS2 18 ECBSI 19 EPMP2-0 20 EPMP3-0 21 优化参数的均方根力 22 E(CIS-MP2) 23 第一个污染物湮灭后密度矩阵中的 RMS 误差 S2 24 (空) 25 CIS 能量 26 UMP4D (=UMP4DQ - E4(R+Q)) 27 BD 的参考能量 28 MP5 29 S4SD(在 L502 的 ANNIL 中计算,由 PSCF 自旋投影例程使用) 30 总能量的冻结内层部分 31 来自 SCFDM 的“TAU” 32 SCF 能量 33 UMP2 能量 34 UMP3 能量

35 UMP4(SDTQ) 能量 36 CBS OIii 37 带 L116 反应场的总能量 38 MP4DQ 能量 39 MP4SDQ 能量 40 由 L116 使用 41 核排斥能 42 T(参考行列式修正的长度) 43 优化中更新的能量,Opt=Simult 的 SCF 波函数的 <S2> 44 一阶修正后的 <S2>(DOUBAR 之后) 45 考虑双激发修正后的 <S2>(未实现) 46 (空) 47 A0 48 用于在 Opt=Simult 中累积能量 49 热力学计算的温度 50 热力学计算的压强 51 热力学计算中频率的标度因子 52 来自非活性原子对的核排斥贡献 53 ROMP2 中 E2 的单激发贡献 54 用于外推的当前轨道下的 E(2) 55 反应场能量中的核项 56 反应场能量中的电子项 57 来自投影频率计算的曲率 58 沿 IRC 进行单点计算的反应坐标 59 外部程序状态标志;参见 RunExt。 60 第一次迭代时的 SCF 能量 61 作业状态:-1=进行中;0=未定义/旧检查点文件;1=成功完成;2=多步作业中的步骤成功完成;3=Link 9999 中的错误终止 62 可用的核坐标导数的最高阶数。 63 最近一次 SCF 的迭代次数。 64 不含外场贡献的核排斥能。
