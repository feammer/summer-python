def conflict(state, nextCol):
    """
    判断是否冲突
    因为坐标是从0开始的，所以state的长度代表了下一行的行坐标
    """
    nextRow = rows = len(state)
    # 遍历已有的皇后位置检查冲突
    for row in range(rows):
        # 获取当前行的皇后位置
        column = state[row]
        # 检查 nextCol 和 column 的皇后是否位于同一列或对角线
        if abs(column - nextCol) in [0, nextRow - row]:
            return True
    return False


def queens(num, state=()):
    """
    基于递归采用回溯算法，算出每一种结果
    state表示列坐标，初始为空
    """
    for pos in range(num):
        # 默认state为空。长度为0，但是是不冲突的
        # 判断是否冲突，state为空时不冲突
        if not conflict(state, pos):  # 回溯法的体现
            # 如果state的长度为7，即到达了倒数第二行，也就是前7行皇后都已经找到了位置，最后一行又没有冲突，返回最后一行的列坐标
            if len(state) == num - 1:
                # 最后一行的（pos,）=最后一行的result，然后再递归回去求倒数第二行的result
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    """
                    递归实现求state：
                        1. 向下递归
                        第一次（行）： pos=0，刚开始不会进入if len(state) == num - 1，进入执行else，会执行queens(num, state + (pos, ))，
                        第二次（行）： 进入else，再调用queens(num, state + (pos, )),递归执行queens(num, state + (pos,) + (pos,))
                        第三次（行）： 进入else，再调用queens(num, state + (pos,) + (pos,),递归执行queens(num, state + (pos,) + (pos,) + (pos,))
                        ...
                        第七次（行）： 执行和上面的一样，不过此时state的长度为7
                        第八次（行）： 执行f len(state) == num - 1:求出最后一行的列坐标(pos,)

                        2.向上递归
                        求出第八行的列坐标，就可以求出第七行的（pos,），返回的是第七行和第八行的列坐标（（pos，） + result）
                        根据下一行的结果依次求出上一行的结果；
                        ....
                        最后求出第一行的列坐标，返回整体结果
                    """
                    yield (pos,) + result


def prettyPrint(solution):
    def line(pos, length=len(solution)):
        return '☆' * (pos) + '★' + '☆' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    solutions = queens(8)
    for index, solution in enumerate(solutions):
        print('第%d种解决方案：' % (index + 1), solution)
        prettyPrint(solution)
        print('-' * 40)
