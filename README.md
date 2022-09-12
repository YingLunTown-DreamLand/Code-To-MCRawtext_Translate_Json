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
apt update && apt upgrade && apt install python && apt install git && pip install brotli && cd /sdcard && git clone https://github.com/Happy2018new/Code-To-MCRawtext_Translate_Json/ && cd Code-To-MCRawtext_Translate_Json
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
## 语言
这个程序只支持中文。

## 联系我
您可以通过 `QQ` 联系我，我的 `QQ` 是 `3527679800` 。

## 更新日志
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