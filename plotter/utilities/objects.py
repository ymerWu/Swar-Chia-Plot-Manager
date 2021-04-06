class Job:
    name = None
    current_work_id = 0

    total_running = 0
    total_completed = 0
    max_concurrent = 0
    max_concurrent_with_disregard = 0
    max_plots = 0

    stagger_minutes = None
    max_for_phase_1 = None
    concurrency_disregard_phase = None
    concurrency_disregard_phase_delay = None

    running_work = []

    temporary_directory = None
    destination_directory = []
    size = None
    bitfield = None
    threads = None
    buckets = None
    memory_buffer = None


class Work:
    work_id = None
    job = None
    pid = None
    log_file = None

    current_phase = 1

    datetime_start = None
    datetime_end = None

    phase_times = {}
    total_run_time = None

    completed = False

    progress = 0

