import os
import argparse

from datetime import datetime, timedelta


def parse_args():
    parser = argparse.ArgumentParser("PaddleClas train script")
    parser.add_argument(
        '-f',
        '--log_path',
        type=str,
        help='log file path')
    parser.add_argument(
        '-g',
        '--gpu',
        type=int,
        default=1,
        help='number of gpus')
    args = parser.parse_args()
    return args


def main(args):
    log_file = args.log_path
    f = open(log_file, "r")
    ips = 0.0
    length = 0
    start_time = None
    end_time = None
    for line in f:
        if "epoch" not in line or "ips" not in line or "reader_cost" not in line:
            continue

        ips += float(line.split(",")[-1].split(" ")[-2])
        length += 1

        if not start_time:
            date_str = line.split("INFO")[0].strip(" ")
            start_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            
        date_str = line.split("INFO")[0].strip(" ")
        end_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    print("result: {:.2f} images/s, {:.2f} m/epoch.".format(ips/length * args.gpu, (end_time - start_time).seconds / 60))


if __name__ == '__main__':
    args = parse_args()
    main(args)
