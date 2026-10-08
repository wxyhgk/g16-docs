### B.2 已弃用(Deprecated)

**NoFMM**

此关键字会阻止使用 FMM 功能,即使它本可以提高性能。在 Gaussian 03 中,于集群或通过 Linda 在局域网上并行运行时,有时需要使用此关键字。相关问题已修复,现已不再需要。

**CCD+STCCD**

指定使用双激发的耦合簇计算,并利用 CCD 波函数评估单激发与三激发贡献至四阶。它已被 CCSD(T) 取代。

**CBS-Q, CBS-Lq**

请求使用 CBS-Q [180] 与 CBS-q [178] 方法(即 Lq 指 "little q")。它们已被 CBS-QB3 取代。

**CBS-QB3O**

使用 CBS-QB3 的原始参数化 [110]。该方法已过时,仅为向后兼容而保留。

**CBS-4O**

请求使用 CBS-4 的原始参数化 [180]。该方法已过时,仅为向后兼容而保留。

**Geom=Coord**

表示几何结构以笛卡尔坐标指定。分子构型中可直接包含笛卡尔坐标,无需任何特殊选项。

**Geom=OldRedundant**

使用 Gaussian 94 的冗余内坐标生成器。

**Geom=ModLargeRedundant**

使用 Opt=Big 的最小设置。不可用于周期性边界计算。

**Int=Raff**

仅适用于 SCF=Conventional。Raff 请求双电子积分采用 Raffenetti 格式 [787]。NoRaff 要求使用常规积分格式,同时在直接 CPHF 过程中抑制 Raffenetti 积分的使用。此选项影响常规 SCF 以及常规和直接频率计算。

**Int=BWeights**

使用 Becke 的加权方案进行数值积分。

**ReUse**

使用已有的积分文件。积分文件与检查点文件必须均来自先前的计算并已保留。仅允许用于单点计算与 Polar=Restart。

**WriteD2E**

强制在 HF 频率计算中写出积分导数文件。仅在调试新的导数代码时有用。

**LST, LSTCyc**

请求使用线性同步转变(Linear Synchronous Transit)[788] 生成过渡结构的初始猜测。LST 方法沿连接两个结构的路径寻找最大值,从而为连接它们的过渡结构提供猜测。*注意,LST 计算实际上并不能找到真正的过渡态。* LST 方法已被 Opt=QST2 取代。

**Massage**

Massage 关键字要求在生成分子构型与基组数据后对其进行修改。该关键字已被 ExtraBasis、Charge、Counterpoise 等关键字取代而弃用。

**Opt=EnOnly**

请求使用伪牛顿-拉夫逊(pseudo-Newton-Raphson)方法进行优化,采用固定 Hessian,并通过能量的数值微分得到梯度。此选项要求通过 ReadFC 或 RCFC 读入 Hessian。它可用于定位过渡结构与更高阶的鞍点。要求分子以 Z 矩阵形式指定。对于仅能量方法,默认值为 Opt=(EnOnly,EF)。

**Opt=FP**

请求使用 Fletcher-Powell 优化算法 [789],该算法不需要解析梯度。Fletcher-Powell 优化允许的最大变量数为 30。要求分子以 Z 矩阵形式指定。

**Opt=Grad**

请求梯度优化,除非指定了其他选项,否则使用默认方法。当解析梯度可用时,这是默认设置;否则该选项无效。

**Opt=MNDOFC**

请求计算 MNDO(若可用则为 AM1)力常数,并用于启动(通常为从头算的)优化。我们建议先执行 PM6Freq 计算,再使用 Opt=RCFC,而不要使用此选项。

**Opt=MS**

指定 Murtaugh-Sargent 优化算法 [790]。Murtaugh-Sargent 优化方法是一种已过时的替代方案,在 Gaussian 中仅为向后兼容而保留。Murtaugh-Sargent 优化允许的最大变量数为 50。要求分子以 Z 矩阵形式指定。

**Opt=UnitFC**

请求使用单位矩阵代替通常的价力场猜测作为 Hessian 的初值。

**Opt=GDIIS**

指定使用改进的 GDIIS 算法 [791–793]。默认的 GEDIIS 算法总是更好。

**Opt=Big**

请求使用快速方程求解方法 [794] 进行坐标变换以及牛顿-拉夫逊或 RFO 步长计算,以优化过程。该方法避免了矩阵对角化。因此,本方法不能与本征矢跟踪方法(Opt=TS)联合使用。此选项不可靠,不推荐使用。

**Output=PolyAtom**

请求输出 PolyAtom 积分程序最初所用格式的一种变体的积分文件。默认生成的格式为 Caltech MQM 程序所用格式,但 Link 9999 中的代码可轻松修改以生成同一主题的其他变体。

**Output=Trans**

以 Caltech(Tran2P5)格式写出 MO 系数文件。仅对 Caltech 程序的用户有用。

**SCF=Sleazy**

请求适用于单点计算的宽松 SCF 收敛判据;等价于 SCF=(Conver=4,VarInt,NoFinal,Direct)。SinglePoint 为 Sleazy 的同义词。不推荐用于生产级计算。

**SCF=VerySleazy**

进一步降低截断值;迭代过程中使用 Int=CoarseGrid 与单点积分精度,随后以常规单点格点(MediumGrid)进行一次迭代。不推荐用于生产级计算。

**SCRF=DPCM**

使用可极化介电模型 [685, 686, 688],除一些细微的实现细节 [700] 外,其与 Gaussian 98 的 SCRF=PCM 选项相对应。该模型不再推荐用于一般用途。默认的 SCRF 方法为 IEFPCM。

**SCRF=Numer**

强制使用数值 SCRF 而非解析形式。对于超过偶极的多极阶数,必须使用此关键字。此选项隐含使用球形空腔,而球形空腔不被推荐。该选项不提供梯度。

**SCRF=Dipole**

选项 Dipole、Quadrupole、Octopole 与 Hexadecapole 用于指定 SCRF 计算中使用的多极阶数。除 Dipole 外,其余选项均需同时指定 Numer 选项。

**SCRF=Cards**

在紧随指定介电常数与半径的行(三个自由格式实数)之后,从输入流读取先前计算好的反应场,并以此开始 SCRF=Numer 计算。

**%SCR**

用于指定 **.SCR** 临时文件的位置。

**Stable=Symm**

保留对称性限制。NoSymm 会放宽对称性限制,为默认设置。

**Transformation=Old2PDM**

强制在后 SCF 梯度计算中采用传统的二粒子密度矩阵(2PDM)处理方式(先在 L1111 中排序,再在 L702 和 L703 中处理)。该方法较慢,但可降低内存需求。此选项不能用于冻结核计算。

**Transformation=New2PDM**

使二粒子密度矩阵在后 SCF 梯度计算中由 L1111 生成、使用并随即丢弃。

**Transformation=Conventional**

请求使用基于外部存储积分的原始变换方法。
