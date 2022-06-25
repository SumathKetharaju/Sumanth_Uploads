import pytest
import sys
import io
import re

if __name__ == '__main__':
    stdout_bak = sys.stdout  # backup stdout
    sys.stdout = io.StringIO()
    pytest.main()
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout_bak  # restore stdout

    print(output)
    #
    # for line in output.splitlines():
    #     # print(line)
    #     fail_pattern = re.compile(r".+FAILED")
    #     fail_match = fail_pattern.search(line)
    #     if fail_match:
    #         print(fail_match.group())
