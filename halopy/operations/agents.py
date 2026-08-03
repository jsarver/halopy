from halopy.paths import  Agent, Team, Roles, Toplevel
from halopy.models import UnameSection


def create_agent(agent_id, **kwargs):
    agent = UnameSection(agent_id=agent_id, **kwargs).__dict__
    return agent


def add_agents_to_team(client, team_id, agents):
    """Adds agents to a team"""
    team = client.get(Team, id=team_id, includedetails=True).json()
    ag_ids = [a['agent_id'] for a in team['agents']]
    for a in agents:
        if a['id'] not in ag_ids:
            team['agents'].append(a)
    print(f"adding agents to team {team['name']}")
    client.create(Team, json=[team])


def add_teams_to_agent(client, agent_id, teams):
    """Adds teams to an agent"""
    agent = client.get(Agent, id=agent_id, includedetails=True).json()
    agent['teams'] = teams
    client.create(Agent, json=[agent])


def set_team_depts_agent_depts(client):
    # get list of all the teams
    team_list = client.list(Team, showall=True).json()

    department_payload = [
        {"type": 1, "organisation_id": "1", "agent_department": True, "id": f"{team["department_id"]}"} for team in
        team_list]
    # updating department 1 at a time, seems to work better
    for dept in department_payload:
        print(f"setting dept:{dept} to an agent dept")
        client.create(Toplevel, json=[dept])


def get_agentlist(client, page_size=50):
    record_count = client.list(Agent, showall=True, pageinate=True, page_size=100, page_no=1).json()['record_count']
    pages = (round(record_count / page_size) + 1)
    agent_list = []
    for page in range(1, pages):
        agent_list.extend(
            client.list(Agent, showall=True, pageinate=True, page_size=page_size, page_no=page).json()['results'])
    return agent_list


def get_role(client, role_id, includedetails=True, **kwargs):
    #returns the role using the roleid
    return client.get(Roles, id=role_id, includedetails=includedetails)


