import copy
import json
import os
# 载入依赖项



def purification(self:list)->list:
    """
    \n摘要
    如函数名字 `purification` 一样，其用途是提纯列表的，剔除重复的区间且只保留更晚添加的区间。
    \n参数
    `self:list` | 给定的列表的格式是 `[[区间起点:int, 区间终点:int], ……, [区间起点:int, 区间终点:int]]`
    \n返回值
    返回提纯好的列表，且单调递增、格式不变。
    """
    # 函数声明
    self = copy.deepcopy(self)
    # 深拷贝列表
    for i in range(len(self)):
        if self[i][0] == 'max' or self[i][0] == 'Max':
            self[i][0] = 2147483647
        if self[i][0] == 'min' or self[i][0] == 'Min':
            self[i][0] = -2147483648
        if self[i][1] == 'max' or self[i][1] == 'Max':
            self[i][1] = 2147483647
        if self[i][1] == 'min' or self[i][1] == 'Min':
            self[i][1] = -2147483648
    # 替换
    self = [[min(i[0],i[1]),max(i[0],i[1])] for i in self]
    self.sort()
    # 以列表 self 中每个元素的最左边的数作为基准进行排序，使得总体大体单调递增
    for i in range(len(self)-1):
        try:
            if self[i][0] <= self[i+1][0] <= self[i][1]:
                0/0
        except ZeroDivisionError:
            0/0
        except:
            None
    # 若发现区间重复，则抛出错误
    return self
    # 返回值
# 提纯列表



def getComplementarySet(self:list)->list:
    """
    \n摘要
    如函数名字 `getComplementarySet` 一样，其用途是取全集-2147483648到2147483647(含边界)的补集的。
    如果提供的集合在取并集后若其本身就是全集，则返回全集。
    \n参数
    `self:list` | 给定的列表的格式是 `[[区间起点:int, 区间终点:int], ……, [区间起点:int, 区间终点:int]]`
        注意：输入的列表的数据应该是单调递增的，且各个子集没有交集。
    \n返回值
    返回补集，但格式变更为 `[[区间起点:int, 区间终点:int, 类型:bool], [区间起点:int, 区间终点:int, 类型:bool], ……, [区间起点:int, 区间终点:int, 类型:bool]]` 。
    其中，`类型:bool` 指的是此区间是否需要被反选。
    """
    # 函数声明
    Left = -2147483648 # 设定左边界
    Right = 2147483647 # 设定右边界
    ans = []
    # 初始化

    if len(self) == 1:
        ans.append([self[-1][0],self[-1][1],0])
        return ans
    # 当列表元素为 1 时的处理办法

    for i in range(len(self)):
        if (Left != self[i][0]) and (self[i][0] > -2147483648):
            ans.append([Left,self[i][0]-1,1])
        Left = self[i][1]+1
    # 总是对左方取补集
    if self[-1][1] < 2147483647:
        ans.append([self[-1][1]+1,Right,1])
    # 对最后一个元素的右方取补集

    if len(ans) == 0:
        return [[-2147483648,2147483647,0]] # 此时补集为空集，因此此时应当取全集
    else:
        return ans
    # 返回结果
# 取补集



def outputSelector(input:list,scoreboardName:str)->str:
    """
    \n摘要
    如函数名字 `outputSelector` 一样，其用途是将补集转换为 `scores` 目标选择器参数
    \n参数
    `input:list` 得到的补集，其是一个列表
    `scoreboardName:str` 一个字符串，即计分板名称
    \n返回值
    返回字符串，是转换好的 `scores` 目标选择器参数，格式为 `计分板=!区间,计分板=!区间, ……, 计分板=!区间`
    """
    # 函数声明
    ans = []
    # 初始化
    for i in input:
        if i[2] == 0:
            if i[0] == i[1]:
                ans.append(f'{scoreboardName}={i[0]}')
                continue
            if i[0] == -2147483648 and i[1] == 2147483647:
                ans.append(f'{scoreboardName}=-2147483648..2147483647')
                continue
            if i[0] == -2147483648 and i[1] != 2147483647:
                ans.append(f'{scoreboardName}=..{i[1]}')
                continue
            if i[0] != -2147483648 and i[1] == 2147483647:
                ans.append(f'{scoreboardName}={i[0]}..')
                continue
            if i[0] != -2147483648 and i[1] != 2147483647:
                ans.append(f'{scoreboardName}={i[0]}..{i[1]}')
                continue
        else:
            if i[0] == i[1]:
                ans.append(f'{scoreboardName}=!{i[0]}')
                continue
            if i[0] == -2147483648 and i[1] != 2147483647:
                ans.append(f'{scoreboardName}=!..{i[1]}')
                continue
            if i[0] != -2147483648 and i[1] == 2147483647:
                ans.append(f'{scoreboardName}=!{i[0]}..')
                continue
            if i[0] != -2147483648 and i[1] != 2147483647:
                ans.append(f'{scoreboardName}=!{i[0]}..{i[1]}')
                continue
    # 对列表内每个元素遍历，并转换为可用的选择器参数，然后放入列表 ans 中
    ans = ",".join(ans)
    # 以 "," 为分隔符拼接列表 ans
    return ans
    # 返回值
# 将补集转换为目标选择器参数



def getList(input:dict,scoresConditions:dict,selector:str,othersSelector:list)->list:
    """
    \n摘要
    本函数作为一个中转过程，根据给定的分数条件、计分板名称、已有的分数条件 及 其他选择器参数 ，将它们组合为一个整体的 `目标选择器` 。
    \n参数
    `input:dict` 指的是一个包含若干个分数条件的列表，格式如下。
    \n
    `{`
        `"scoreboardA":[ [start, end], [start, end], ……, [start, end] ],`
        `"scoreboardB":[ [start, end], [start, end], ……, [start, end] ],`
        \n
        `……,`
        `"scoreboardN":[ [start, end], [start, end], ……, [start, end] ]`
    `}`
    \n
    `scoresConditions:dict` 指的是已有的条件，格式同 `input:dict` 不变
    `selector:str` 指的是选择器，形如 `@s, @r, @e, @p`
    `othersSelector:list` 指的是其他的选择器参数，格式类似于 `["x=1","r=3","rm=1"]`
    \n返回值
    返回一个 `目标选择器` 及目前已有的 分数条件 ，格式是 `[ 选择器:str, 分数条件:dict ]` 。
    """
    # 函数声明
    ans = []
    # 初始化

    for i in input:
        if not i in scoresConditions:
            scoresConditions[i] = []
        scoreConditions = [k for k in input[i]]
        scoresConditions[i] = scoresConditions[i] + scoreConditions
        # 取得“分数条件”
        try:
            ans.append(outputSelector(getComplementarySet(purification(scoresConditions[i])),i))
        except ZeroDivisionError:
            print('错误：您给出的 分数条件 存在重复的区间，请检查后重试。被检测到的可能的重复的区间如下：')
            print(
                json.dumps(
                    scoresConditions[i],
                    sort_keys=True,
                    indent=4,
                    separators=(', ', ': '),
                    ensure_ascii=False
                    )
                )
            os.system("pause")
            0/0
        # 得到对应的选择器参数

    if len(ans) == 0 and len(othersSelector) == 0:
        (1).encode()
    # 如果没有给任何条件（分数、其他目标选择器参数），则返回一个错误
    result = []
    if len(ans) > 0:
        ans = result.append('scores={' + ",".join(ans) + '}')
    # 对 scores 部分进行一个简单的处理
    if len(othersSelector) > 0:
        result = result + othersSelector
    # 对 其他目标选择器参数 部分进行一个简单的处理

    return [
        selector + '[' + ",".join(result) + ']',
        scoresConditions
        ]
    # 返回值



def checkIfNeedToJump(existing:dict,conditions:dict)->bool:
    """
    \n摘要
    根据已有的条件和提供的条件，判断是否需要进行 `if else` 嵌套。
    \n参数
    `existing:dict` 指的是目前已经存在的条件
    `conditions:dict` 指的是提供的条件
    \n返回值
    如果提供的条件数大于已有的条件数，则返回 `True` 。特别地，如果已有的条件数为 `0` ，则永远返回 `False` 。\n
    当为 `True` 时，视为需要嵌入 `if else` 结构体，反则否之。
    """
    # 函数声明
    if len(existing.keys()) == 0:
        return False
    # 如果目前不存在条件，则无需使用 if else 结构
    else:
        if set(existing.keys()) | set(conditions.keys()) != set(existing.keys()):
            return True
        else:
            return False
    # 如果目前已有条件且两者的并集不等价，则视为 提供的条件 > 已经存在的条件



def checkIfSelectorIsChanged(selector:str,lastSelector:str)->bool:
    """
    \n摘要
    根据上次的选择器及现在的选择器，判断是否需要进行 `if else` 嵌套。
    \n参数
    `selector:str` 指的是目前的选择器
    `lastSelector:str` 指的是上一次的选择器
    \n返回值
    如果当前的选择器不是上一次的选择器，则返回 `True` ，否则返回 `False` 。
    """
    # 函数声明
    if lastSelector == None:
        return False
    else:
        if selector != lastSelector:
            return True
        else:
            return False
    # 返回值



def structuralBody(input:list,ifElseStructural:bool=False)->dict:
    """
    \n摘要
    用于处理一个 `结构体` ，然后返回对应的 `JSON` 。
    \n参数
    `input:list` 指的是要被处理的结构体
    `ifElseStructural:bool` 指的是当前处理的结构体是否是一个 `if else` 结构体
    \n返回值
    返回对应的 `JSON` 形式，数据类型是 `dict` 。
    """
    # 函数声明



    ans = {
        "rawtext":[
            {
                "translate":"",
                "with":{"rawtext":[]}
            }
        ]
    }
    scoresConditions = {}
    saveList = []
    lastSelector = None
    # 初始化



    if ifElseStructural == True:
        ans['rawtext'][0]['translate'] = '%%2'
    # 如果当前正在处理一个 if else 结构体，则永远为 %%2



    for i in range(min((len(input)),7)):
        if ifElseStructural == True and i > 0:
            ans['rawtext'][0]['with']['rawtext'].append(saveList[0])
            # 插入“显示内容”
            if len(input[i]['显示条件']['其他目标选择器参数']) > 0:
                ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[i:],True))
                return ans
            else:
                ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[i:],False))
                return ans
            # 这个时候区分两种情况，也就是需要继续嵌套一个 if else 结构体，或者跳出并进入正常状态
        # 当前正在处理一个 if else 结构体时的处理办法

        if ifElseStructural == False and len(input[i]['显示条件']['其他目标选择器参数']) > 0 and (
            len(ans['rawtext'][0]['with']['rawtext']) > 0
        ):
            ans['rawtext'][0]['translate'] = '%%' + str(len(ans['rawtext'][0]['with']['rawtext']) + 1)
            # 此时应该显示 with 复合标签中的第 条件数+1 项元素
            for m in saveList:
                ans['rawtext'][0]['with']['rawtext'].append(m)
            # 将 显示内容 插入到 分数条件(目标选择器) 之后
            ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[i:],True))
            # 处理后续的部分(嵌套)
            return ans
            # 返回值
        # 如果给了 其他目标选择器参数 条件，则需要嵌入一个 if else 结构体
        # 为什么这样干应该很好理解，因为你很容易就可以证明，除了 scores 选择器参数外，
        # 其他任何的选择器参数几乎都不支持“取补集”，因此也就只能这样一堆 if else 下去了
        # 如果是手写 JSON 的话，你的大脑应该会爆炸，所以我加入了这个功能后，你应该好好感谢我~
        # 对了，我喜欢可爱滴男孩纸（划掉）
        # 我就是个颜控罢了~

        if (checkIfNeedToJump(
            scoresConditions,
            input[i]['显示条件']['分数条件']
            ) == True) or (
            checkIfSelectorIsChanged(input[i]['显示条件']['目标选择器'],
            lastSelector) == True):
            ans['rawtext'][0]['translate'] = '%%' + str(len(ans['rawtext'][0]['with']['rawtext']) + 1)
            # 此时应该显示 with 复合标签中的第 条件数+1 项元素
            for m in saveList:
                ans['rawtext'][0]['with']['rawtext'].append(m)
            # 将 显示内容 插入到 分数条件(目标选择器) 之后
            ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[i:]))
            # 处理后续的部分(嵌套)
            return ans
            # 返回值
        # 如果当前给出的分数条件无法满足已有的分数条件，则使用 if 结构体

        try:
            saveData = getList(
                input[i]['显示条件']['分数条件'],
                scoresConditions,
                input[i]['显示条件']['目标选择器'],
                input[i]['显示条件']['其他目标选择器参数']
                )
        except AttributeError:
            print(
                '错误：您不能提供空条件。您应当保证 分数条件 或 其他选择器参数 至少提供一个条件。'+ 
                '具体错误发生在：\n'+f'{input[i]}')
            os.system("pause")
            0/0
        # 取得“目标选择器 及 分数条件”并保存在 saveData 中
        scoresConditions = copy.deepcopy(saveData[1])
        nestedLocation = input[i]['嵌套位置']
        # 取得 分数条件 及 嵌套位置
        ans['rawtext'][0]['with']['rawtext'].append({"selector":saveData[0]})
        lastSelector = input[i]['显示条件']['目标选择器']
        # 插入“分数条件”并刷新“上一次选择器”
        for k in nestedLocation:
            input[i]['内容'][k-1] = structuralBody(input[i]['内容'][k-1]['结构体'])
        # 解析嵌套的部分
        if len(input[i]['内容']) > 1:
            saveList.append({"rawtext":input[i]['内容']})
        else:
            if len(input[i]['内容']) == 1:
                saveList.append(input[i]['内容'][0])
            else:
                saveList.append({"text":""})
        # 放入“显示内容”
    # 处理至多 7 项的内容


    if len(input) > 8:
        ans['rawtext'][0]['translate'] = '%%8'
        # 此时应该显示 with 复合标签中的第 8 项元素
        for i in saveList:
            ans['rawtext'][0]['with']['rawtext'].append(i)
        # 将 显示内容 插入到 分数条件(目标选择器) 之后
        ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[7:]))
        # 受限于 MC 本身的牛马特性，最多解析到 with 数组的第 9 项，即 8 个条件及对应的 显示内容
        # 不过你仔细分析一下就知道为什么这里用 %%8 而非 %%9
        # 这样的话，我们就作一个 if else 结构，然后向下递归，直到最内层被完成，然后回递
    # 当输入的 input 列表中的元素个数超过 8 时的处理办法


    else:
        if len(input) == 8:
            if ifElseStructural == False and len(input[-1]['显示条件']['其他目标选择器参数']) > 0:
                ans['rawtext'][0]['translate'] = '%%8'
                # 此时应该显示 with 复合标签中的第 8 项元素
                for m in saveList:
                    ans['rawtext'][0]['with']['rawtext'].append(m)
                # 将 显示内容 插入到 分数条件(目标选择器) 之后
                ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[-1],True))
                # 处理后续的部分(嵌套)
                return ans
                # 返回值
            # 如果给了 其他目标选择器参数 条件，则需要嵌入一个 if else 结构体
            # 为什么这样干应该很好理解，因为你很容易就可以证明，除了 scores 选择器参数外，
            # 其他任何的选择器参数几乎都不支持“取补集”，因此也就只能这样一堆 if else 下去了
            # 如果是手写 JSON 的话，你的大脑应该会爆炸，所以我加入了这个功能后，你应该好好感谢我~
            # 对了，我喜欢可爱滴男孩纸（划掉）
            # 我就是个颜控罢了~

            if (checkIfNeedToJump(
                scoresConditions,
                input[-1]['显示条件']['分数条件']
                ) == True) or (
                checkIfSelectorIsChanged(input[-1]['显示条件']['目标选择器'],
                lastSelector) == True):
                ans['rawtext'][0]['translate'] = '%%8'
                # 此时应该显示 with 复合标签中的第 8 项元素
                for m in saveList:
                    ans['rawtext'][0]['with']['rawtext'].append(m)
                # 将 显示内容 插入到 分数条件(目标选择器) 之后
                ans['rawtext'][0]['with']['rawtext'].append(structuralBody([input[-1]]))
                # 处理后续的部分(嵌套)
                return ans
                # 返回值
            # 如果当前给出的条件无法满足已有的条件，则使用 if 结构体

            ans['rawtext'][0]['translate'] = '%%9'
            # 此时应该显示 with 复合标签中的第 9 项元素
            for k in input[-1]['嵌套位置']:
                input[-1]['内容'][k-1] = structuralBody(input[-1]['内容'][k-1]['结构体'])
            # 解析嵌套的部分
            try:
                ans['rawtext'][0]['with']['rawtext'].append(
                {
                    "selector":(
                        getList(
                            input[-1]['显示条件']['分数条件'],
                            scoresConditions,
                            input[-1]['显示条件']['目标选择器'],
                            input[-1]['显示条件']['其他目标选择器参数']
                            ))[0]
                })
            except AttributeError:
                print(
                    '错误：您不能提供空条件。您应当保证 分数条件 或 其他选择器参数 至少提供一个条件。'+ 
                    '具体错误发生在：\n'+f'{input[-1]}')
                os.system("pause")
                0/0
            # 放入“分数条件”
            if len(input[-1]['内容']) > 1:
                saveList.append({"rawtext":input[-1]['内容']})
            else:
                if len(input[-1]['内容']) == 1:
                    saveList.append(input[-1]['内容'][0])
                else:
                    saveList.append({"text":""})
            # 放入“显示内容”
        # 当输入的 input 列表中的元素个数为 8 时的处理办法

        else:
            ans['rawtext'][0]['translate'] = '%%' + str(len(ans['rawtext'][0]['with']['rawtext']) + 1)
            # 此时应该显示 with 复合标签中的第 条件数+1 项元素
        # 当输入的 input 列表中的元素小于 8 时的处理办法

        for i in saveList:
            ans['rawtext'][0]['with']['rawtext'].append(i)
        # 将 显示内容 插入到 分数条件(目标选择器) 之后
    # 当输入的 input 列表中的元素个数小于等于 8 时的处理办法
    return ans
    # 返回值