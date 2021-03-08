package aux.hardcoded;

import org.jetbrains.annotations.NotNull;
import org.joda.time.LocalTime;

// only works for
    /*
    {
        "title": "HomePatternDetector",
            "type": "object",
            "additionalProperties": false,
            "properties": {
        "placeId": {
            "type": "number"
        }
    },
        "required": [
            "placeId"
        ]
    }
    */
/*
 * Id: 1 Bedroom      | 00h -> 07h10   : 07h:41 -> 07m:44
 * Id: 2 Kitchen      | 07h11 -> 07h25 (Breakfast): 12h31 -> 13h55 (lunch): 19h31 -> 21h04 (dinner)
 * Id: 3 Bathroom     | 07h26 -> 07h40 : 21h05 -> 21h12
 * Id: 4 Living Room  | 18h -> 19h30 : 21h13 -> 23:59
 * Id: 5 Not home     | 07h45 -> 12h30 : 13h56 -> 17h59
 *
 *
 * Random Events (and probability of happening):
 *  Event #1 "Missing meal":
 *      : Stays in bed instead of eating a meal
 *  Event #2 "Probably Died":
 *      : Doesn't leave the bedroom
 *  Event #3 "Didn't eat at home":
 *      : Self explanatory
 * */

public class HardCodedDay {

    protected static final int BEDROOM = 1;
    protected static final int KITCHEN = 2;
    protected static final int BATHROOM = 3;
    protected static final int LIVING_ROOM = 4;
    protected static final int NOT_HOME = 5;

    protected static LocalTime BED_ROOM_SLEEP_START = LocalTime.parse( "00:00:00" );
    protected static LocalTime BED_ROOM_SLEEP_END = LocalTime.parse( "07:10:00" );

    protected static LocalTime BREAKFAST_START = LocalTime.parse( "07:11:00" );
    protected static LocalTime BREAKFAST_END = LocalTime.parse( "07:25:00" );

    protected static LocalTime BATH_ROOM_MAIN_START = LocalTime.parse( "07:26:00" );
    protected static LocalTime BATH_ROOM_MAIN_END = LocalTime.parse( "07:40:00" );

    protected static LocalTime BED_ROOM_VISIT_START = LocalTime.parse( "07:41:00" );
    protected static LocalTime BED_ROOM_VISIT_END = LocalTime.parse( "07:44:00" );

    protected static LocalTime WORK_MORNING_START = LocalTime.parse( "07:45:00" );
    protected static LocalTime WORK_MORNING_END = LocalTime.parse( "12:30:00" );

    protected static LocalTime LUNCH_START = LocalTime.parse( "12:31:00" );
    protected static LocalTime LUNCH_END = LocalTime.parse( "13:55:00" );

    protected static LocalTime WORK_AFTERNOON_START = LocalTime.parse( "13:56:00" );
    protected static LocalTime WORK_AFTERNOON_END = LocalTime.parse( "17:59:00" );

    protected static LocalTime PROCRASTINATION_START = LocalTime.parse( "18:00:00" );
    protected static LocalTime PROCRASTINATION_END = LocalTime.parse( "19:30:00" );

    protected static LocalTime DINNER_START = LocalTime.parse( "19:31:00" );
    protected static LocalTime DINNER_END = LocalTime.parse( "21:04:00" );

    protected static LocalTime PROCRASTINATION_RETURNS_START = LocalTime.parse( "21:05:00" );
    protected static LocalTime PROCRASTINATION_RETURNS_END = LocalTime.parse( "23:59:00" );


    public int generatePattern(@NotNull LocalTime sampleTime) {

        if( sampleTime.isAfter( BED_ROOM_SLEEP_START ) && sampleTime.isBefore( BED_ROOM_SLEEP_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( BREAKFAST_START ) && sampleTime.isBefore( BREAKFAST_END ) )
            return KITCHEN;

        if( sampleTime.isAfter( BATH_ROOM_MAIN_START ) && sampleTime.isBefore( BATH_ROOM_MAIN_END ) )
            return BATHROOM;

        if( sampleTime.isAfter( BED_ROOM_VISIT_START ) && sampleTime.isBefore( BED_ROOM_VISIT_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( WORK_MORNING_START ) && sampleTime.isBefore( WORK_MORNING_END ) )
            return NOT_HOME;

        if( sampleTime.isAfter( LUNCH_START ) && sampleTime.isBefore( LUNCH_END ) )
            return KITCHEN;

        if( sampleTime.isAfter( WORK_AFTERNOON_START ) && sampleTime.isBefore( WORK_AFTERNOON_END ) )
            return NOT_HOME;

        if( sampleTime.isAfter( PROCRASTINATION_START ) && sampleTime.isBefore( PROCRASTINATION_END ) )
            return LIVING_ROOM;

        if( sampleTime.isAfter( DINNER_START ) && sampleTime.isBefore( DINNER_END ) )
            return KITCHEN;

        if( sampleTime.isAfter( PROCRASTINATION_RETURNS_START ) && sampleTime.isBefore( PROCRASTINATION_RETURNS_END ) )
            return LIVING_ROOM;

        return -99;
    }
}
