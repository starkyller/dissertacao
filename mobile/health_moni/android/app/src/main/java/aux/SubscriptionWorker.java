package aux;

import android.content.Context;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.work.Worker;
import androidx.work.WorkerParameters;
import androidx.work.ListenableWorker.Result;

public class SubscriptionWorker extends Worker {
    private static final String TAG = "SubscriptionWorker";

    public SubscriptionWorker(@NonNull Context context, @NonNull WorkerParameters workerParams) {
        super(context, workerParams);
    }

    @NonNull
    @Override
    public Result doWork() {
        Log.e(TAG, "work is downe!!");

        return Result.success();
    }
}
