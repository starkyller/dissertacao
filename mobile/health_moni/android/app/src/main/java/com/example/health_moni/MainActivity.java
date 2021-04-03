package com.example.health_moni;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.work.ExistingPeriodicWorkPolicy;
import androidx.work.ExistingWorkPolicy;
import androidx.work.OneTimeWorkRequest;
import androidx.work.PeriodicWorkRequest;
import androidx.work.WorkManager;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import aux.SubscriptionService;
import aux.SubscriptionWorker;
import aux.hardcoded.HardCodedWorker;
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;


public class MainActivity extends FlutterActivity {
    private Intent forService;
    private static final String CHANNEL = "com.example.health_moni.messages";
    private SubscriptionService subscriptionService = null;
    public static final String WORK_TAG_POST_DATA ="PostDataWorkerTag";
    public static final String WORK_TAG_HARD_CODED ="WorkiWorkerTag";


    BinaryMessenger getFlutterView() {
        return getFlutterEngine().getDartExecutor().getBinaryMessenger();
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        forService = new Intent(MainActivity.this, MyService.class);

        new MethodChannel(getFlutterView(), CHANNEL)
                .setMethodCallHandler(new MethodChannel.MethodCallHandler() {

                    @Override
                    @SuppressWarnings("unchecked")
                    public void onMethodCall(@NonNull MethodCall methodCall, @NonNull MethodChannel.Result result) {

                        switch (methodCall.method) {
                            case "startService":
                                startService();
                                result.success("Service Started");
                                break;
                            case "loadSubscriptions":
                                HashMap<Object, Object> args =
                                        (HashMap<Object, Object>) methodCall.arguments;

                                loadSubscriptions(args);

                                result.success("Subscriptions Loaded");
                                break;
                            default:  
                                result.notImplemented();
                                break;
                        }

                    }
                });

    }

    private void startService() {
        subscriptionService = SubscriptionService.getInstance(getApplicationContext());

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(forService);
        } else {
            startService(forService);
        }
    }

    @SuppressWarnings("unchecked")
    private void loadSubscriptions(HashMap<Object, Object> args) {

        subscriptionService.setBaseUrl(args.get("baseUrl").toString());
        subscriptionService.setHeaders((Map<String, String>) args.get("headers"));

        List< HashMap<Object, Object> > subscriptionList =
                (List< HashMap<Object, Object> >) args.get("subscriptions");

        subscriptionService.addSubscriptionFromArrayList(subscriptionList);

        startHardCodedWorker();

        OneTimeWorkRequest postData = new OneTimeWorkRequest.Builder(SubscriptionWorker.class).build();

        WorkManager.getInstance(getApplicationContext())
                .enqueueUniqueWork(WORK_TAG_POST_DATA,
                        ExistingWorkPolicy.REPLACE, postData);
    }
    
    private void startHardCodedWorker() {
        
        PeriodicWorkRequest worki = new PeriodicWorkRequest.Builder(
                HardCodedWorker.class,
                15, // change to 24 hours
                TimeUnit.MINUTES
        ).build();
        
        WorkManager.getInstance(getApplicationContext())
                .enqueueUniquePeriodicWork(
                        WORK_TAG_HARD_CODED,
                        ExistingPeriodicWorkPolicy.KEEP,
                        worki);
        
    }

}
