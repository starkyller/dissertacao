package aux.hardcoded;


import org.joda.time.DateTime;
import org.joda.time.LocalTime;
import org.joda.time.format.DateTimeFormatter;
import org.joda.time.format.ISODateTimeFormat;
import org.json.JSONException;
import org.json.JSONObject;

public class HardCodedData {

    private static HardCodedData singleton = null;
    private DateTime sampleTimeStamp = null;
    private Boolean isDead = false;
    private HardCodedDay simulatedDay = null;



    public static HardCodedData getSingleton() {
        return singleton;
    }

    private HardCodedData(){
        if(this.sampleTimeStamp == null)
            this.sampleTimeStamp = new DateTime();
    }

    public static HardCodedData getInstance() {

        if( singleton == null )
            singleton = new HardCodedData();

        return singleton;
    }

    private static final double EVENT_POSSIBLE_DEATH = 0.0001;
    private static final double EVENT_NO_MEAL = 0.010;
    private static final double EVENT_EAT_OUT = 0.16;


    // Task to run at midnight everyday
    public void setNewDay() {

        if(this.isDead){
            this.simulatedDay = new HardCodedDeath();
            return;
        }

        double endGameProbability = Math.random();

        if(endGameProbability <= EVENT_POSSIBLE_DEATH){
            this.isDead = true;
            this.simulatedDay = new HardCodedDeath();
            return;
        }

        if (endGameProbability <= EVENT_NO_MEAL){
            this.simulatedDay = new HardCodedNoMeal();
            return;
        }

        if (endGameProbability <= EVENT_EAT_OUT){
            this.simulatedDay = new HardCodedDinnerOut();
            return;
        }

        this.simulatedDay = new HardCodedDay();

    }


    public JSONObject GenerateData(int solutionId) {
        /*
        {
            "isValid": false,
            "collectedTimeStamp": null,
            "userSolution": null,
            "dataSample": {
                "placeId": null
            }
        }
        */

        LocalTime sampleTime = LocalTime.now();
        JSONObject jsonObj = new JSONObject();
        JSONObject colData = new JSONObject();
        boolean isValid = true;

        double switchValid = Math.random();
        if(switchValid < 0.005)
            isValid = false;

        int placeId = this.simulatedDay.generatePattern(sampleTime);

        DateTime timestamp = sampleTime.toDateTime(null);
        DateTimeFormatter fmt = ISODateTimeFormat.dateTime();
        //String str = fmt.print(timestamp);


        try {
            jsonObj.put("isValid", isValid);
            jsonObj.put("userSolution", solutionId);
            jsonObj.put("collectedTimeStamp", fmt.print(timestamp));
            colData.put("placeId", placeId);
            jsonObj.put("dataSample", colData);

        } catch (JSONException e) {
            e.printStackTrace();
        }


        return jsonObj;
    }


}



