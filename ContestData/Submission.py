import xml.etree.ElementTree as ElementTree

class submission:

    def __init__(self, id, time, name, problem , language):
        self.id = id
        self.time = time
        self.name = name
        self.problem = problem
        self.language = language
        self.judgeResult = 'Submission Result Not Found'

    def __str__(self):
        return str([self.time , self.name , self.problem , self.language , self.judgeResult])

def getSubmission( xmlPath ):
    tree = ElementTree.parse( xmlPath)
    root = tree.getroot()[0]
    summary = []
    for _ in root:
        time = _.attrib['time']
        if _[0].tag == 'submission':
            summary.append(submission(
                id = _[0].attrib['id'],
                time = time,
                name = _[0][0].text,
                problem = _[0][1].attrib['id'],
                language = _[0][2].text
            ))
        else:
            summary[-1].judgeResult = _[0].text
    return summary

if __name__ == '__main__':
    getSubmission('../event.xml' )
