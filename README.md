# CDOJ-Contest-Result-Analysis



```python
from PageSpider.PageSpider import spideRegisterPage
from ContestData.Submission import getSubmission
from ConfigRead.ConfigRead import raedConfig
from Analysis.Analysis import ProblemAnalysis
import matplotlib.pyplot as plt
%matplotlib inline
```

## 定义如何更新每个Team的提交,保证Modify操作是按照时间顺序进行的


```python
def Modify( SolveStatus , problem , status , time ):
    if problem not in SolveStatus:
        SolveStatus[problem] = ['Not Correct' , 0 , 0]
    if SolveStatus[problem][0] == 'correct':
        return
    SolveStatus[problem][1] = SolveStatus[problem][1] + 1
    if status == 'correct':
        SolveStatus[problem][0] = 'correct'
        SolveStatus[problem][2] = time
```

## 读取配置文件Config.conf，获取相关参数


```python
hostUrl, contestId, maxRegisterPageNumber, xmlPath = raedConfig( 'config.conf' )
```

## 抓取Register页面,并初始化Team的相关参数.

+ TeamSet是一个List,里面的每一项都是一个Dict,初始时每个Dict只有一个Key值,为name,标明这个Team的名字。
+ TeamDict提供了名字到TeamSet下标的映射,是一个Dict,Key值为这个Team的队员的`NickName` + ' ' + `Name`,Value则为在TeamSet中所对应的Index下标。


```python
TeamSet, TeamDict = spideRegisterPage(
    registerurl='http://' + hostUrl + '/contest/registryStatusList' ,
    contestid = int(contestId),
    maxpageindex = int(maxRegisterPageNumber)
)
```

    2018-03-27 21:35:34,470 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 1/25
    2018-03-27 21:35:34,674 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:35,036 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 2/25
    2018-03-27 21:35:35,039 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:35,391 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 3/25
    2018-03-27 21:35:35,391 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:35,707 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 4/25
    2018-03-27 21:35:35,707 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:36,019 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 5/25
    2018-03-27 21:35:36,019 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:36,362 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 6/25
    2018-03-27 21:35:36,362 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:36,691 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 7/25
    2018-03-27 21:35:36,691 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:37,002 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 8/25
    2018-03-27 21:35:37,002 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:37,316 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 9/25
    2018-03-27 21:35:37,316 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:37,618 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 10/25
    2018-03-27 21:35:37,620 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:38,042 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 11/25
    2018-03-27 21:35:38,044 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:38,362 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 12/25
    2018-03-27 21:35:38,362 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:38,668 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 13/25
    2018-03-27 21:35:38,670 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:38,971 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 14/25
    2018-03-27 21:35:38,971 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:39,286 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 15/25
    2018-03-27 21:35:39,286 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:39,637 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 16/25
    2018-03-27 21:35:39,637 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:39,941 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 17/25
    2018-03-27 21:35:39,941 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:40,333 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 18/25
    2018-03-27 21:35:40,333 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:40,654 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 19/25
    2018-03-27 21:35:40,654 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:40,959 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 20/25
    2018-03-27 21:35:40,959 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:41,271 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 21/25
    2018-03-27 21:35:41,275 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:41,589 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 22/25
    2018-03-27 21:35:41,591 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:41,923 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 23/25
    2018-03-27 21:35:41,923 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:42,240 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 24/25
    2018-03-27 21:35:42,240 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    2018-03-27 21:35:42,566 - PageSpider.PageSpider - INFO - Spide RegisterPage Status: 25/25
    2018-03-27 21:35:42,569 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): qscoj.cn
    

## 将Contest导出的XML文件进行解析,获取比赛提交数据.


```python
SubmissionSet = getSubmission( xmlPath )
```

## 按照比赛的时间戳更新每个队伍的状态.


```python
for _ in SubmissionSet:
    setIndex = TeamDict[_.name]
    Modify( SolveStatus = TeamSet[setIndex],
    problem = _.problem,
    status = _.judgeResult,
    time = _.time)
```

## 计算比赛提交的条形图


```python
ListSummary = ProblemAnalysis( TeamSet )
plt.bar(range( 0 , 8 * len( ListSummary ) , 8 ), 
        list(map( lambda x : x[1] , ListSummary )) , 
        align = 'center',color='darkorange', 
        width = 3,
        alpha = 0.73)
plt.bar(range( 3 , 8 * len( ListSummary ) + 3 , 8 ), 
        list(map( lambda x : x[2] , ListSummary )) , 
        align = 'center',color='limegreen', 
        width = 3,
        alpha = 0.73)
plt.title('Submission Summary')
plt.xticks(range(0 , len( ListSummary ) * 8 , 8 ) , map( lambda x : x[0] , ListSummary ) )
for x , y in enumerate( ListSummary ):
    plt.text( 8 * x , int(y[1]) + 10 , '%d' % ( int(y[1]) ) , ha = 'center' )
for x , y in enumerate( ListSummary ):
    plt.text( 3 + 8 * x + 1 , int(y[2]) + 10 , '%d' % ( int(y[2]) ) , ha = 'center' )
plt.show()
```


![png](src/output_12_0.png)


## 计算题目饼状图


```python
ListSummary = ProblemAnalysis( TeamSet )
for _ in ListSummary:
    fig1, ax1 = plt.subplots()
    ax1.pie([_[1] , _[2]], [0 , 0.1], labels= ['Rejected' , 'Accepted'], colors = ['crimson' , 'limegreen'] , autopct='%1.1f%%',
        shadow=True, startangle= 45  )
    ax1.axis('equal')
    ax1.set_title( 'Problem ' + _[0] )
    plt.show()
```


![png](src/output_14_0.png)



![png](src/output_14_1.png)



![png](src/output_14_2.png)



![png](src/output_14_3.png)



![png](src/output_14_4.png)



![png](src/output_14_5.png)



![png](src/output_14_6.png)



![png](src/output_14_7.png)



![png](src/output_14_8.png)



![png](src/output_14_9.png)



![png](src/output_14_10.png)



![png](src/output_14_11.png)



![png](src/output_14_12.png)

