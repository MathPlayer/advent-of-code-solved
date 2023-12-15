#!/usr/bin/env python3

from intervaltree import IntervalTree, Interval


def read_data(filename):

    with open(filename) as f:
        raw = [line.strip() for line in f.readlines()]

    almanac = {}
    seeds = IntervalTree()
    mode = ''
    for line in raw:
        if not line:
            mode = ''
            continue
        if line.startswith('seeds'):
            numbers = line.split(':')[-1].strip().split(' ')
            numbers = [int(s) for s in numbers]
            for start, end in zip(numbers[::2], numbers[1::2]):
                seeds[start:start+end] = True
            continue
        if line.endswith('map:'):
            mode = line.split()[0]
            continue

        if mode:
            if mode not in almanac:
                almanac[mode] = IntervalTree()
            numbers = [int(x) for x in line.split()]
            for dst, src, size in zip(numbers[::3], numbers[1::3], numbers[2::3]):
                almanac[mode][src:src+size] = (dst, dst+size)

    return seeds, almanac


def merge_overlapping(intervals: IntervalTree):
    result = IntervalTree()
    for interval in intervals:
        result[interval.begin:interval.end] = True

    sorted_intervals = sorted(intervals)
    merged = []
    for interval in sorted_intervals:
        if not merged or merged[-1].end < interval.begin:
            merged.append(interval)
        else:
            merged[-1] = Interval(
                merged[-1].begin,
                max(merged[-1].end, interval.end),
                True
            )

    return IntervalTree(merged)


def transform_intervals(intervals: IntervalTree, mapping: IntervalTree):
    result = IntervalTree()
    for interval in intervals:
        begin, end = interval.begin, interval.end

        overlap = IntervalTree()
        for transformation in mapping[begin:end]:
            src_begin, src_end = transformation.begin, transformation.end
            dst_begin, dst_end = transformation.data

            overlap_begin = max(begin, src_begin)
            overlap_end = min(end, src_end)

            overlap_offset = overlap_begin - src_begin

            new_dst_begin = dst_begin + overlap_offset
            new_dst_end = new_dst_begin + overlap_end - overlap_begin

            result[new_dst_begin:new_dst_end] = True

            overlap[overlap_begin:overlap_end] = True

        leftover = IntervalTree()
        leftover.add(interval)
        leftover.difference_update(overlap)
        leftover = merge_overlapping(leftover)

        if not leftover.is_empty and leftover.span:
            result.update(leftover)
            result = merge_overlapping(result)

    return result


def solve(filename):
    intervals, almanac = read_data(filename)

    for mode in almanac:
        intervals = transform_intervals(intervals, almanac[mode])

    print(intervals.begin())


filename = 'test'
filename = 'input'

solve(filename)

print("DONE")
