package aux.hardcoded;

import org.jetbrains.annotations.NotNull;
import org.joda.time.LocalTime;

public class HardCodedDeath extends HardCodedDay{
    @Override
    public int generatePattern(@NotNull LocalTime sampleTime) {
        return BEDROOM;
    }
}
