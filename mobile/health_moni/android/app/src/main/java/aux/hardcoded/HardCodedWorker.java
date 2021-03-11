package aux.hardcoded;

import android.content.Context;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.work.Worker;
import androidx.work.WorkerParameters;

public class HardCodedWorker extends Worker {
    private static final String TAG = "HardCodedWorker";

    public HardCodedWorker(@NonNull Context context, @NonNull WorkerParameters workerParams) {
        super(context, workerParams);
    }

    @NonNull
    @Override
    public Result doWork() {

        Log.i(TAG, "Changing HardCoded Object now!");
        HardCodedData hardCodedDataSingleton = HardCodedData.getInstance();
        hardCodedDataSingleton.setNewDay();

        Log.d(TAG, "HardCoded Object changed!");

        return Result.success();
    }
}
