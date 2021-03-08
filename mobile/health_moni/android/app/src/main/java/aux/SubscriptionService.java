package aux;

import android.content.Context;
import android.util.Log;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;

import org.jetbrains.annotations.NotNull;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubscriptionService {
    private static final String TAG = "SubscriptionService";
    private static SubscriptionService singleton = null;
    private HardCodedData hardCodedData= null;
    private List<Subscription> subscriptions = null;
    private Map<String,String> headers = null;
    private String baseUrl;
    private RequestQueue requestQueue = null;
    private static Context ctx;


    /*
        SubscriptionService
    */
    public static SubscriptionService getSingleton() {
        return singleton;
    }

    private SubscriptionService(Context context){
        ctx = context;

        if(this.subscriptions == null)
            this.subscriptions = new ArrayList<Subscription>();

        if(this.headers == null)
            this.headers = new HashMap<String,String>();

        if(this.requestQueue == null)
            this.requestQueue = Volley.newRequestQueue(ctx.getApplicationContext());

        if(this.hardCodedData == null){
            this.hardCodedData = HardCodedData.getInstance();
            this.hardCodedData.setNewDay();
        }


    }

    public static SubscriptionService getInstance(Context context) {

        if( singleton == null )
            singleton = new SubscriptionService(context);

        return singleton;
    }

    /*
        List<Subscription>
    */
    public List<Subscription> getSubscriptions() {
        return subscriptions;
    }

    public void addSubscription(Subscription subscription) {
        this.subscriptions.add(subscription);
    }

    public void addSubscriptionFromArrayList(@NotNull List<HashMap<Object,Object>> subscriptionList) {

        for (HashMap<Object,Object> temp : subscriptionList){
            Subscription aux = new Subscription( (int)temp.get("subscriptionId"),
                    getJsonFromMap((Map<String, Object>)temp.get("jsonSchema")) );

            addSubscription(aux);
        }
    }

    private JSONObject getJsonFromMap(Map<String, Object> map) {
        JSONObject jsonData = new JSONObject();
        for (String key : map.keySet()) {
            Object value = map.get(key);
            if (value instanceof Map<?, ?>) {
                value = getJsonFromMap((Map<String, Object>) value);
            }
            try {
                jsonData.put(key, value);
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
        return jsonData;
    }

    public void removeSubscription(int id) {
        this.subscriptions.remove(id);
    }
    /*
        headers
    */
    public Map<String, String> getHeaders() {
        return headers;
    }

    public void setHeaders(Map<String, String> headers) {
        this.headers = headers;
    }

    /*
        baseUrl
    */
    public String getBaseUrl() {
        return baseUrl;
    }

    public void setBaseUrl(String baseUrl) {
        this.baseUrl = baseUrl;
    }

    public void startSampleTransmission(){

        postSubscriptionData();
    }

    private void postSubscriptionData(){
        Subscription temp = subscriptions.get(0);

        Response.Listener<JSONObject> responseListener = new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                Log.i(TAG, response.toString() );
            }
        };

        Response.ErrorListener errorListener = new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Log.e(TAG, error.toString() )
                // save data to try again later
                ;
            }
        };

        JSONObject body = hardCodedData.GenerateData(temp.getId());

        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest
                (Request.Method.POST,
                        this.baseUrl,
                        body,
                        responseListener,
                        errorListener){
            @Override
            public Map<String, String> getHeaders() throws AuthFailureError {
                return headers;
            }
        };


        this.requestQueue.add(jsonObjectRequest);

    }


}
