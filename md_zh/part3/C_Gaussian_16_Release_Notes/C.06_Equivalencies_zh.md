### C.6 等价项

控制 Gaussian 16 运行方式的大多数选项可以通过以下 4 种方式之一指定。按优先级从高到低依次为:1. **作为 Link 0 输入(% 行)**:这是控制特定作业的常用方法,也是控制多步输入文件中特定步骤的唯一方式。示例:%CPU=1,2,3,4

2. **作为命令行选项**:*命令行选项*适用于为不同的常用运行方式定义别名或其他快捷方式。示例:g16 -c="1,2,3,4" ··· 3. **作为环境变量**:这在标准脚本中最为有用,例如用于生成作业并提交至批处理队列系统。示例:`export GAUSS_CDEF="1,2,3,4"` 4. **作为 Default.Route 文件中的指令**:当希望更改所有作业的程序默认值时最为有用。示例:-C- 1,2,3,4 在查找 *Default.Route* 文件时,会先检查当前默认目录,然后依次检查 Gaussian 16 可执行文件路径中的目录:环境变量 GAUSS_EXEDIR,其通常指向 $g16root/g16。下表列出了 Link 0 命令、命令行选项、*Default.Route* 项与环境变量之间的等价关系。-h、-o 选项以及 -i 和 -o 选项类别是在 [**REV**

**B**] 中引入的,其对应的环境变量也一并引入。

**Default.Route   Link 0   选项   环境变量   说明**

*Gaussian 16 执行默认值* -R--r   GAUSS_RDEF   路由段关键字列表。-M-%Mem-m   GAUSS_MDEF   Gaussian 作业的内存量。-C-%CPU-c   GAUSS_CDEF   多处理器并行作业的处理器/核心列表。-G-%GPUCPU-g   GAUSS_GDEF   GPU 并行作业的 GPU=核心列表。-S-%UseSSH, %UseRSH-s   GAUSS_SDEF   用于启动网络并行作业工作进程的程序:rsh 或 ssh。-W-%LindaWorkers-w   GAUSS_WDEF   网络并行作业的主机名列表。-P-%NProcShared-p   GAUSS_PDEF   多处理器并行作业的处理器/核心数。已弃用;请使用 -C-。-L-%NProcLinda-l   GAUSS_LDEF   网络并行作业的节点数。已弃用;请使用 -W-。*归档条目数据* -H--h   GAUSS_HDEF   计算机主机名。-O--o   GAUSS_ODEF   单位(站点)名称。*实用程序默认值* -F-   GAUSS_FDEF   formchk 实用程序的选项。-U-   GAUSS_UDEF   实用程序的内存量。*脚本与外部程序的参数* # *section*-x   GAUSS_XDEF   作业的完整路由(路由不从输入文件读取)。%Chk-y   GAUSS_YDEF   作业的检查点文件。%RWF-z   GAUSS_ZDEF   作业的读写文件。%OldChk-ic   GAUSS_ICDEF   用于读取输入的已有检查点文件。

%OldMatrix-im   GAUSS_IMDEF   用于读取输入的矩阵元文件。%OldMatrix=(*file*,i4lab)-im4   GAUSS_IM4DEF   用于读取输入的、使用 4 字节整数的矩阵元文件。%OldRaw-ir   GAUSS_IRDEF   用于读取输入的原始矩阵元文件。%OldRaw=(*file*,i4lab)-im4   GAUSS_IR4DEF   用于读取输入的、使用 4 字节整数的原始矩阵元文件。-oc   GAUSS_OCDEF   输出检查点文件。通常与 -y/GAUSS_YDEF 重复。-om   GAUSS_OMDEF   输出矩阵元文件。-om4   GAUSS_OM4DEF   使用 4 字节整数的输出矩阵元文件。-or   GAUSS_IRDEF   输出原始矩阵元文件。-or4   GAUSS_IR4DEF   使用 4 字节整数的输出原始矩阵元文件。

注意,在命令行与环境变量中,指定值通常需要加上引号,以防止 shell 修改参数字符串。
