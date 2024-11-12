from gooey import Gooey, GooeyParser

@Gooey(program_name="GPFS Snap Command GUI", 
       default_size=(700, 700),
       description="GUI for executing gpfs.snap command with configurable options.")
def main():
    parser = GooeyParser(description="Configure gpfs.snap command options")
    
    # Required options
    parser.add_argument("-c", "--CommandString", type=str, help="Specify the command string to run on nodes (enclose in double quotes)", widget="TextField")
    parser.add_argument("-d", "--OutputDirectory", type=str, default="/tmp/gpfs.snapOut", help="Specify the output directory", widget="DirChooser")

    # Toggle options
    parser.add_argument("-m", action="store_true", help="Exclude merge logs with -N option")
    parser.add_argument("-z", action="store_true", help="Collect data only from the node on which the command is invoked")
    parser.add_argument("-a", action="store_true", help="Collect data from all nodes in the cluster (default)")
    
    # Node selection
    parser.add_argument("-N", "--Nodes", type=str, help="Specify nodes (Node[,Node...] | NodeFile | NodeClass)")

    # Check space options
    parser.add_argument("--check-space", action="store_true", help="Perform space checking before collecting data")
    parser.add_argument("--no-check-space", action="store_true", help="No space checking (default)")
    parser.add_argument("--check-space-only", action="store_true", help="Perform only space checking, without data collection")
    
    # Deadlock options
    parser.add_argument("--deadlock", action="store_true", help="Collect minimum data needed for deadlock debugging")
    parser.add_argument("--quick", action="store_true", help="Collect less data for deadlock debugging (with --deadlock)")
    
    # Exclusion options
    parser.add_argument("--exclude-aix-disk-attr", action="store_true", help="Exclude data about AIX disk attributes")
    parser.add_argument("--exclude-aix-lvm", action="store_true", help="Exclude data about AIX Logical Volume Manager")
    parser.add_argument("--exclude-net", action="store_true", help="Exclude network-related information")
    parser.add_argument("--exclude-merge-logs", action="store_true", help="Exclude merge logs and waiters")

    # Additional options
    parser.add_argument("--gather-logs", action="store_true", help="Gather, merge, and sort mmfs.log files")
    parser.add_argument("--mmdf", action="store_true", help="Collect mmdf output")
    parser.add_argument("--prefix", action="store_true", help="Add prefix name gpfs.snap to the tar file")
    
    args = parser.parse_args()
    
    # Construct the command string based on user inputs
    command = "gpfs.snap"
    if args.CommandString:
        command += f' -c "{args.CommandString}"'
    if args.OutputDirectory:
        command += f' -d "{args.OutputDirectory}"'
    if args.m:
        command += " -m"
    if args.z:
        command += " -z"
    if args.a:
        command += " -a"
    if args.Nodes:
        command += f' -N "{args.Nodes}"'
    if args.check_space:
        command += " --check-space"
    if args.no_check_space:
        command += " --no-check-space"
    if args.check_space_only:
        command += " --check-space-only"
    if args.deadlock:
        command += " --deadlock"
    if args.quick:
        command += " --quick"
    if args.exclude_aix_disk_attr:
        command += " --exclude-aix-disk-attr"
    if args.exclude_aix_lvm:
        command += " --exclude-aix-lvm"
    if args.exclude_net:
        command += " --exclude-net"
    if args.exclude_merge_logs:
        command += " --exclude-merge-logs"
    if args.gather_logs:
        command += " --gather-logs"
    if args.mmdf:
        command += " --mmdf"
    if args.prefix:
        command += " --prefix"

    print("Generated Command:", command)
    
    # Execute the command (if you want to run it directly, uncomment below)
    # os.system(command)

if __name__ == "__main__":
    main()
