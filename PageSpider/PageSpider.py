from json import loads
from requests import post, Response
from time import sleep
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def getPage(registerurl, contestid, pageindex, TeamSet, TeamDict, Occur):
    response = post(
        url = registerurl,
        json={
            "contestId": contestid,
            "currentPage": pageindex,
            "orderFields": "contestTeamId",
            "orderAsc": "false",
            "teamId": None,
            "status": None,
        })
    data = loads(response.text)['list']
    for _ in data:
        if _['statusName'] == 'Accepted':
            TeamList = _['teamUsers']
            TeamName = _['teamName']
            if TeamName in Occur:
                continue
            Occur.add( TeamName )
            for eachUser in TeamList:
                TeamDict[eachUser['nickName'] + ' ' +
                         eachUser['name']] = len( Occur ) - 1
            TeamSet.append({ 'Teamname' : TeamName })

def spideRegisterPage(registerurl, contestid, maxpageindex):
    TeamSet , TeamDict , Occur = [] , {} , set()
    for _ in range( maxpageindex ):
        logger.info( 'Spide RegisterPage Status: ' + str(_ + 1) + '/' + str(maxpageindex) )
        getPage(registerurl, contestid, _ + 1, TeamSet, TeamDict, Occur)
        sleep( 0.2 )
    return TeamSet , TeamDict

if __name__ == '__main__':
    Teamset , Teamdict = spideRegisterPage('http://qscoj.cn/contest/registryStatusList' , 199, 25)
    for _ in Teamset:
        print( _ )
    for _ in Teamdict:
        print( _ , Teamdict[_] )