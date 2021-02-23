package aux;

import com.google.gson.Gson;

import org.jetbrains.annotations.NotNull;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubscriptionService {
    private static SubscriptionService singleton = null;
    private List<Subscription> subscriptions = null;
    private Map<String,String> headers = null;
    private String baseUrl;


    /*
        SubscriptionService
    */
    public static SubscriptionService getSingleton() {
        return singleton;
    }

    private SubscriptionService(){

        if(this.subscriptions == null)
            this.subscriptions = new ArrayList<Subscription>();

        if(this.headers == null)
            this.headers = new HashMap<String,String>();
    }

    public static SubscriptionService getInstance() {

        if( singleton == null )
            singleton = new SubscriptionService();

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
        Gson gson = new Gson();

        for (HashMap<Object,Object> temp : subscriptionList){
            Subscription aux = new Subscription( (int)temp.get("subscriptionId"), getJsonFromMap((Map<String, Object>)temp.get("jsonSchema")) );

            addSubscription(aux);
        }
        //this.subscriptions.add(subscription);
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



}
