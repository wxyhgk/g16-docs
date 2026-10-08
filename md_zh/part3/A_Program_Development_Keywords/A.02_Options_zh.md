### A.2 Options(选项)

CPHF 以下选项用于调试:KeepMicro 保留 CPHF 中的所有 EE 中心,即使对于使用非二次微迭代的 Opt=CalcFC 或 Opt=CalcAll,其中不用于内坐标的原子也无需包含在 CPHF 中。NoReuse 在频率计算的第二次(核)CPHF 中不复用电场 CPHF 解。默认为 ReUse。XYTreat 将实部和虚部微扰一起处理。其相反选项为 NoXY,它们将分开处理。若同时进行核微扰,则默认分开处理;若仅有电磁微扰,则默认一起处理。ZVector 对 SCF 后梯度使用 Z 矢量方法 [225–227]。若未同时请求 Hartree-Fock 二阶导数,则允许使用且为默认值。NoZVector 关键字表示对 SCF 后梯度使用完整的 3 × N *Atoms* CPHF。

FMM 以下选项可用于调试:

LMax=*N* 指定最高阶多极展开。默认值为 25。Levels=*N* 指定 FMM 所用的层数。分子默认为 8,对于 PBC 则动态调整。Tolerance=*N* 指定精度水平为 10−*N*。*N* 的默认值为 11,但在 SCF 第 0 遍中为 7。JBoxLen=*N* 在进行 J 计算时,将最小盒子长度(尺寸)设为 *N*/1000 玻尔。默认 *N* 为 2.5。若同时进行 J 和 K 计算,则取 JBoxLen 与 KBoxLen 中的较大值。BoxLen 是 JBoxLen 的同义词。KBoxLen=*N* 在进行 K 计算时,将最小盒子长度(尺寸)设为 *N*/1000 玻尔。默认 *N* 为 0.75。若同时进行 K 和 J 计算,则取 KBoxLen 与 JBoxLen 中的较大值。AllNearField 开启 FMM 中的全部近场计算。NoParallelCPHF 禁止在 CPHF 阶段的 FMM 中并行执行。NoParCPHF 是该选项的同义词。

Integral 以下选项用于调试:

CNDO 使用 CNDO/2 积分在主程序中进行计算。INDO 使用 INDO/2 积分在主程序中进行计算。ZIndo1 使用 ZIndo/1 积分在主程序中进行计算。ZIndoS 使用 ZIndo/S 积分在主程序中进行计算。DPRISM 对 spdf 积分导数使用 PRISM 算法 [782]。这是默认值。Rys1E 使用 Rys 方法 [783–785] 计算单电子积分,而非默认方法。这在内存非常有限的机器上是必要的。Rys2E 若写入双电子积分,则使用 Rys 方法(L314)[783–786]。这比默认方法慢,但在小内存机器上可能需要,并且在请求常规(非 Raffenetti)积分(通过 NoRaff 选项)时默认选用。DSRys 使用标量 Rys 积分导数代码。可与 Berny 结合,仅对 df 使用 Rys。Berny 使用 Berny sp 积分导数及二阶导数代码(L702)。Pass 指定积分通过磁盘存储在内存中,NoPass 则禁用此功能。与 SCF=[No]Pass 同义,后者为推荐用法。NoJEngine 禁止使用特殊库仑代码。NoSP 在将积分写入磁盘时,不使用特殊 sp 积分程序(L311)。RevDagSam 反转 Prism 中对角采样的选择。NoSchwartz 不使用 Schwartz 积分估计(仅使用启发式集合)。Schwartz 表示除启发式集合外,还使用 Schwartz 积分估计。默认两者都使用。RevRepFock 反转 Scat20 与复制 Fock 矩阵的选择。NoDFTCut 关闭额外的 DFT 截断。SplitSP 将 AO S=P 壳层拆分为独立的 S 和 P 壳层。NoSplitSP 为默认值。SplitSPDF 将 AO S=P=D 和 S=P=D=F 壳层拆分为 S=P、D 和 F。NoSplitSPDF 为默认值。

SplitDBFSPDF 将密度 S=P=D 与 S=P=D=F 拆分为 S=P、D 和 F。NoSplitDBFSPDF 为默认值。NoGather 禁止使用 gather/scatter 数字化处理,即使在处理少量密度矩阵时也是如此。Splatter 是该选项的同义词。ForceNuc 将核-电子库仑与电子-电子库仑一起计算。SepJK 在 HF/杂化 DFT 中将 J 与 K 分开计算,用于测试。Seq2E 设置为并行计算双电子积分,但随后不并行运行(用于调试)。SeqXC 设置为并行计算双电子积分,但随后不并行运行(用于调试)。SeqLinda 使 Linda 工作进程按顺序运行。目前仅使除主进程外的 Linda 工作进程同时运行,但先于主进程。BigAtoms 在 XC 求积中将所有原子尺寸设为较大值。BigShells 在 XC 求积中将所有壳层尺寸设为较大值。NoSymAtGrid 不利用(阿贝尔)对称性减少对称唯一原子上的格点数。LinMIO 在 FoFCou 中转换为线性存储,用于测试。RevDistanceMatrix 反转是否在数值求积期间预先计算距离矩阵的选择。默认对分子预先计算,对 PBC 不预先计算。NoDynParallel 关闭动态工作分配。

Sparse 以下选项用于调试:

Loose 将截断设为 5 × 10−5。Medium 将截断设为 5 × 10−7。这是半经验方法的默认值。将截断设为 1 × 10−10。这是 DFT 方法的默认值。Tight 将截断设为 1 × 10−*N*。*N*

#### A.2.1 Changing Link Invocation and Ordering(更改链接调用与顺序)

ExtraLinks 请求执行额外的链接。它们在常规链接之后被添加到其覆盖层的所有实例中。例如,ExtraLinks=L9997 将使覆盖层 99 的每个实例按此顺序包含链接 9999(默认)和 9997。ExtraOverlays 此命令请求以非标准路由格式读入额外的覆盖层卡片,并将其紧接在最终(覆盖层 99)卡片之前插入标准路由段中。Skip 跳过路由中的初始覆盖层卡片。Skip=OvNNN 跳过直至首次出现覆盖层 NNN。Skip=M 跳过前 M 张卡片。Use=L *nnn* 指定通过程序的替代路由。可用以下选项:

L123 对 IRC 使用 L123 代替 L115。这是 IRC 的默认值,IRCMax 作业除外。L402 对半经验方法使用旧的链接 402 代码。L503 对 SCF 使用链接 503。L506 对 ROHF 使用链接 506。
