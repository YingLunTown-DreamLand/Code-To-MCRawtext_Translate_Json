# Code-To-MCRawtext_Translate_Json
这是一个翻译软件，用于将 `伪代码` 写成的 `JSON` 文件转换为 `Minecraft Bedrock Edition` 中的 `Tellraw`
或 `Titleraw` 命令。

## 如何使用？
1. 下载 `run.exe` 并把它和 `input.json` 放在一起。
   - [下载链接](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/raw/main/run.exe)
2. 然后运行这个程序。
***
注意事项<br>
您应该参考 [input.json](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/blob/main/Example/Example%20-%201/input.json.py) 中的格式来编写 `伪代码` 形式的 `JSON` 文件。

## 从源代码运行程序(对于 `Termux` )
您应该授予 `Termux` 存储权限，否则您将不能通过源代码来运行本程序。
***
下载和首次使用
1. 在 `Termux` 执行此命令：
```
apt update && apt upgrade && apt install python && apt install git && cd /sdcard && git clone https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/ && cd Code-To-MCRawtext_Translate_Json
```
2. 将 `input.json` 放置在路径 `/storage/emulated/0/Code-To-MCRawtext_Translate_Json/` ，然后在 `Termux` 执行命令 `python run.py` 。
***
后续的使用
1. 在 `Termux` 执行命令 `cd /sdcard/Code-To-MCRawtext_Translate_Json` 。
2. 将 `input.json` 放置在路径 `/storage/emulated/0/Code-To-MCRawtext_Translate_Json/` 。
3. 在 `Termux` 执行命令 `python run.py` 。
***
移除
```
cd /sdcard && rm -r Code-To-MCRawtext_Translate_Json
```
***
更新
```
cd /sdcard && rm -r Code-To-MCRawtext_Translate_Json && git clone https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/
```

## 作为 `Api` 使用
如果您是开发者，那么您可能需要将此工具作为一个 `Api` 使用，而非调用程序本体。<br>
实际上，虽然本转换器虽然包含多个函数，但您可以由一个函数调用而实现。<br>
因此，作为 `Api` 来使用本工具并不是一件难事。<br>
***
首先，请将本工具相关的代码置于您代码的目录下。<br>
此处预设变量 `WaitingForTranslate` 已经存放了 `伪代码` 数据(`dict` 类型)。<br>
那么，执行下述代码片段，转换结果会存放于变量 `TranslateResult` 中。
```python
import function
TranslateResult = function.structuralBody(WaitingForTranslate['结构体'])
```
然后，您就可以利用本工具自由地转换 `伪代码` 片段了。

## 语言
这个程序只支持中文。

## 联系我
您可以通过 `QQ` 联系我，我的 `QQ` 是 `3527679800` 。

## 更新日志
   - `2022/09/25 Night - Alpha(10.5)`<br>
      - 删减了不必要的代码并在 `README.md` 中增添了 `Api` 使用说明 & 于 [13cdafe](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/13cdafea18a29d4564a664b36877f869242809ef) 更新
   - `2022/09/24 Afternoon - Alpha(10.0)`<br>
   下述特性或问题于 [bd7e29c](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/bd7e29ca62240828c1c1964b4db8c0294a4b971f) 更新和修复
      - 修复了使用多个计分板时会由于条件不继承而造成的重大问题
      - 支持了任意形式的 `目标选择器` 及 `选择器参数` 。<br>
      因此原本的“分数条件”部分被修改为诸如下述样例的格式。
         ```json
         "显示条件":
         {
            "分数条件":
            {
               "sapling":[[1,2],[7,9]],
               "air":[[-9,3]]
            },
            "目标选择器":"@r",
            "其他目标选择器参数":["x=5","dx=3"]
         }
         ```
   - `2022/09/16 Morning - Alpha(5.0)`
      - 优化了输出的 `目标选择器` 并且修复了一些问题；现在对 `分数条件` 中加入了 `最大值` 和 `最小值` ，相关示例具体见下 & 于 [e886fc1](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/e886fc11ee29e86337ca8838fbd9e68a530f0be9) 更新和修复
         > 例子Ⅰ `"分数条件":{"Demo1":[ ["min","max"] ]}`<br>
         > 例子Ⅱ `"分数条件":{"Demo2":[ ["Min","Max"] ]}`<br>
         > 例子Ⅲ `"分数条件":{"Demo3":[ [233,"max"] ]}`<br>
         > 例子Ⅳ `"分数条件":{"Demo4":[ [233,"Max"] ]}`<br>
         > 例子Ⅴ `"分数条件":{"Demo5":[ ["min",2018] ]}`<br>
         > 例子Ⅵ `"分数条件":{"Demo6":[ ["Min",2018] ]}`
   - `2022/09/14 Noon - Alpha(4.3)`
      - 修复了 `结构体` 中的元素个数为 `8` 时，第 `8` 个元素中指定的嵌套不被解析的问题 & 于 [e264ef0](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/e264ef0271cd69691ecbf962324ecfe765447d39) 修复
   - `2022/09/14 Morning - Alpha(4.0)`<br>
   下述特性于 [d04ac9f](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/d04ac9f095ae3168bea082865d378b31a24898a3) 更新
      - 弃用 `计分板名称`
      - `分数条件` 的书写格式变更，更新为如下格式，现在允许使用更多的计分板。每个计分板中列表的条件以 `or(或)` 连接，计分板与计分板之间的条件以 `and(且)` 连接。
      ```
      "分数条件":
      {
         "计分板":[ [区间起始点, 区间终止点], [区间起始点, 区间终止点], ……, [区间起始点, 区间终止点] ],
         "计分板":[ [区间起始点, 区间终止点], [区间起始点, 区间终止点], ……, [区间起始点, 区间终止点] ],
         ……,
         "计分板":[ [区间起始点, 区间终止点], [区间起始点, 区间终止点], ……, [区间起始点, 区间终止点] ]
      }
      ```
   - `2022/09/12 Morning - Alpha(2.5)`
      - `分数条件` 的书写格式变更，更新为如下格式，即对一个单个的显示内容支持了更多的分数条件 & 于 [0786109](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/07861093026272c99d15f92f70e458d72bd692dc) 更新
      ```
      "分数条件":
      [
         [区间起始点, 区间终止点],
         [区间起始点, 区间终止点],
         ……,
         [区间起始点, 区间终止点]
      ]
      ```
   - `2022/09/11 Afternoon - Alpha(2.0)`
      - 进行了优化并增添了 `2` 个示例 & 于 [b3d2777](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/b3d2777d0cfbdac5efcfcc619e74c02e56d3830a) 更新
         - 所有示例见 [Code-To-MCRawtext_Translate_Json/Example](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/tree/main/Example)
   - `2022/09/11 Morning - Alpha`
      - 现在输出的 `JSON` 更短了；同时修复了一些潜在性问题 & 于 [5ecd234](https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/commit/5ecd2348703d42efab5de08afb1c76612ebce9be) 更新和修复

## 免责声明(This is not translated into English)
- 若因为使用本软件而造成了任何可能的问题，我不会对此负责。 
- 作者保留有关此工具的所有解释权。
- 特别应当注意的是，您不得将本工具用于盈利用途，除非得到作者的授权。
