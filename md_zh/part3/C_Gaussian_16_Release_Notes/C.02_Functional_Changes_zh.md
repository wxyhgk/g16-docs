### C.2 功能变更

#### C.2.1 相对 Gaussian 16 Rev. A.03 的变更

- 从源代码编译的步骤有少量修改,相关说明记载于 `http://gaussian.com/g16/g16src_install.pdf`。

#### C.2.2 相对 Gaussian 09 的变更

计算默认值

Gaussian 16 中以下计算默认值与 Gaussian 09 不同:

- 积分精度为 10^-12,而 Gaussian 09 中为 10^-10。
- 一般用途的 DFT 格点默认为 UltraFine,而 G09 中为 FineGrid;CPHF 的默认格点为 SG1,而非 CoarseGrid。参见关于 Integral 关键字的讨论。
- SCRF 默认使用对称形式的 IEFPCM [702](Gaussian 09 中不存在),而非非对称版本。
- 物理常数采用 2010 年的数值,而 Gaussian 09 中采用 2006 年的数值。前两项的更改是为了确保若干新计算类型(例如 TD-DFT 频率、非简谐 ROA)的准确性。基于这些原因,Integral=(UltraFine,Acc2E=12) 被设为默认。与 Gaussian 09 的默认值 Integral=(FineGrid,Acc2E=10) 相比,使用这些设置通常能提高涉及数值积分的计算(例如溶液中的 DFT 优化)的可靠性,而 CPU 需求略有增加。G09Defaults 关键字会将这四项默认值全部恢复为 Gaussian 09 的值。它是为了与先前的计算兼容而提供的,但强烈建议在新研究中使用新的默认值。

默认内存用量

Gaussian 16 将内存用量默认设为 %Mem=100MW(800MB)。对于更大的分子以及使用大量处理器的计算,更大的数值是合适的;详情参见"并行作业"标签页。

TD-DFT 频率

TDDFT 频率计算默认解析地计算二阶导数,因为这比数值导数快得多(而在 Gaussian 09 中只能使用数值导数)。
