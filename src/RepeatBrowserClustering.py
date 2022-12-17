
import os
import sys
import time
import json
import shutil
import random
import string
import multiprocessing
from APIFramework import APIFramework, APIFrameworkWithFrontEnd, queue



class RepeatBrowserClustering(APIFrameworkWithFrontEnd):

    def form_task(self, p):
        res = {}

        txt = p["tsv_content"].strip()

        list_id = self.str2hash(txt.encode("utf-8"))

        res["id"] = list_id
        res["tsv_content"] = txt

        return res

    def worker(self, pid, task_queue, result_queue, suicide_queue_pair, params):

        self.output(2, "Worker-%s is starting up" % (pid))

        self.output(2, "Worker-%s is ready to take job" % (pid))

        while True:
            task_detail = self.task_queue_get(task_queue, pid, suicide_queue_pair)

            self.output(2, "Worker-%s is computing task: %s" % (pid, task_detail))

            error = []
            calculation_start_time = time.time()

            try:
                os.mkdir("./task/")
            except:
                pass

            list_id = task_detail["id"]
            txt = task_detail["tsv_content"]

            print(txt)



            result = txt[:100]

            calculation_end_time = time.time()
            calculation_time_cost = calculation_end_time - calculation_start_time

            self.output(2, "Worker-%s finished computing job (%s)" % (pid, list_id))

            res = {
                "id": list_id,
                "start time": calculation_start_time,
                "end time": calculation_end_time,
                "runtime": calculation_time_cost,
                "error": error,
                "result": result
            }

            self.output(2, "Job (%s): %s" % (list_id, res))

            result_queue.put(res)




if __name__ == '__main__':
    multiprocessing.freeze_support()

    RepeatBrowserClustering_App = RepeatBrowserClustering()
    RepeatBrowserClustering_App.find_config("RepeatBrowserClustering.ini")
    RepeatBrowserClustering_App.start()




