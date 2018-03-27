import configparser

def raedConfig( path ):
    ConfigParser = configparser.ConfigParser()
    ConfigParser.read( path )
    Section = ConfigParser.sections()[0]
    hostUrl = ConfigParser.get(Section, 'hostUrl')
    contestId = ConfigParser.get(Section, 'contestId')
    maxRegisterPageNumber = ConfigParser.get(Section, 'maxRegisterPageNumber')
    xmlPath = ConfigParser.get(Section, 'eventXmlPath')
    return hostUrl, contestId, maxRegisterPageNumber, xmlPath

if __name__ == '__main__':
    pass
