# Import standard library packages.
import math

# Import local packages.
from src.agents.tabular import TabularAgent


def test_matches_closed_form():
    alpha = 0.1
    agent = TabularAgent(n_cues=3, learning_rate=alpha)
    for t in range(1, 21):
        agent.update(0, 1.0)
        assert math.isclose(agent.predict(0), 1 - (1 - alpha) ** t)


def test_preexposure_changes_nothing_when_init_is_zero():
    agent = TabularAgent(n_cues=3, learning_rate=0.1, initial_value=0.0)
    for _ in range(100):
        assert agent.update(0, 0.0) == 0.0
    assert agent.predict(0) == 0.0


def test_cues_are_independent():
    agent = TabularAgent(n_cues=3, learning_rate=0.5)
    agent.update(0, 1.0)
    assert agent.predict(1) == 0.0
    assert agent.predict(2) == 0.0


def test_optimistic_init_decays_during_preexposure():
    agent = TabularAgent(n_cues=3, learning_rate=0.1, initial_value=1.0)
    for _ in range(50):
        agent.update(0, 0.0)
    assert agent.predict(0) < 0.01
