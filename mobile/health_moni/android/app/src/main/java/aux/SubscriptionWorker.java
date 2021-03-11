package aux;

import android.content.Context;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.work.ExistingWorkPolicy;
import androidx.work.OneTimeWorkRequest;
import androidx.work.WorkManager;
import androidx.work.Worker;
import androidx.work.WorkerParameters;

import com.example.health_moni.MainActivity;

public class SubscriptionWorker extends Worker {
    private static final String TAG = "SubscriptionWorker";
    private static final int MINUTE = 60000;

    public SubscriptionWorker(@NonNull Context context, @NonNull WorkerParameters workerParams) {
        super(context, workerParams);
    }

    @NonNull
    @Override
    public Result doWork() {
        // the android workmanager api doesn't allow less than 15 minutes repetitive works
        // so a hack with the OneTimeWorkRequest must be used
        try {
            Log.d(TAG, "Sleeping before running task.");
            // hack it needs to be more than 1 minute or the work will be canceled
            // need to find a better solution in the future
            Thread.sleep(MINUTE + 5000); //1.5 minutes cycle
            doTheActualProcessingWork();
        } catch (InterruptedException e) {
            Log.d(TAG, "Thread sleep failed...");
            e.printStackTrace();
        }

        return Result.success();
    }


    private void doTheActualProcessingWork(){
        Log.d(TAG, "Running task now!");

        SubscriptionService subscriptionService = SubscriptionService.getInstance(getApplicationContext());

        subscriptionService.startSampleTransmission();

        Log.d(TAG, "Transmission of data concluded!");

        OneTimeWorkRequest refreshWork = new OneTimeWorkRequest.Builder(SubscriptionWorker.class)
                .build();
        WorkManager.getInstance(getApplicationContext())
                .enqueueUniqueWork(MainActivity.WORK_TAG_POST_DATA, ExistingWorkPolicy.REPLACE,
                        refreshWork);
    }

}
