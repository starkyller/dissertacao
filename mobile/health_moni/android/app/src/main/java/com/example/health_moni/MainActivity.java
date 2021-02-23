package com.example.health_moni;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import aux.SubscriptionService;
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;


public class MainActivity extends FlutterActivity {
    private Intent forService;
    private static final String CHANNEL = "com.example.health_moni.messages";
    private SubscriptionService subscriptionService = null;

    BinaryMessenger getFlutterView(){
        return getFlutterEngine().getDartExecutor().getBinaryMessenger();
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //GeneratedPluginRegistrant.registerWith(this);

        forService = new Intent(MainActivity.this, MyService.class);

        new MethodChannel(getFlutterView(), CHANNEL)
                .setMethodCallHandler(new MethodChannel.MethodCallHandler(){

            @Override
            public void onMethodCall(@NonNull MethodCall methodCall, @NonNull MethodChannel.Result result) {

                switch (methodCall.method) {
                    case "startService":
                        startService();
                        subscriptionService = SubscriptionService.getInstance();
                        result.success("Service Started");
                        break;
                    case "loadSubscriptions":
                        HashMap<Object,Object> args = (HashMap<Object, Object>) methodCall.arguments;
                        subscriptionService.setBaseUrl(args.get("baseUrl").toString());
                        subscriptionService.setHeaders((Map<String, String>) args.get("headers"));
                        subscriptionService.addSubscriptionFromArrayList((List<HashMap<Object, Object>>) args.get("subscriptions"));
                        result.success("Subscriptions Loaded");
                        break;
                    default:  //Code for case where you don't recognize the call method
                        result.notImplemented();
                }

            }
        });

    }

    private void startService(){
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.O){
            startForegroundService(forService);
        } else {
            startService(forService);
        }
    }

}
