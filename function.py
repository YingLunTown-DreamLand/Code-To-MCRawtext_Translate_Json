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
    \n参数
    `self:list` | 给定的列表的格式是 `[[区间起点:int, 区间终点:int], ……, [区间起点:int, 区间终点:int]]`
        注意：输入的列表的数据应该是单调递增的，且各个子集没有交集。
    \n返回值
    返回补集，且格式不变。
    """
    # 函数声明
    Left = -2147483648
    Right = 2147483647
    # 设定左右边界
    ans = []
    # 初始化
    if len(self) == 1:
        ans.append([Left,self[-1][0]-1])
        ans.append([self[-1][1]+1,Right])
        return ans
    # 当列表元素为 1 时的处理办法
    for i in range(len(self)):
        if Left != self[i][0]:
            ans.append([Left,self[i][0]-1])
        Left = self[i][1]+1
    # 总是对左方取补集
    ans.append([self[-1][1]+1,Right])
    # 对最后一个元素的右方取补集
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
        if i[0] != i[1]:
            ans.append(f'{scoreboardName}=!{i[0]}..{i[1]}')
        else:
            ans.append(f'{scoreboardName}=!{i[-1]}')
    # 对列表内每个元素遍历，并转换为可用的选择器参数，然后放入列表 ans 中
    ans[0] = f'{scoreboardName}=!..{input[0][1]}'
    ans[-1] = f'{scoreboardName}=!{input[-1][0]}..'
    # 处理 ans 列表的首末项数据
    ans = ",".join(ans)
    # 以 "," 为分隔符拼接列表 ans
    return ans
    # 返回值
# 将补集转换为目标选择器参数



def getList(input:dict,scoresConditions:dict)->list:
    """
    \n摘要
    本函数作为一个中转过程，根据给定的分数条件、计分板名称、已有的分数条件，将它们转化为 `scores` 目标选择器参数。
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
    \n返回值
    返回一个 `目标选择器` 及目前已有的 分数条件 ，格式是 `[ 选择器:str, 分数条件:dict ]` 。
    """
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
    return [
        '@s[scores={' + ",".join(ans) + '}]',
        scoresConditions
        ]
    # 返回值



def structuralBody(input:list)->dict:
    """
    \n摘要
    用于处理一个 `结构体` ，然后返回对应的 `JSON` 。
    \n参数
    `scoreboardName:str` 指的是计分板名称。欲被处理的结构体都使用此计分板
    `input:list` 指的是要被处理的结构体
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
    # 初始化
    for i in range(min((len(input)),7)):
        saveData = getList(input[i]['分数条件'],scoresConditions)
        # 取得“目标选择器 及 分数条件”并保存在 saveData 种
        scoresConditions = copy.deepcopy(saveData[1])
        nestedLocation = input[i]['嵌套位置']
        # 取得 分数条件 及 嵌套位置
        ans['rawtext'][0]['with']['rawtext'].append({"selector":saveData[0]})
        # 插入“分数条件”
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
        ans['rawtext'][0]['translate'] = '%%9'
        # 此时应该显示 with 复合标签中的第 9 项元素
        scoresConditions = {}
        for i in range(len(input)):
            scoresConditions = (getList(input[i]['分数条件'],scoresConditions))[1]
        ans['rawtext'][0]['with']['rawtext'].append(
            {
                "selector":(
                    getList(scoresConditions,{})
                    )[0]
            })
        # 此时应筛选出所有条件下的结果，并作为 with 复合标签的第 8 项元素
        for i in saveList:
            ans['rawtext'][0]['with']['rawtext'].append(i)
        # 将 显示内容 插入到 分数条件(目标选择器) 之后
        ans['rawtext'][0]['with']['rawtext'].append(structuralBody(input[7:]))
        # 受限于 MC 本身的牛马特性，最多解析到 with 数组的第 9 项，即 8 个条件及对应的 显示内容
        # 这样的话，我们得把第 8 个条件取所有条件的并集，然后向下递归，直到最内层被完成，然后回递
    # 当输入的 input 列表中的元素个数超过 8 时的处理办法


    else:
        if len(input) == 8:
            ans['rawtext'][0]['translate'] = '%%9'
            # 此时应该显示 with 复合标签中的第 9 项元素
            for k in input[-1]['嵌套位置']:
                input[-1]['内容'][k-1] = structuralBody(input[-1]['内容'][k-1]['结构体'])
            # 解析嵌套的部分
            ans['rawtext'][0]['with']['rawtext'].append(
            {
                "selector":(
                   getList(input[-1]['分数条件'],scoresConditions)
                    )[0]
            })
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