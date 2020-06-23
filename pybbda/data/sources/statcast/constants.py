t = (
    "https://baseballsavant.mlb.com/statcast_search/csv"
    "?all=true"
    "&hfPT="
    "&hfAB="
    "&hfBBT="
    "&hfPR="
    "&hfZ="
    "&stadium="
    "&hfBBL="
    "&hfNewZones="
    "&hfGT=R%7C"
    "&hfC="
    "&hfSea=2019%7C"
    "&hfSit="
    "&player_type=pitcher"
    "&hfOuts=&opponent="
    "&pitcher_throws="
    "&batter_stands="
    "&hfSA=&game_date_gt=2019-09-02"
    "&game_date_lt=2019-09-02"
    "&hfInfield="
    "&team="
    "&position="
    "&hfOutfield="
    "&hfRO="
    "&home_road="
    "&hfFlag="
    "&hfPull="
    "&metric_1="
    "&hfInn="
    "&min_pitches=0"
    "&min_results=0"
    "&group_by=name"
    "&sort_col=pitches"
    "&player_event_sort=h_launch_speed"
    "&sort_order=desc"
    "&min_pas=0"
    "&type=details&"
)

EXAMPLE_URL = (
    "https://baseballsavant.mlb.com/statcast_search/csv?all=true"
    "&hfPT="
    "&hfAB="
    "&hfBBT="
    "&hfPR="
    "&hfZ="
    "&stadium="
    "&hfBBL="
    "&hfNewZones="
    "&hfGT=R%7C"
    "&hfC="
    "&hfSea=2019%7C"
    "&hfSit="
    "&player_type=pitcher"
    "&hfOuts="
    "&opponent="
    "&pitcher_throws="
    "&batter_stands="
    "&hfSA="
    "&game_date_gt=2019-09-02"
    "&game_date_lt=2019-09-02"
    "&hfInfield="
    "&team="
    "&position="
    "&hfOutfield="
    "&hfRO="
    "&home_road="
    "&hfFlag="
    "&hfPull="
    "&metric_1="
    "&hfInn="
    "&min_pitches=0"
    "&min_results=0"
    "&group_by=name"
    "&sort_col=pitches"
    "&player_event_sort=h_launch_speed"
    "&sort_order=desc"
    "&min_pas=0"
    "&type=details"
)

STATCAST_PBP_URL_FORMAT = (
    r"https://baseballsavant.mlb.com/statcast_search/csv"
    r"?all=true"
    r"&{player_id_var}={player_id}"
    r"&game_data_gt={start_date}"
    r"&game_data_lt={end_date}"
    r"&min_pitches=0"
    r"&min_results=0"
    r"&group_by=name"
    r"&sort_col=pitches"
    r"&player_event_sort=h_launch_speed"
    r"&sort_order=desc"
    r"&min_abs=0"
    r"&type=details"
)
