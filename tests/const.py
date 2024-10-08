TESTFILE_SHAPE = (55074, 7)
TESTFILE_DIR = "files"
DEFAULT_TESTFILE_NAME = "Test_Inventory_VMs.{}"

SERVER_NAME_MATCHES = {
    "CentOS 4/5 (64-bit)": {"OS_Name": "CentOS", "OS_Version": "4/5 ", "Architecture": "64-bit"},
    "CentOS 4/5/6 (32-bit)": {"OS_Name": "CentOS", "OS_Version": "4/5/6 ", "Architecture": "32-bit"},
    "CentOS 4/5/6 (64-bit)": {"OS_Name": "CentOS", "OS_Version": "4/5/6 ", "Architecture": "64-bit"},
    "CentOS 4/5/6/7 (64-bit)": {"OS_Name": "CentOS", "OS_Version": "4/5/6/7 ", "Architecture": "64-bit"},
    "CentOS 6 (64-bit)": {"OS_Name": "CentOS", "OS_Version": "6 ", "Architecture": "64-bit"},
    "CentOS 7 (64-bit)": {"OS_Name": "CentOS", "OS_Version": "7 ", "Architecture": "64-bit"},
    "Debian GNU/Linux 5 (64-bit)": {"OS_Name": "Debian GNU/Linux", "OS_Version": "5 ", "Architecture": "64-bit"},
    "Debian GNU/Linux 8 (64-bit)": {"OS_Name": "Debian GNU/Linux", "OS_Version": "8 ", "Architecture": "64-bit"},
    "Debian GNU/Linux 9 (64-bit)": {"OS_Name": "Debian GNU/Linux", "OS_Version": "9 ", "Architecture": "64-bit"},
    "FreeBSD 13 or later versions (64-bit)": {
        "OS_Name": "FreeBSD 13 or later versions",
        "OS_Version": None,
        "Architecture": "64-bit",
    },
    "FreeBSD Pre-11 versions (64-bit)": {
        "OS_Name": "FreeBSD Pre-11 versions",
        "OS_Version": None,
        "Architecture": "64-bit",
    },
    "Linux 4.18.0-477.27.2.el8_8.x86_64 AlmaLinux 8.8 (Sapphire Caracal) 8.8 AlmaLinux 8.8 (Sapphire Caracal) cpe:/o:almalinux:almalinux:8::baseos": None,
    "Linux 6.1.11 Other Linux 6.x and later kernel": None,
    "Oracle Linux 4/5 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "4/5 ", "Architecture": "64-bit"},
    "Oracle Linux 4/5/6 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "4/5/6 ", "Architecture": "64-bit"},
    "Oracle Linux 4/5/6/7 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "4/5/6/7 ", "Architecture": "64-bit"},
    "Oracle Linux 6 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "6 ", "Architecture": "64-bit"},
    "Oracle Linux 7 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "7 ", "Architecture": "64-bit"},
    "Oracle Linux 8 (64-bit)": {"OS_Name": "Oracle Linux", "OS_Version": "8 ", "Architecture": "64-bit"},
    "Other (32-bit)": {"OS_Name": "Other", "OS_Version": None, "Architecture": "32-bit"},
    "Other (64-bit)": {"OS_Name": "Other", "OS_Version": None, "Architecture": "64-bit"},
    "Other 2.6.x Linux (32-bit)": {"OS_Name": "Other 2.6.x Linux", "OS_Version": None, "Architecture": "32-bit"},
    "Other 2.6.x Linux (64-bit)": {"OS_Name": "Other 2.6.x Linux", "OS_Version": None, "Architecture": "64-bit"},
    "Other 3.x Linux (64-bit)": {"OS_Name": "Other 3.x Linux", "OS_Version": None, "Architecture": "64-bit"},
    "Other 3.x or later Linux (64-bit)": {
        "OS_Name": "Other 3.x or later Linux",
        "OS_Version": None,
        "Architecture": "64-bit",
    },
    "Other 4.x or later Linux (64-bit)": {
        "OS_Name": "Other 4.x or later Linux",
        "OS_Version": None,
        "Architecture": "64-bit",
    },
    "Other 5.x or later Linux (64-bit)": {
        "OS_Name": "Other 5.x or later Linux",
        "OS_Version": None,
        "Architecture": "64-bit",
    },
    "Other Linux (64-bit)": {"OS_Name": "Other Linux", "OS_Version": None, "Architecture": "64-bit"},
    "Red Hat Enterprise Linux 5 (32-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "5 ",
        "Architecture": "32-bit",
    },
    "Red Hat Enterprise Linux 5 (64-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "5 ",
        "Architecture": "64-bit",
    },
    "Red Hat Enterprise Linux 6 (64-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "6 ",
        "Architecture": "64-bit",
    },
    "Red Hat Enterprise Linux 7 (64-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "7 ",
        "Architecture": "64-bit",
    },
    "Red Hat Enterprise Linux 8 (64-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "8 ",
        "Architecture": "64-bit",
    },
    "Red Hat Enterprise Linux 9 (64-bit)": {
        "OS_Name": "Red Hat Enterprise Linux",
        "OS_Version": "9 ",
        "Architecture": "64-bit",
    },
    "SUSE Linux Enterprise 10 (64-bit)": {
        "OS_Name": "SUSE Linux Enterprise",
        "OS_Version": "10 ",
        "Architecture": "64-bit",
    },
    "SUSE Linux Enterprise 11 (64-bit)": {
        "OS_Name": "SUSE Linux Enterprise",
        "OS_Version": "11 ",
        "Architecture": "64-bit",
    },
    "SUSE Linux Enterprise 12 (64-bit)": {
        "OS_Name": "SUSE Linux Enterprise",
        "OS_Version": "12 ",
        "Architecture": "64-bit",
    },
    "SUSE Linux Enterprise 15 (64-bit)": {
        "OS_Name": "SUSE Linux Enterprise",
        "OS_Version": "15 ",
        "Architecture": "64-bit",
    },
    "SUSE Linux Enterprise 8/9 (64-bit)": {
        "OS_Name": "SUSE Linux Enterprise",
        "OS_Version": "8/9 ",
        "Architecture": "64-bit",
    },
    "SUSE openSUSE (64-bit)": {"OS_Name": "SUSE openSUSE", "OS_Version": None, "Architecture": "64-bit"},
    "Ubuntu Linux (32-bit)": {"OS_Name": "Ubuntu Linux", "OS_Version": None, "Architecture": "32-bit"},
    "Ubuntu Linux (64-bit)": {"OS_Name": "Ubuntu Linux", "OS_Version": None, "Architecture": "64-bit"},
    "VM OS": None,
    "VMware ESXi 6.x": None,
    "VMware Photon OS (64-bit) ": {"OS_Name": "VMware Photon OS", "OS_Version": None, "Architecture": "64-bit"},
    "Microsoft Windows 10 (64-bit)": {"OS_Name": "Microsoft Windows", "OS_Version": "10", "Architecture": "64-bit"},
    "Microsoft Windows 2000 Professional": None,
    "Microsoft Windows 7 (32-bit)": {"OS_Name": "Microsoft Windows", "OS_Version": "7", "Architecture": "32-bit"},
    "Microsoft Windows 7 (64-bit)": {"OS_Name": "Microsoft Windows", "OS_Version": "7", "Architecture": "64-bit"},
    "Microsoft Windows Server 2003 (32-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2003",
        "Architecture": "32-bit",
    },
    "Microsoft Windows Server 2003 Standard (32-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2003",
        "Architecture": None,
    },
    "Microsoft Windows Server 2008 (32-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2008",
        "Architecture": "32-bit",
    },
    "Microsoft Windows Server 2008 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2008",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Server 2008 R2 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2008 R2",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Server 2012 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2012",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Server 2016 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2016",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Server 2016 or later (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2016",
        "Architecture": None,
    },
    "Microsoft Windows Server 2019 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2019",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Server 2022 (64-bit)": {
        "OS_Name": "Microsoft Windows Server",
        "OS_Version": "2022",
        "Architecture": "64-bit",
    },
    "Microsoft Windows Vista (32-bit)": {
        "OS_Name": "Microsoft Windows",
        "OS_Version": "Vista",
        "Architecture": "32-bit",
    },
    "Microsoft Windows XP Professional (32-bit)": {
        "OS_Name": "Microsoft Windows",
        "OS_Version": "XP Professional",
        "Architecture": "32-bit",
    },
}

CLI_OPTIONS = {
    "default": {},
    "disk_space_range_both_env": {
        "get-disk-space-ranges": True,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "both",
    },
    "disk_space_range_prod_env": {
        "get-disk-space-ranges": True,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "prod",
    },
    "disk_space_range_prod_env_by_terabyte": {
        "breakdown-by-terabyte": True,
        "get-disk-space-ranges": True,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "prod",
    },
    "os_min_counts": {
        "get-os-counts": True,
        "minimum-count": 500,
    },
    "supported_os_all_envs": {
        "get-supported-os": True,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "all",
    },
    "supported_os_both_envs": {
        "get-supported-os": True,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "both",
    },
    "supported_os_min_count": {
        "get-supported-os": True,
        "minimum-count": 500,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "all",
    },
    "supported_os_non_prod": {
        "get-supported-os": True,
        "minimum-count": 500,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "non-prod",
    },
    "unsupported_os_both": {
        "get-unsupported-os": True,
        "minimum-count": 500,
        "prod-env-labels": "Prod-DC2,Prod-DC1",
        "sort-by-env": "both",
    },
}

EXPECTED_CLI_OUTPUT = {
    "disk_space_range_both_env": (
        "Environment                            non-prod   prod       \n"
        "0-200 GB                               2312       5082      \n"
        "201-400 GB                             6176       12970     \n"
        "401-600 GB                             3338       5232      \n"
        "601-900 GB                             1828       6744      \n"
        "901-1500 GB                            1039       3580      \n"
        "1501-2000 GB                           253        658       \n"
        "2001-3000 GB                           1398       915       \n"
        "3001-5000 GB                           338        821       \n"
        "5001-9000 GB                           131        1006      \n"
        "9001-114256 GB                         65         707"
    ),
    "disk_space_range_prod_env": (
        "Environment                            prod       \n"
        "0-200 GB                               5082      \n"
        "201-400 GB                             12970     \n"
        "401-600 GB                             5232      \n"
        "601-900 GB                             6744      \n"
        "901-1500 GB                            3580      \n"
        "1501-2000 GB                           658       \n"
        "2001-3000 GB                           915       \n"
        "3001-5000 GB                           821       \n"
        "5001-9000 GB                           1006      \n"
        "9001-114256 GB                         707"
    ),
    "disk_space_range_prod_env_by_terabyte": (
        "Environment                            prod       \n"
        "0-2000 GB                              34621     \n"
        "2001-9000 GB                           2805      \n"
        "9001-114256 GB                         707"
    ),
    "os_min_counts": (
        "OS Name\n"
        "Ubuntu Linux                16583\n"
        "Microsoft Windows Server    13732\n"
        "Oracle Linux                10589\n"
        "Microsoft Windows            7280\n"
        "SUSE Linux Enterprise        1991\n"
        "Red Hat Enterprise Linux     1150\n"
        "CentOS                        592"
    ),
    "supported_os_all_envs": (
        "OS Name\n"
        "Microsoft Windows Server    13732\n"
        "Microsoft Windows            7280\n"
        "SUSE Linux Enterprise        1991\n"
        "Red Hat Enterprise Linux     1150"
    ),
    "supported_os_both_envs": (
        "Environment               non-prod   prod\n"
        "OS Name\n"
        "Microsoft Windows              399   6881\n"
        "Microsoft Windows Server      3614  10118\n"
        "Red Hat Enterprise Linux       437    713\n"
        "SUSE Linux Enterprise          644   1347"
    ),
    "supported_os_min_count": (
        "OS Name\n"
        "Microsoft Windows Server    13732\n"
        "Microsoft Windows            7280\n"
        "SUSE Linux Enterprise        1991\n"
        "Red Hat Enterprise Linux     1150"
    ),
    "supported_os_non_prod": (
        "OS Name\n"
        "Microsoft Windows Server    3614\n"
        "SUSE Linux Enterprise        644\n"
        "Red Hat Enterprise Linux     437\n"
        "Microsoft Windows            399"
    ),
    "unsupported_os_both": (
        "OS Name\n"
        "Ubuntu Linux    16583\n"
        "Oracle Linux    10589\n"
        "CentOS            592\n"
        "Other             671"
    ),
}
