package aux.hardcoded;

import org.jetbrains.annotations.NotNull;
import org.joda.time.LocalTime;

public class HardCodedNoMeal extends HardCodedDay{

    /*
    * Only has lunch
    * Stays in bed  all day
    */

    @Override
    public int generatePattern(@NotNull LocalTime sampleTime) {
        if( sampleTime.isAfter( BED_ROOM_SLEEP_START ) && sampleTime.isBefore( BED_ROOM_SLEEP_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( BREAKFAST_START ) && sampleTime.isBefore( BREAKFAST_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( BATH_ROOM_MAIN_START ) && sampleTime.isBefore( BATH_ROOM_MAIN_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( BED_ROOM_VISIT_START ) && sampleTime.isBefore( BED_ROOM_VISIT_END ) )
            return BATHROOM;

        if( sampleTime.isAfter( WORK_MORNING_START ) && sampleTime.isBefore( WORK_MORNING_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( LUNCH_START ) && sampleTime.isBefore( LUNCH_END ) )
            return KITCHEN;

        if( sampleTime.isAfter( WORK_AFTERNOON_START ) && sampleTime.isBefore( WORK_AFTERNOON_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( PROCRASTINATION_START ) && sampleTime.isBefore( PROCRASTINATION_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( DINNER_START ) && sampleTime.isBefore( DINNER_END ) )
            return BEDROOM;

        if( sampleTime.isAfter( PROCRASTINATION_RETURNS_START ) && sampleTime.isBefore( PROCRASTINATION_RETURNS_END ) )
            return BEDROOM;

        return -99;
    }
}
