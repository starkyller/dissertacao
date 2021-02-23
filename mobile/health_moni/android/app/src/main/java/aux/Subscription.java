package aux;

import org.json.JSONObject;

public class Subscription {
    private int id;
    private JSONObject schema;

    public Subscription(int id, JSONObject schema) {
        this.id = id;
        this.schema = schema;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public JSONObject getSchema() {
        return schema;
    }

    public void setSchema(JSONObject schema) {
        this.schema = schema;
    }
}
