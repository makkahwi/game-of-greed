from tests.flow.flo import Flo

def test_no_for_wanna_play():
    Flo.test("flow/quitter.sim.txt")

def test_one_and_done():
    Flo.test("flow/one_and_done.sim.txt")

def test_bank_one_roll_then_quit():
    Flo.test("flow/bank_one_roll_then_quit.sim.txt")

def test_bank_first_for_two_rounds_then_quit():
    Flo.test("flow/bank_first_for_two_rounds.sim.txt")

def test_hot_dice():
    Flo.test("flow/hot_dice.sim.txt")
