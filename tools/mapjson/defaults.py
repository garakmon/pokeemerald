# user-defined default fields for map macros

object_event_defaults = {
    'graphics_id' : '0',
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'movement_type' : '0',
    'movement_range_x' : '0',
    'movement_range_y' : '0',
    'trainer_type' : '0',
    'trainer_sight_or_berry_tree_id' : '0',
    'script' : 'NULL',
    'flag' : '0'
}

warp_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'dest_warp_id' : '0',
    'dest_map' : '0'
}

coord_trigger_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'var' : 'VAR_TEMP_0',
    'var_value' : '0',
    'script' : 'NULL'
}

coord_weather_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'weather' : 'COORD_EVENT_WEATHER_SUNNY'
}

bg_sign_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'player_facing_dir' : 'BG_EVENT_PLAYER_FACING_ANY',
    'script' : 'NULL'
}

bg_hidden_item_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'item' : '1',
    'flag' : 'FLAG_HIDDEN_ITEMS_START'
}

bg_secret_base_event_defaults = {
    'x' : '0',
    'y' : '0',
    'elevation' : '3',
    'secret_base_id' : 'SECRET_BASE_RED_CAVE1_1'
}

default_fields = {
    'object_events' : object_event_defaults,
    'warp_events' : warp_event_defaults,
    'trigger_events' : coord_trigger_event_defaults,
    'weather_events' : coord_weather_event_defaults,
    'sign_events' : bg_sign_event_defaults,
    'hidden_item_events' : bg_hidden_item_event_defaults,
    'secret_base_events' : bg_secret_base_event_defaults
}
