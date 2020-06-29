import   pandas    as        pd


def fetch_state_data(state,state_data):
    state_pops     = state_data.copy()[['Province_State','Population']].groupby('Province_State').sum()
    death_data     = state_data.copy().drop(['UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Lat','Long_','Combined_Key','Population'],axis=1)
    death_data     = death_data.groupby(by='Province_State').sum()
    state_deaths   = death_data.loc[state].copy() / state_pops.loc[state].Population
    return state_deaths


