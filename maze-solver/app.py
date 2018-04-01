from board import Board
from defs import DEFAULT_GRID
from solver import Solver
from agent import Agent

def app():
    board = Board(DEFAULT_GRID)
    agent = Agent(11, 1)
    solver = Solver(board, agent)

    # draw the board cells before the agent starts moving
    board.drawGrid()
    print("\n\n")

    # the agent starts moving
    solver.bfs()
    # draw the grid when the agent has found all treasures
    board.drawGrid()
    # display the total score
    print("\nFinal score", agent.getScore())


app()
