from collections import deque
from defs import CELL_PROP
from board import Board


class Solver:
    __board = {}
    __agent = {}

    def __init__(self, board, agent):
        self.__board = board
        self.__agent = agent

    def bfs(self):
        agentPosition = self.__agent.getPosition()
        queue = deque([(agentPosition.x, agentPosition.y, None)])
        treasuresFound = 0
        maxTreasures = 0

        # count nr of treasures for stop condition
        for row in self.__board.getGrid():
            maxTreasures += row.count(CELL_PROP["LUCKY"])

        # make sure there are nodes to check left
        while len(queue) > 0 and treasuresFound < maxTreasures:
            # grab the first node
            node = queue.popleft()
            # get x and y
            self.__agent.setPosition(node[0], node[1])

            agentPosition = self.__agent.getPosition()

            # make sure the agent does not go out of bounds
            if ((agentPosition.x not in range(0, len(self.__board.getGrid()))) or
                (agentPosition.y not in range(0, len(self.__board.getGrid()[0])))):
                continue

            # check if the agent has found a treasure
            if self.__board.getCell(agentPosition.x, agentPosition.y) == CELL_PROP["LUCKY"]:
                # the agent gets 100 points for each found treasure
                self.__agent.updateScore(+100)
                # mark cell as visited
                self.__board.setCellVisited(agentPosition.x, agentPosition.y)
                treasuresFound += 1
                
            if self.__killMonster(agentPosition):
                # make the agent shoot twice to left and right (-25 points each shot)
                self.__agent.updateScore(-50)
                # move further
                continue

            if self.__board.getCell(agentPosition.x, agentPosition.y) == CELL_PROP["DANGEROUS"]:
                # agent loses 1000 points when entering a cell with a monster
                self.__agent.updateScore(-1000)
                # mark cell as visited to not visit again
                self.__board.setCellVisited(agentPosition.x, agentPosition.y)
                # move further
                continue

            # the agend will move only if the cell is empty
            if self.__board.getCell(agentPosition.x, agentPosition.y) != CELL_PROP["EMPTY"]:
                # move somewhere else
                continue

            # mark the current cell the agent is on as visited to avoid it further
            self.__board.setCellVisited(agentPosition.x, agentPosition.y)

            # the agent loses 1 point for each move
            self.__agent.updateScore(-1)

            # the agent will move up, down, left and right
            for cell in [
                [agentPosition.x - 1, agentPosition.y],
                [agentPosition.x + 1, agentPosition.y],
                [agentPosition.x, agentPosition.y - 1],
                [agentPosition.x, agentPosition.y + 1]
            ]:
                # create the new cell, with node as the parent
                queue.append((cell[0], cell[1], node))

    def __killMonster(self, agentPosition):
        # check if agent can shoot
        if ((agentPosition.x not in range(0, len(self.__board.getGrid()) - 1)) or 
            (agentPosition.y not in range(0, len(self.__board.getGrid()[0]) - 1))):
            return False

        # no monsters have been killed in this step
        monsterKilled = False

        # check if monster is on the right
        if self.__board.getCell(agentPosition.x, agentPosition.y + 1) == CELL_PROP["DANGEROUS"]:
            # mark monster cell as empty
            self.__board.setCellEmpty(agentPosition.x, agentPosition.y + 1)
            # the agent gets 50 points for each killed monster
            self.__agent.updateScore(+50)
            # state that the monster has been killed
            monsterKilled = True
        
        # check if monster is on the left
        if self.__board.getCell(agentPosition.x, agentPosition.y - 1) == CELL_PROP["DANGEROUS"]:
            # mark monster cell as empty
            self.__board.setCellEmpty(agentPosition.x, agentPosition.y - 1)
            # the agent gets 50 points for each killed monster
            self.__agent.updateScore(+50)
            # state that the monster has been killed
            monsterKilled = True
            
        return monsterKilled            
