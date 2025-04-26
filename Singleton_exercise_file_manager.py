import threading
import datetime

class FileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, file_name = 'audit.log', *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(FileAuditManager, cls).__new__(cls)
                cls._instance._file_name = file_name
                with open(cls._instance._file_name, 'a') as file:
                    file.write(f'Log started: {datetime.datetime.now()}\n')
        return cls._instance

    def log_message(self, message):
        with self._lock:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(self._file_name, 'a') as file:
                file.write(f'{timestamp}: {message}\n')

# Test code to show that the FileAuditManager works as expected
def test_file_audit_manager():
    logger = FileAuditManager('test_audit.log')
    logger.log_message('Test message from thread.')

if __name__ == '__main__':
    threads = []
    for i in range(10):
        thread = threading.Thread(target=test_file_audit_manager)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()