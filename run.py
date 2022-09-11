import json
import os
import sys
import traceback
import function
# 载入依赖项

try:
    with open("input.json","r+",encoding='UTF-8') as file:
        jsonContext = json.loads("".join(file.readlines()))
except:
    print('请将正确的 JSON 文件置于当前目录下，并命名为 input.json ！')
    os.system("pause")
    sys.exit()
# 载入 json

try:
    jsonContext = function.setGroup(jsonContext)
except ZeroDivisionError:
    sys.exit()
except:
    print('错误：在转换时发生了未知错误。如果不出意外，可能是您提供了不正确的 JSON 文件\n相关错误日志如下：\n')
    print(traceback.format_exc())
    os.system("pause")
    sys.exit()
# 取得结果

with open("ans.json","w+",encoding='UTF-8') as file:
    file.write(
        json.dumps(
            jsonContext,
            sort_keys=True,indent=4
            ,separators=(', ', ': '),
            ensure_ascii=False
            )
        )
# 输出展开版本的 json

with open("指令.txt","w+",encoding='UTF-8') as file:
    jsonContext = json.dumps(jsonContext,ensure_ascii=False,separators=(',', ':'))
    file.write(
        '/Execute <Target> ~ ~ ~ Tellraw @s ' + jsonContext + 
        '\n' + '/Execute <Target> ~ ~ ~ Titleraw @s <Title|Subtitle|Actionbar> ' + 
        jsonContext + '\n\n' + 'Execute <Target> ~ ~ ~ Tellraw @s ' + jsonContext + 
        '\n' + 'Execute <Target> ~ ~ ~ Titleraw @s <Title|Subtitle|Actionbar> ' + 
        jsonContext
        )
# 输出指令

print('完成：已将 input.json 转换为指令')
print('已展开的 JSON 形式保存在当前目录下的 ans.json 中')
print('指令已保存在当前目录下的 指令.txt 中')
print('')
print('Made By Happy2018new')
os.system("pause")
sys.exit()
# 善后