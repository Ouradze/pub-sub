from upciti.pub_sub.workers import run_worker


def test_run_workers(mocker):
    mocker.patch("upciti.pub_sub.workers.Manager")
    process = mocker.patch("upciti.pub_sub.workers.Process")
    process.return_value.start.return_value = True
    process.return_value.join.return_value = True

    mocker.patch("upciti.pub_sub.workers.MotionDetector")
    mocker.patch("upciti.pub_sub.workers.Logger")
    mocker.patch("upciti.pub_sub.workers.SingleShotDetector")

    run_worker()
    # 1 publisher, 1 subscriber and 2 pubsub
    assert process.return_value.start.call_count == 4
    assert process.return_value.join.call_count == 4


def test_run_workers_more_process(mocker):
    mocker.patch("upciti.pub_sub.workers.Manager")
    process = mocker.patch("upciti.pub_sub.workers.Process")
    process.return_value.start.return_value = True
    process.return_value.join.return_value = True

    mocker.patch("upciti.pub_sub.workers.MotionDetector")
    mocker.patch("upciti.pub_sub.workers.Logger")
    mocker.patch("upciti.pub_sub.workers.SingleShotDetector")

    run_worker(workers=5)
    # 1 publisher, 1 subscriber and 5 pubsub
    assert process.return_value.start.call_count == 7
    assert process.return_value.join.call_count == 7
