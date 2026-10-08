### A.1 Keywords(关键字)

此处描述的关键字和选项可用于开发新方法及其他调试目的,但不推荐用于生产级计算。

#### A.1.1 General Job Restart(作业通用重启)

此处我们讨论 Restart 的通用用法,该用法用于调试。生产环境中的用法请参见 Restart 一节。此关键字通过复用读写文件来重启计算。形式 Restart L1 复用读写文件,但生成新的路由段。若要沿用原路由段重启,可使用以下语法指定某个链接的出现位置,以及是否清理或保留覆盖层和链接易失性文件:

**#P Restart** [**L** *n*[(*m*)]] [**Clean**|**KeepOverlay**|**KeepAll**]

若指定了所有参数,则作业将在链接 *n* 的第 *m* 次出现处重启。Clean 要求由 Link1 删除所有例程和覆盖层易失性文件;KeepOverlay 要求保留覆盖层易失性文件,但不保留链接易失性文件;KeepAll 则保留全部文件。若读写文件是为链接内重启而设置的,则默认为 KeepAll,否则默认为 Clean。

#### A.1.2 IOp Setting Keywords(IOp 设置关键字)

IOp1=*keyword* 此关键字控制操作系统接口的各种细节。其选项为标准选项,但并非所有选项都已实现(或在每个版本中都相关)。

FileIODump 在每个链接结束时转储 FileIO 表。FDump 是该关键字的同义词。

![](../../../md/images/part3/p003_1.jpeg)

TimeStamp 开启时间戳。TStamp 是该关键字的同义词。FileIOPrint 开启 FileIO 中额外的调试输出。Synch 目前为空操作(仅出现在少数测试作业中)。NoDFTJ 关闭非杂化 DFT 中纯库仑项的使用(在生产作业中很少有用)。AbelianOnly 强制仅使用阿贝尔对称性(在生产作业中很少有用)。NoPackSort 在排序期间关闭将地址压缩为 32 位的做法,即使待排序地址空间小于 2^31 也是如此(在生产作业中很少有用)。

IOp2 此选项设置可动态分配的最大内存量。MDV 和 Core 是 IOp2 的同义词。IOp33 此项设置指定的标准调试输出选项。例如,以下设置在覆盖层 2 的所有调用中将 IOp(33) 设为 3,在覆盖层 7 的所有调用中将 IOp(33) 设为 1:

```
IOp33(2=3,7=1)
```

《Gaussian 16 IOps Reference》也记录了所有内部 IOp 选项。
