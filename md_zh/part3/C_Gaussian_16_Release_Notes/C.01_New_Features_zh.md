### C.1 新功能

#### C.1.1 新的建模能力

- [**REV B**] 现可在 CIS 和 TD 理论水平上计算激发态的静态拉曼强度。TD Freq=Raman 通过对电场进行数值微分来计算极化率,因此对这些方法而言,Freq=Raman 的计算成本是不计算拉曼强度时频率计算的 7 倍。
- TD-DFT 解析二阶导数,用于预测振动频率/红外与拉曼光谱,并对激发态进行过渡态优化与 IRC 计算。
- EOMCC 解析梯度,用于进行几何优化。
- 用于 VCD 与 ROA 光谱的非简谐振动分析:参见 Freq=Anharmonic。
- 振动光谱与强度:参见 Freq=FCHT 及相关选项。
- 共振拉曼光谱:参见 Freq=ReadFCHT。
- 新的 DFT 泛函:M08HX、MN15、MN15L。
- 新的双杂化方法:DSDPBEP86、PBE0DH 与 PBEQIDH。
- PM7 半经验方法。
- Ciofini 激发态电荷转移诊断:参见 Pop=DCT。
- Caricato 的 EOMCC 溶剂化相互作用模型:参见 SCRF=PTED。
- 广义内坐标(Generalized internal coordinates),一种可定义并使用任意冗余内坐标的功能,用于优化约束及其他用途。参见 Geom=GIC 与 GIC Info。

#### C.1.2 性能增强

- NVIDIA K40、K80 与 P100(Pascal)GPU 在 Linux 下支持 Hartree-Fock 与 DFT 计算;P100 支持为 [**REV B**] 新增,同时为所有 GPU 类型提供性能改进。GPU 支持与使用的详细信息参见"使用 GPU"。

![](../../../md/images/part3/p027_5.jpeg)

- 在更多处理器上的并行性能得到改善。获取多 CPU 与集群上最佳性能的方法参见"并行性能"标签页。
- [**REV B**] Linda 工作进程之间的动态任务分配现已成为默认设置,从而提高并行效率。
- Gaussian 16 采用优化的内存算法,在 CCSD 迭代过程中避免 I/O。
- 对 GEDIIS 优化算法进行了多项改进。
- 活性空间的 CASSCF 改进
- (10,10) 提升性能,并使多达 16 个轨道的活性空间变得可行(取决于分子体系)。
- 显著加速 W1 复合模型的核心关联能计算。
- Gaussian 16 包含算法改进,显著加速复合电子传播子(CEP)方法中对角、二阶自能近似(D2)部分的计算,如 [385] 所述。参见 EPT。

#### C.1.3 使用改进

- [**REV B**] ChkChk 工具现在会报告作业状态(作业是否正常完成、失败、正在进行中等)。
- [**REV B**] 原子的输入行中可选参数现在可以指定使用有限(非点)核时所用的半径。半径以原子单位制的浮点数指定,使用 RadNuclear=*val* 项。例如:

```
C(RadNucl=0.001)0.00.03.0
```

- 用于将 Gaussian 与其他程序对接的工具,既适用于 Fortran 与 C 等编译型语言,也适用于 Python 与 Perl 等解释型语言。详情参见《与 Gaussian 16 对接》。[**REV B**] 在矩阵元文件中增加了许多其他量,包括原子布居、单电子与性质算符矩阵以及非绝热耦合矢量。新增的带标签部分包括 QUADRUPOLE INTEGRALS、OCTOPOLE INTEGRALS、HEX-ADECAPOLE INTEGRALS、[MULLIKEN,ESP,AIM,NPA,MBS] CHARGES、DIP VEL INTEGRALS、R X DEL INTEGRALS、OVERLAP DERIVATIVES、CORE HAMILTONIAN DERIVATIVES、F(X)、DENSITY DERIVATIVES、FOCK DERIVATIVES、ALPHA UX、BETA UX、ALPHA MO DERIVATIVES、BETA MO DERIVATIVES、[Alpha,Beta] [SCF,MP2,MP3,MP4,CI Rho(1),CI,CC] DENSITY 以及 TRANS MO COEFFICIENTS,以及标量 63–64。
- 在 Link 0(%)输入行和/或 *Default.Route* 文件中指定的参数,现在也可以通过命令行参数或环境变量指定。[**REV B**] 引入了命令行选项,用于使用检查点文件或矩阵元文件指定输入和/或数据(相当于用于输入的 %OldChk 或 %OldMatrix Link 0 命令)。详情参见"等价项"标签页。
- 现在可以在每 n 步几何优化时计算力常数:参见 Opt=Recalc。
- [**REV B**] DFTB 参数现在在构建基组之前于 Link 301 中读取,因此某元素是否包含 d 函数可由参数文件决定。
- [**REV B**] 现在有命令行选项,可用于指定与检查点文件或矩阵元文件之间的输入和/或数据交换。详情参见"等价项"标签页或"命令行选项"页面。
