from typing import List, Text


class NoAgentFoundException(Exception):
    def __str__(self):
        return "No Agent Found"


class Agent(object):
    agents = []

    def __init__(self, name, skills, load):
        self._name = name
        self.skills = skills
        self.load = load
        self.agents.append(self._name)

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self._id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented()

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented()


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        try:
            pass
        except:
            raise NoAgentFoundException()


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        try:
            pass
        except:
            raise NoAgentFoundException()


from IPython import embed

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)


least_loaded_policy = LeastLoadedAgent()
# embed()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2])
